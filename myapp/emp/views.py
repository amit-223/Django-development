from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp
from .models import Testimonial
from .forms import Feedbackform

# Create your views here.
#Employee management App
def empfunc(request):
    # return  HttpResponse("Emp Homepage")
    # return render(request, "emp/home.html",{})
    emps=Emp.objects.all()
    return render(request, "emp/home.html",{
       ' emps':emps
    })

def add_emp(request):
    if request.method=="POST":
    #data fetch
        emp_name= request.POST.get("emp_name")
        emp_id= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_department= request.POST.get("emp_department")
        emp_working= request.POST.get("emp_working")
     
        #create model object & set the data
        e=Emp()
        e.name=emp_name
        e.empid=emp_id
        e.phone=emp_phone
        e.department=emp_department
        if emp_working is None:
            e.working=False  
        else:
            e.working=True
        e.save()
    
        



        print("data coming...")
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def testimonials(request):
    t = Testimonial.objects.all()
    return render(request, "emp/testimonials.html",{ 
        t:t
    })
def feedback(request):
    if request.method == 'POST':
        pass
    else:
        f=Feedbackform()
        return render(request, "emp/feedback.html",{
            'f':f
        })