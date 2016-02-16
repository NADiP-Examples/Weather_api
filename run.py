# Установка requests: sudo pip3 install requests
# Если не установлен pip3: sudo apt-get install python3-pip
# requests - модуль для удобной работы с запросами и ответами
import requests
import settings
from datetime import datetime, date

# id городов с названиями и координатами тут: http://bulk.openweathermap.org/sample/city.list.json.gz
# - Это обычный .json  в архиве
city_id = '1496990'
# TODO: если отправить несуществующий id, то вернется json  с ошибкой. Доделать обарботку таких ошибок.
params = {'id': city_id, 'APPID': settings.APPID}

# Подробнее про HTTP запросы тут: http://ruseller.com/lessons.php?rub=28&id=1726
response = requests.get(settings.url, params=params)
# request - запрос, response - ответ

print('full_result = ', response.json())
print('all_keys = ', response.json().keys())
print('city_name = ', response.json()['name'])
date_mc = response.json()['dt']  # Дата в микросекундах

print('date = ', datetime.fromtimestamp(date_mc))