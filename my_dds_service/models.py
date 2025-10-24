from django.db import models

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
