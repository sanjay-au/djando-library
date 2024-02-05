from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from student.models import Students
from student.models import MyUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        s=request.POST['s']
        ph=request.POST['ph']
        a=request.POST['a']
        if(p==cp):
            user=MyUser.objects.create_user(username=u,password=p,first_name=f,last_name=s,email=e,phone=ph,place=a)
            user.save()
            user=authenticate(username=u, password=p)
            if user:
                login(request, user)
                return redirect('books:home')
            else:
                return HttpResponse("Invalid Credentials")
        else:
            return HttpResponse("Password must be same")
    return render(request,'register.html')
@login_required
def viewstudents(request):
    k=Students.objects.all()
    return render(request,'viewstudents.html',{'b':k})
@login_required
def user_logout(request):
    logout(request)
    return redirect('student:login')