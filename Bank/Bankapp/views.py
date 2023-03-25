from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import district, bran
from .forms import MyForm


# Create your views here.
def Homepage(request):
    return render(request, 'home.html')

def login(request):

    return render(request, 'login.html')

def reg(request):
    
    return render(request, 'register.html')

def tofill(request):
    
    return render(request, 'tofill.html')

def adddet(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'details.html',{'form':form})


def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = bran.objects.filter(district_id=district_id).all()
    return render(request,'branch_dropdown.html', {'branches' :branches})

def accept(request):
    return render(request, 'accept.html')

