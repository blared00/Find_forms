# Web-приложение для определения заполненных форм.
******
Данное приложение не содержит визуальной оболочки и создавалось в учебных целях 
******
### Задание

В базе данных хранится список шаблонов форм.

На вход по url  /get_form POST запросом передаются данные такого вида:
f_name1=value1&f_name2=value2

В ответ нужно вернуть имя шаблона формы, поля которой совпали с полями в запросе. Совпадающими считаются поля, у которых совпали имя и тип значения. Полей в запросе может быть больше, чем в шаблоне. В этом случае шаблон все равно будет считаться подходящим. Самое главное, чтобы все поля шаблона присутствовали в запросе.

### Входные данные для веб-приложения:
Список полей со значениями в теле POST запроса.

### Выходные данные:
Имя наиболее подходящей данному списку полей формы, при отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.
****
## Запуск web-приложения

~~~docker
docker-compose build --no-cache
docker-compose up -d
~~~
Для проверки работоспособности запустить script_requests.py   
