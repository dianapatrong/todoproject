from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect


def todo_app_view(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo_items})


def add_todo_view(request):
    todo_content = request.POST['content']
    new_todo_item = TodoListItem(content=todo_content)
    new_todo_item.save()
    return HttpResponseRedirect('/todoapp/')


def delete_todo_view(request, i):
    print("REQUEST: ", request, i)
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/')
