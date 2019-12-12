from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def signup(request):
    if request.method == 'POST':
        users = Profile()
        users.Name = request.POST.get("name")
        users.Personal_Num1 = request.POST.get("personal_num1")
        users.Personal_Num2 = request.POST.get("personal_num2")
        users.save()
        return redirect('/')
    return render(request, 'signup.html')

