from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def next(request):
	return render(request,'accounts/next.html')

def okay(request):
	return render(request,'accounts/okay.html')

def okay1(request):
	return render(request,'accounts/okay1.html')

def log(request):
	return render(request,'accounts/log.html')

def signup_view(request):
        if request.method =='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'accounts/okay.html')
        else:
            form = UserCreationForm()
        return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request,'accounts/next.html')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
