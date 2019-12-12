from django.shortcuts import render
from account.models import *
from main.models import *
# Create your views here.
def main(request):
    return render(request, 'main.html')

def again(request):
    if request.method == 'POST':
        Name = request.POST.get("name")
        Personal_Num1 = request.POST.get("personal_num1")
        Personal_Num2 = request.POST.get("personal_num2")
        users = Profile.objects.filter(Name=Name, Personal_Num1=Personal_Num1, Personal_Num2=Personal_Num2).exists()
        if users:
            return render(request, 'write.html')
        else:
            return render(request, 'again.html')
    return render(request, 'again.html')

def write(request):
    if request.method == 'POST':
        chk_info = request.POST.get("chk_info")
        doctor=Doctor.objects.filter(Type=chk_info)

        return render(request, 'doctor.html',{'doctor':doctor})