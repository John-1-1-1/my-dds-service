import django_filters
from .models import Transaction
from django import forms


class TransactionFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='Дата от',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    created_at__lte = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='lte',
        label='Дата до',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Transaction
        fields = [
            'status',
            'transaction_type',
            'category',
            'subcategory'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        select_fields = ['status', 'transaction_type', 'category', 'subcategory']

        for name, field in self.form.fields.items():
            if name in select_fields:
                field.widget.attrs.update({'class': 'form-select form-select-sm'})
            else:
                field.widget.attrs.update({'class': 'form-control form-control-sm'})