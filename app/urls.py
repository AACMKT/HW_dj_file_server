

from django.urls import path
from app.views import file_list, file_content
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    path('', file_list,  name='file_list'),
    path('<str:date>', file_list, name='file_list'),
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('file/<name>', file_content, name='file_content'),
]
