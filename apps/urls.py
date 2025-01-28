from django.urls import path

from apps.views import get_user

# from apps.views import html_code
#
# from apps.views import todo_list, get_id, get_user, html_code
# from apps.views import view_home


urlpatterns = [
      # path('', view_home),
      # path('get_id', get_id),
      # path('get_user', get_user),
      # path('todos', todo_list),
      # path('html_cod', html_code),
      path("user_list/", get_user),
]



