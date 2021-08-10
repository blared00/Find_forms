from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from list_form.utils import Valid_form, get_db_handle, find_forms


class HomePageView(View):
    """Отображение всех форм в базе данных"""
    def get(self, request):
        db = get_db_handle()
        context = list(map(lambda x: f'{x}</br>', db['forms'].find({}, {'_id': 0})))
        return HttpResponse(context)


class GetFormView(View):
    """Обработка запроса на получение подходящих форм из БД"""
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        context = {'result': ''}
        if request.method == "POST":

            requests_post = request.POST.copy()
            requests_post.pop('csrfmiddlewaretoken', None)
            db = get_db_handle()

            if requests_post:
                keys = requests_post.keys()
                for key in keys:
                    requests_post[key] = Valid_form(requests_post[key]).type_form #Валидация полей и определение
                                                                                  #типа данных для поиска
                result_find = find_forms(db['forms'], requests_post) #Проверка всех возможных комбинаций полей запроса
                result = [form['name'] for form in result_find]
                if result:
                    context['result'] = 'Имена подходящих форм:\n '+'\n '.join(result)
                else:
                    context['result'] = "Форма не найдена, по запросу должна быть такая форма \n{\n      "+',\n      '.join([f'{x}: {y}' for x,y in requests_post.items()])+'\n}'
            else:
                context['result'] = 'Для поиска форм необходимо передать не пустой запрос'
        return HttpResponse(context['result'])
