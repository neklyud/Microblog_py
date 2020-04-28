import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Translation service is not configured')

    if 'YANDEX_TRANSLATOR_URL' not in current_app.config or not current_app.config['YANDEX_TRANSLATOR_URL']:
        return _('Translation service is not configured')
    
    params = {
        "key": current_app.config['YANDEX_TRANSLATOR_KEY'],     
        "text": text,
        "lang": dest_language
    }
    r = requests.get(current_app.config['YANDEX_TRANSLATOR_URL'], params = params)
    if r.status_code != 200:
        return _('Error: the translation service failed.' + str(r.status_code))
    return json.loads(r.content.decode('utf-8-sig'))
