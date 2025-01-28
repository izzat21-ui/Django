import json
from os.path import join

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from root.settings import BASE_DIR


# Create your views here.

# def todo_list(request):
#     with open(join(BASE_DIR, 'dumpy', 'todos.json')) as f:
#         data = json.load(f)
#     return JsonResponse(data)
#
# def view_home(request):
#     return render(request, "index.html")
#
# def get_id(request):
#     with open(join(BASE_DIR, 'dumpy', 'todos.json')) as f:
#         data = json.load(f)
#     ids = [item['id'] for item in data]
#     return JsonResponse(ids)
#
# def get_user(request):
#     with open(join(BASE_DIR, 'dumpy', 'todos.json')) as f:
#         data = json.load(f)
#     names = [item['username'] for item in data]
#     return JsonResponse({"username": names})
#
# def html_code(request):
#     users = User.objects.all()
#
#     return render(request, "index.html", context)


def get_user(request):
    users = User.objects.all()
    context = {"users": users}

    return render(request, "User.html", context)
