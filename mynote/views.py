from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def test(request):
    return render(request,'test.html')

def addData(request):
    return render(request, '')

def saveData(request):
    return render(request, '')

def updateData(request):
    return render(request, '')

def delData(request):
    return render(request, '')

def queryData(request):
    return render(request, '')
