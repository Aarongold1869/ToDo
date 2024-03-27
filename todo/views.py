from django.shortcuts import render


def home_view(request):
    title = 'Welcome to the Todo App'
    return render(request, 'todo.html', {'title': title})