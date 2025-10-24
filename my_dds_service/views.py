from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TransactionStatus, TransactionType, Category, Subcategory


class TransactionStatusCreateView(CreateView):
    model = TransactionStatus
    fields = ['name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class TransactionStatusUpdateView(UpdateView):
    model = TransactionStatus
    fields = ['name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class TransactionStatusDeleteView(DeleteView):
    model = TransactionStatus
    success_url = reverse_lazy('all_lists')

class TransactionTypeCreateView(CreateView):
    model = TransactionType
    fields = ['name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    fields = ['name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    success_url = reverse_lazy('all_lists')

class CategoryCreateView(CreateView):
    model = Category
    fields = ['type', 'name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['type', 'name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('all_lists')



class SubcategoryCreateView(CreateView):
    model = Subcategory
    fields = ['category', 'name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    fields = ['category', 'name']
    template_name = 'crud_form.html'
    success_url = reverse_lazy('all_lists')

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('all_lists')


from django.views.generic import TemplateView


class AllListsView(TemplateView):
    template_name = 'all_lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        simple_headers = ['Название']
        simple_fields = ['name']

        context['status_table'] = {
            'title': "Статусы транзакций",
            'object_list': TransactionStatus.objects.all(),
            'headers': simple_headers,
            'create_url': 'transaction_status_create',
            'update_url_name': 'transaction_status_update',
            'delete_url_name': 'transaction_status_delete',
            'display_fields': simple_fields,
        }

        context['type_table'] = {
            'title': "Типы транзакций",
            'object_list': TransactionType.objects.all(),
            'headers': simple_headers,
            'create_url': 'transaction_type_create',
            'update_url_name': 'transaction_type_update',
            'delete_url_name': 'transaction_type_delete',
            'display_fields': simple_fields,
        }

        context['category_table'] = {
            'title': "Категории",
            'object_list': Category.objects.all(),
            'headers': ['Название', "Родительский тип"],
            'create_url': 'category_create',
            'update_url_name': 'category_update',
            'delete_url_name': 'category_delete',
            'display_fields': ['name', 'type.name'],
        }

        context['subcategory_table'] = {
            'title': "Подкатегории",
            'object_list': Subcategory.objects.all().select_related('category'),
            'headers': ['Название', 'Родительская категория'],
            'create_url': 'subcategory_create',
            'update_url_name': 'subcategory_update',
            'delete_url_name': 'subcategory_delete',
            'display_fields': ['name', 'category.name'],
        }

        return context