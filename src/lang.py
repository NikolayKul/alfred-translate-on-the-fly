
def is_russian(text):
    try:
        text.decode('ascii')
        return False
    except (UnicodeDecodeError, UnicodeEncodeError):
        return True


def get_lang(text):
    return 'ru' if is_russian(text) else 'en'


def get_translation_lang(text):
    return 'ru-en' if is_russian(text) else 'en-ru'
