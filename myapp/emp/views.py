from django.shortcuts import render, redirect
from .models import Emp, Feedback, Testimonial
from .forms import Feedbackform

# Create your views here.
#Employee management App
def empfunc(request):
    # return  HttpResponse("Emp Homepage")
    # return render(request, "emp/home.html",{})
    emps=Emp.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, "emp/home.html",{'emps' : emps, 'feedbacks': feedbacks,})
   

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

def testimonials(request):
    if request.method == 'POST':
        t = Testimonial()
        t.name = request.POST['name']
        t.testimonial = request.POST['testimonial'] 
        t.rating = request.POST ['rating']
        Testimonial.objects.create(name = t.name,testimonial=t.testimonial,rating=t.rating)
        return redirect('/emp/home/')
    return render(request, 'emp/testimonials.html')

def feedback(request):
    # Feedbacks are only deleted from admin for that, goto admin/feebacks/delete manually
    
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