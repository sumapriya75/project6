from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("<h1> hello world</h1>")
def sample1(request):
    return render(request,'app1/sample1.html')