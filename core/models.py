from django.db import models


class Customer(models.Model):
    username = models.CharField('Логин покупателя', max_length=20, unique=True)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username


class Item(models.Model):
    name = models.CharField('Название', max_length=20, unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Deal(models.Model):
    customer = models.ForeignKey(
        Customer,
        verbose_name='Покупатель',
        on_delete=models.CASCADE,
        related_name='deals',
    )
    item = models.ForeignKey(
        Item,
        verbose_name='Товар',
        on_delete=models.CASCADE,
        related_name='deals',
    )
    total = models.PositiveIntegerField('Сумма сделки')
    quantity = models.PositiveIntegerField(
        'Количество',
        help_text='Количество товара, в штуках',
    )
    date = models.DateTimeField('Дата сделки')

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ('-date',)

    def __str__(self) -> str:
        return f'{self.customer.username}-{self.item.name}'
