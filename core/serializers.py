from typing import List

from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from core import models


class Customer(serializers.ModelSerializer):
    spent_money = serializers.IntegerField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = models.Customer
        fields = '__all__'

    def get_gems(self, obj: models.Customer) -> List[str]:
        return list(
            set(obj.deals.filter(item__in=self.context['common_gems']).values_list('item__name', flat=True))
        )


class Deal(serializers.ModelSerializer):
    class Meta:
        model = models.Deal
        fields = '__all__'


class DealFile(serializers.Serializer):
    deals = serializers.FileField(required=True, validators=[FileExtensionValidator(['csv'])])
