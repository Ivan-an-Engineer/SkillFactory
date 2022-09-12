import json
import requests
from config import exchanges, user_exchanges, payload, headers


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            if base in exchanges.keys():
                base_key = exchanges[base]
            else:
                base_key = user_exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена! Список валют: /values")

        try:
            if sym in exchanges.keys():
                sym_key = exchanges[sym]
            else:
                sym_key = user_exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена! Список валют: /values")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        if len(amount) > 9:
            raise APIException(f'Слишком большое количество конвертируемой валюты!')
        
        try:
            amount = float(amount)
            if amount == 0:
                raise APIException(f'Введите ненулевое количество валюты!')
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"
        response = requests.request("GET", url, headers=headers, data=payload)
        d = json.loads(response.content)

#        status_code = response.status_code Нужен для отладки
        total_price = round(float(d.get('result')), 3)
        message = f"Стоимость {amount} {base} в {sym} : {total_price}"
        return message
