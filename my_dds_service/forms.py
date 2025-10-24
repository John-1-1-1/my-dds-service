from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction, Subcategory


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'subcategory', 'amount', 'comment', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        """Серверная валидация обязательности полей и логики "Категория/Подкатегория"."""
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')

        if amount is None or amount <= 0:
            raise ValidationError("Сумма должна быть положительной.", code='invalid_amount')

        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        type = cleaned_data.get('transaction_type')

        if category and category.type != type:
            self.add_error('subcategory', "Выбранная категория не принадлежит выбранному типу.")
        if category and Subcategory.objects.filter(category=category).exists():
            if not subcategory:
                self.add_error('subcategory', "Для выбранной категории 'Подкатегория' обязательна.")
        if subcategory and subcategory.category != category:
            self.add_error('subcategory', "Выбранная подкатегория не принадлежит выбранной категории.")

        return cleaned_data