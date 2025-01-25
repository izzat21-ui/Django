from django.urls import path
from apps.views import todo_list, get_id, get_user
from apps.views import view_home


urlpatterns = [
      path('', view_home),
      path('get_id', get_id),
      path('get_user', get_user),
      path('todos', todo_list),
]



