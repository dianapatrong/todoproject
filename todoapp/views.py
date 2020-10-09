from django.shortcuts import render, redirect
from .models import TodoListItem
from .forms import TodoListItemForm


def todo_app_view(request):
    all_todo_items = TodoListItem.objects.all()
    form = TodoListItemForm()
    context = {'items': all_todo_items, 'form': form}
    return render(request, 'todolist.html', context)


def add_item(request):
    form = TodoListItemForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')


def update_item(request, id):
    item = TodoListItem.objects.get(id=id)
    form = TodoListItemForm(instance=item)

    if request.method == 'POST':
        form = TodoListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update_todolist.html', context)


def delete_item(request, i):
    print("REQUEST: ", request, i)
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return redirect('/')
