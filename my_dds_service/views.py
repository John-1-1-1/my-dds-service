from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .filters import TransactionFilter
from .forms import TransactionForm
from .models import TransactionStatus, TransactionType, Category, Subcategory, Transaction


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
            'create_form_name': "Статусов транзакций",
            'object_list': TransactionStatus.objects.all(),
            'headers': simple_headers,
            'create_url': 'transaction_status_create',
            'update_url_name': 'transaction_status_update',
            'delete_url_name': 'transaction_status_delete',
            'display_fields': simple_fields,
        }

        context['type_table'] = {
            'title': "Типы транзакций",
            'create_form_name': "Типов транзакций",
            'object_list': TransactionType.objects.all(),
            'headers': simple_headers,
            'create_url': 'transaction_type_create',
            'update_url_name': 'transaction_type_update',
            'delete_url_name': 'transaction_type_delete',
            'display_fields': simple_fields,
        }

        context['category_table'] = {
            'title': "Категории",
            'create_form_name': "Категории",
            'object_list': Category.objects.all(),
            'headers': ['Название', "Родительский тип"],
            'create_url': 'category_create',
            'update_url_name': 'category_update',
            'delete_url_name': 'category_delete',
            'display_fields': ['name', 'type.name'],
        }

        context['subcategory_table'] = {
            'title': "Подкатегории",
            'create_form_name': "Подкатегории",
            'object_list': Subcategory.objects.all().select_related('category'),
            'headers': ['Название', 'Родительская категория'],
            'create_url': 'subcategory_create',
            'update_url_name': 'subcategory_update',
            'delete_url_name': 'subcategory_delete',
            'display_fields': ['name', 'category.name'],
        }

        return context

class TransactionCreateUpdateView(CreateView, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'crud_transaction_form.html'
    success_url = reverse_lazy('transaction_list')

    def get_object(self, queryset=None):
        if self.kwargs.get('pk'):
            return super().get_object(queryset)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = Transaction._meta.verbose_name
        return context


def load_categories(request):
    """AJAX-представление: возвращает JSON-список категорий для выбранного типа."""
    type_id = request.GET.get('type_id')

    categories = Category.objects.filter(type_id=type_id).order_by('name')

    data = [{'id': category.pk, 'name': category.name} for category in categories]

    return JsonResponse(data, safe=False)


def load_subcategories(request):
    """AJAX-представление: возвращает список подкатегорий в формате JSON."""
    category_id = request.GET.get('category_id')

    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')

    data = [{'id': subcategory.pk, 'name': subcategory.name} for subcategory in subcategories]

    return JsonResponse(data, safe=False)

class TransactionListView(FilterView):
    model = Transaction
    filterset_class = TransactionFilter
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = Transaction._meta.verbose_name_plural
        return context


class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transaction_list')
