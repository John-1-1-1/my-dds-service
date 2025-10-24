from django.template.defaultfilters import register


@register.filter(name='get')
def get(dictionary, key):
    """Возвращает значение по ключу из словаря."""
    return dictionary.get(key)