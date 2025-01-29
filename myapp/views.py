#"pip install django" --> django installment command
#initial code 
# django-admin startproject myapp --> it create files like, manage.py
# python manage.py runserver --> it gives url, django have internal server


from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    # print(check=request.POST("check"))
    if request.method=="POST":
        c= request.POST.get("check")
        print(c)
        # if c is None:
        #     isactive=False
        # else:
        #     isactive=True

    d= datetime.datetime.now()
    # isactive=True
    # name="Amit Karmakar"
    # student={'sname':"Prothom", 'sid':"15"}
    # data={'isactive':isactive, 'd':d,'name':name, 'student':student}
    # print("test func is call from view")
    # return HttpResponse("<h1>Index Page </h1>" +str(d))
    return render(request,"home.html")

def about(request):
    # return HttpResponse("<h1>About page </h1>")
    return render(request,"about.html",{})

def service(request):
    # return HttpResponse("<h1>Service page </h1>")   
    return render(request,"service.html",{})

def test1(request):
    return render(request, 'test1.html' ,{})

def test2(request):
    return render(request, 'test2.html' ,{})