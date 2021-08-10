from pymongo import MongoClient
from _datetime import datetime
from itertools import combinations
from web_setting.settings import DATABASE


def get_db_handle():
    """Подключение к БД"""
    client = MongoClient(host=DATABASE['host'],
                         port=DATABASE['port'],
                         # username=DATABASE['user'],
                         # password=DATABASE['password']
                         )
    db_handle = client[DATABASE['db_name']]
    return db_handle


class Valid_form:
    """Валидация полей отправленного запроса.
    Согласно заданию необходимо валидацию производить в следующем порядке:
     1. Дата.
     2. Телефон
     3. Почта
     Непрошедшим валидацию полям  присуждается тип поля 'text'
    """
    def __init__(self, value):
        self.value = value
        self.type_form = self.valid_date()

    def valid_date(self):
        try:
            datetime.strptime(self.value, '%Y-%m-%d')
            return 'date'
        except ValueError:
            try:
                datetime.strptime(self.value, '%d.%m.%Y')
                return 'date'
            except ValueError:
                return self.valid_phone()

    def valid_phone(self):
        if self.value.startswith('+7'):
            phone_number = ''.join(list(self.value[2:]))
            if len(phone_number) == 10 and phone_number.isdigit():
                return 'phone'
        return self.valid_email()

    def valid_email(self):
        email = self.value.split('@', maxsplit=1)
        if len(email) == 2:
            if len(email[1].split('.')) == 2:
                return 'email'
        return 'text'


def find_forms(db, request):
    """Поиск подходящих форм
    Подходящими считаются поля, у которых совпали имя и тип значения.
    Полей в запросе может быть больше, чем в шаблоне.
    В этом случае шаблон все равно будет считаться подходящим.
    Самое главное, чтобы все поля шаблона присутствовали в запросе. """
    result = []
    if len(request) == 0:
        pass
    else:
        for count_field_in_find in range(1, len(request)+1):
            iter_find = combinations(request.items(), count_field_in_find) #Перебор комбинаций полей
            iter_find = list(map(lambda x: dict(x), iter_find))
            for comb in iter_find:
                list_form = db.find(comb, {'_id': 0})
                result += list((filter(lambda x: len(x) == count_field_in_find+1, list_form)))
    return result


