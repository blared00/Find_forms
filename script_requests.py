import requests


HOST_URL = 'http://localhost:8080'
FIELDS_FOR_FIND = [{'new_email': 'edsad@gmail.com',
                    'email': 'email@mail.ru'},

                   {'new_email': 'edsad@gmail.com',
                    'email': 'email@mail.ru',
                    'first_name': 'Michal',},
                   {'new_email': 'edsad@gmail.com',
                    'email': 'email@mail.ru',
                    'first_name': 'Michal',
                    'date':'13.12.2000'},
                   {},
                   {'empty':'Sometimes not empty',
                    'lazy_day': '2021-04-08'}
                   ]


def get_form(field_for_find):
    """Функция отправки POST запроса на получение списка подходящих форм"""
    print(field_for_find)
    response2 = requests.post(f'{HOST_URL}/get_form', data=field_for_find)
    print(response2.content.decode('utf-8'))


if __name__ == '__main__':
    response = requests.get(HOST_URL)

    if response.status_code == 200:

        print('Список шаблонов в базе данных',
              response.content.decode('utf-8').replace('</br>', '\n'),
              'Сервер успешно открыт, направляем POST запрос ',
              sep='\n')

        for n in range(len(FIELDS_FOR_FIND)):
            print(f'\n№{n+1}')
            get_form(FIELDS_FOR_FIND[n])
    else:
        print('Сервер отключен')

