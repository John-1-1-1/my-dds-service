from django.db import models
from django.utils import timezone

class TransactionStatus(models.Model):
    """Модель для статуса записи ДДС (Бизнес, Личное, Налог)."""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = "Статус транзакции"
        verbose_name_plural = "Статусы транзакций"

    def __str__(self):
        return self.name

class TransactionType(models.Model):
    """Модель для типа операции."""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Тип операции"
    )

    class Meta:
        verbose_name = "Тип транзакции"
        verbose_name_plural = "Типы транзакций"

    def __str__(self):
        return self.name

class Category(models.Model):
    """Модель для Категорий."""

    type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name='type',
        verbose_name="Родительский тип"
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.type.name}: {self.name}"

class Subcategory(models.Model):
    """Модель для Подкатегорий."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name="Родительская категория"
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Подкатегория"
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name}: {self.name}"

class Transaction(models.Model):
    """Основная модель записи о движении денежных средств (ДДС)."""
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания записи"
    )

    status = models.ForeignKey(
        TransactionStatus,
        on_delete=models.PROTECT,
        verbose_name="Статус",
        null=True,
        blank=True
    )

    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        verbose_name="Тип"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        verbose_name="Подкатегория"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма"
    )

    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий"
    )

    class Meta:
        verbose_name = "Транзакция ДДС"
        verbose_name_plural = "Транзакции ДДС"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d')} | {self.transaction_type.name} | {self.amount} р."