from django.template.defaultfilters import register


@register.filter(name='getattribute')
def getattribute(value, arg):
    """
    Получает атрибут объекта или связанные поля по имени строки.
    """

    parts = arg.split('.')
    current = value

    try:
        for part in parts:
            if hasattr(current, part):
                current = getattr(current, part)
            elif isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
    except Exception:
        return None
    if callable(current):
        return current()

    return current