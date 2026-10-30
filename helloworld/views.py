from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'detail.html')

def form(request, ):
    form = UserForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        return HttpResponse("响应成功")
    return render(request, 'form.html', {'form': form})