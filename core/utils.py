from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
import pandas as pd

from core import models, serializers


def get_common_gems(queryset: QuerySet[models.Customer]) -> set:
    customers = models.Customer.objects.filter(id__in=queryset.values_list('id', flat=True))
    items_list = list(customers.values_list('deals__item', flat=True).distinct())
    common_gems = {x for x in items_list if items_list.count(x) >= 2}
    return common_gems


def parse_csv(file: InMemoryUploadedFile) -> None:
    fields = ['customer', 'item', 'total', 'quantity', 'date']

    df = pd.read_csv(file, encoding='utf-8')

    if list(df.columns.values) != fields:
        raise ValidationError('Проверьте правильность заданных колонок')

    for _, row in df.iterrows():
        customer, _ = models.Customer.objects.get_or_create(username=row['customer'])
        item, _ = models.Item.objects.get_or_create(name=row['item'])

        data = {
            'customer': customer.pk,
            'item': item.pk,
            'total': row['total'],
            'quantity': row['quantity'],
            'date': row['date'],
        }

        serializer = serializers.Deal(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
