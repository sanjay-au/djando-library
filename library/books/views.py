from django.db.models import Q
from django.shortcuts import render
from books.models import Book
from books.forms import bookform
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        f=request.FILES['pdf']
        i=request.FILES['cover']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbooks(request)
    return render(request,'addbooks.html')
@login_required
def viewbooks(request):
    k=Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})
@login_required
def addbooks1(request):
    if(request.method=="POST"):
        form=bookform(request.POST)     #creates form objects with values inside
        if form.is_valid():
            form.save()     #saves in model db
            return viewbooks(request)
    form=bookform()     #creates empty forms
    return render(request,'addbooks1.html',{'form':form})
@login_required
def factorial(request):
    if(request.method=="POST"):
        n=request.POST['n']
        n=int(n)
        fact=1
        for i in range(1,n+1,1):
            fact=fact * i
        return render(request,'factorial.html',{'b':fact})
    return render(request,'factorial.html')
@login_required
def viewdetails(request,p):
    b=Book.objects.get(id=p)
    return render(request,'viewdetails.html',{'b':b})
@login_required
def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)
@login_required
def edit(request,p):
    b = Book.objects.get(id=p)
    if (request.method == "POST"):
        form = bookform(request.POST,request.FILES,instance=b)  # creates form objects with values inside
        if form.is_valid():
            form.save()  # saves in model db
            return viewbooks(request)
    form=bookform(instance=b)
    return render(request,'edit.html',{'form':form})
@login_required
def search(request):
    b=None
    q=""
    if(request.method=="POST"):
        q=request.POST['search']
        b=Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})
