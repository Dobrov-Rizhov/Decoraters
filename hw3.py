from functools import wraps
from pprint import pprint
from datetime import datetime

import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20240902T113519Z.ce641082ae0bc9aa.0380ec04addbcf76c23891db3870580399100ae0'

def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        dates = datetime.now()
        result = old_function(*args, **kwargs)
        with open("hw3.log", "a") as log_file:
            log_file.write(
                f'{dates} Вызвана функция: {old_function} \n с аргументами: {args}, {kwargs} и результатом: {result}\n'
            )
        return result

    return new_function

@logger
def translate_word(word):
    param = {
        'key': token,
        'lang': 'ru-en',
        'text': word,
        'ui': 'ru',
    }
    new_trw = []

    response = requests.get(url=url, params=param)
    result = response.json()
    if 'def' in result:
        translation = result['def'][0]['tr'][0]['text']
        new_trw.append(translation)
    else:
        return 'Перевод не найден'
    for translate_word in new_trw:
        return translate_word

if __name__ == '__main__':
    word = 'машина'
    assert translate_word(word) == 'car'