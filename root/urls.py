from django.contrib import admin
from django.urls import path, include

from apps.views import view_home, get_id, get_user

urlpatterns = [
      path('', view_home),
      path('get_id/', get_id),
      path('get_user/', get_user),
      path('admin/', admin.site.urls),
      path("apps/", include('apps.urls')),
]



