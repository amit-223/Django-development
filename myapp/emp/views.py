from django.shortcuts import render, redirect
from .models import Emp, Feedback
from .models import Testimonial
from .forms import Feedbackform

# Create your views here.
#Employee management App
def empfunc(request):
    # return  HttpResponse("Emp Homepage")
    # return render(request, "emp/home.html",{})
    emps=Emp.objects.all()
    return render(request, "emp/home.html",{'emps' : emps})

def ffunc(request): 
    feed = Feedback.objects.all()
    return render(request,'emp/home.html', { 'feed' : feed})

def add_emp(request):
    if request.method=="POST":
           #data fetch from add_emp.html
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_phone = request.POST.get('emp_phone')
        e= Emp()
        e.id = emp_id
        e.name = emp_name
        e.phone = emp_phone
        e.save() # save all data to django data server
        print("data coming...")
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def del_emp(request,e_id):
    e = Emp.objects.get(id=e_id)
    print(e)
    e.delete()
    return redirect('/emp/home/')


    #data fetch
        # emp_name= request.POST.get("emp_name")
        # emp_id= request.POST.get("emp_id")
        # emp_phone= request.POST.get("emp_phone")
        # emp_department= request.POST.get("emp_department")
        # emp_working= request.POST.get("emp_working")
     
        #create model object & set the data
        # e=Emp()
        # e.name=emp_name
        # e.empid=emp_id
        # e.phone=emp_phone
        # e.department=emp_department
        # if emp_working is None:
        #     e.working=False  
        # else:
        #     e.working=True
        # e.save()
    
        



        

def testimonials(request):
    t = Testimonial.objects.all()
    return render(request, "emp/testimonials.html",{ 
        t:t
    })
def feedback(request):
    if request.method == 'POST':
        print('ok')
        # name = request.POST['name'] 
        f = Feedback()
        f.name = request.POST.get('name')
        f.message= request.POST.get('message')
        
        # feedback = request.POST['feedback']
        Feedback.objects.create(name=f.name, message=f.message) 
        return redirect("/emp/home/")
    return render(request, "emp/feedback.html",{})