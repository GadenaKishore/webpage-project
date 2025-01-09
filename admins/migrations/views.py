from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def adminlogin(request):
    return render(request,'adminlogin.html')

def adminlogincheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            return render(request,'adminhome.html')
        else:
            print('inavalid details')
            messages.success(request,'donkey entered invalid credintials')
    return render(request,'adminlogin.html',{})           
