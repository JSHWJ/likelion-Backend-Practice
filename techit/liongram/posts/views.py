from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Post # 같은 패키지 안에 있어서 .model 이라고 해놓음

# Create your views here.

def url_view(request):
    print('url_view()')
    data = {'code':'001', 'msg':'OK'}
    return HttpResponse('<h1>url_view</ h1>')

def url_parameter_view(request, username):
    print('url_parameter_view()') # 콘솔에 응답
    print(f'username: {username}')
    print(request.GET)
    return HttpResponse(username) # 웹에 응답

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model = Post
    ordering = ['-id']
    template_name = 'cbv_view.html'
