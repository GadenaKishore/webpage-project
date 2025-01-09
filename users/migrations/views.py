from django.shortcuts import render
from .forms import registrationform

# Create your views here.

def basefucntion(request):
    return render(request,'base.html')

def registercheck(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            form = registrationform()
            return render(request,'registration.html',{'form':form})   
    else:
        form = registrationform()
    return render(request,'registration.html',{'form':form})
