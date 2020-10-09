from django.shortcuts import render


def todo_app_view(request):
    return render(request, 'todolist.html')
