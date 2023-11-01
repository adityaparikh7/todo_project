from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

