from django import template

register = template.Library()


@register.filter()
def censor(text):
    CENSOR_WORDS = {
        'Войн': 'В***',
        'войн': 'в***',
        'Путин': 'П****',
        'Украин': 'У*****',
        'Медуз': 'М***',
        'медуз': 'м***',
        'Секс': 'C***',
        'секс': 'с***'
    }
    for i, j in CENSOR_WORDS.items():
        text = text.replace(i, j)
    return f'{text}'
