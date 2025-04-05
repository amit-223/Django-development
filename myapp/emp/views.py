#Employee management Application
from django.shortcuts import render, redirect, get_object_or_404
from .models import Emp, Feedback, Testimonial

def empfunc(request):
    emps=Emp.objects.all()
    feedbacks = Feedback.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "emp/home.html",{'emps' : emps, 'feedbacks': feedbacks,'testimonials' : testimonials})
    #create object of classes & passed emps, feedbacks, testimonials to html through dictonary
   
def add_emp(request):
    if request.method=="POST": #user send post request 
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
        name = request.POST['name']
        testimonial = request.POST['testimonial'] 
        rating = request.POST ['rating']
        Testimonial.objects.create(name = name,testimonial=testimonial,rating=rating)
        return redirect('/emp/home/')
    return render(request, 'emp/testimonials.html', {})

def feedback(request):
    # Feedbacks are only deleted from admin for that, goto admin/feebacks/delete manually
    if request.method == 'POST':
        print('ok')
        name = request.POST['name'] 
        message= request.POST['message']
        Feedback.objects.create(name=name, message=message) 
        return redirect("/emp/home/")
    return render(request, "emp/feedback.html")

def update_emp(request, e_id):
    emp = get_object_or_404(Emp, id= e_id)
    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.phone= request.POST['phone']
        emp.save()
        return redirect('/emp/home/')
    return render(request, 'emp/update-emp.html', {'emp' : emp})
    
        
        