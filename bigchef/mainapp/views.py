from django.shortcuts import render, redirect,get_object_or_404
from .models import  Appointment, HomeSlider,Chef, About,Blog,Meal
from .forms import AppointmentForm
from accounts.models import Comment
from accounts.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def home(request): 
    slider= HomeSlider.objects.all()  
    
    context= {    
        "slider": slider   
        
    }
    return render(request,'pages/home.html',context)

def about(request): 
    abouts= About.objects.all() 
    
    context= {   
        "abouts": abouts     
        
    }
    return render(request,'pages/about.html',context)

def menu(request):  
    breakfast=Meal.objects.filter(cinsi='breakfast') 
    lunch=Meal.objects.filter(cinsi='lunch') 
    dinner=Meal.objects.filter(cinsi='dinner') 
    allmeal=Meal.objects.all()
    
    context= { 
        "breakfast":breakfast,   
        "lunch":lunch, 
        "dinner":dinner, 
        "allmeal":allmeal,
        
    }
    return render(request,'pages/menu.html',context)

def chefs(request):
    chefs= Chef.objects.all() 
    

    context= {  
        "chefs": chefs      
        
    }
    return render(request,'pages/chefs.html',context)

def reservation(request):
    formobj=Appointment.objects.all()
    

    if request.method=="POST":                
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        quantity=request.POST['quantity']
        email=request.POST['email']
        message=request.POST['message']        
        desiredate=request.POST['desiredate']
        desiretime=request.POST['desiretime']

        
        print(email)
        rez=Appointment(first_name=first_name,last_name=last_name,quantity=quantity,email=email,message=message,desire_date=desiredate,desire_time=desiretime)
        
        rez.save()
        #maili burada göndereceğiz
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'reservation',
                'Hello ' +first_name +' '+ last_name +' your reservation status iswaiting we will send mail if its accept. You will have a meal on Moon' ,
                admin_email,
                [email],                
                fail_silently=False,
            )
        return redirect('home')


    context= {    
        
    }
    return render(request,'pages/reservation.html')







def blog(request):   
    blogs= Blog.objects.all()
    context= {       
        "blogs": blogs  
    }
    return render(request,'pages/blog.html',context)



def blogdetail(request,category_slug): 
    
    if category_slug != None:
        blogs = get_object_or_404(Blog, slug=category_slug)
        user = request.user
        comments = Comment.objects.filter(blog=blogs).order_by('date')

        if request.method == 'POST':
            forms = CommentForm(request.POST)
            if forms.is_valid():
                comment = forms.save(commit=False)
                comment.blog = blogs
                comment.user = user
                comment.save()
                return HttpResponseRedirect(reverse('blogdetail', args=[category_slug]))
        else:
            forms = CommentForm()
        
    context= {  
        "blogs": blogs,
        "comments": comments,
        "forms": forms     
    }
    return render(request,'detail/blogdetail.html',context)

def chefdetail(request,id):
    chefquery= Chef.objects.all()
    chefs=get_object_or_404(chefquery, id=id)
    
    
    context= {  
        "chefs": chefs   
    }      
    
    return render(request,'detail/chefdetail.html',context)

def fooddetail(request,id): 

    foodquery= Meal.objects.all()
    foods=get_object_or_404(foodquery, id=id)
    
    
    context= {  
        "foods": foods   
    }
    return render(request,'detail/fooddetail.html',context)

def appointments(request):   
    appointments= Appointment.objects.all()
    if request.method=="POST":
        appointmentsAccept= Appointment.objects.get(id=request.POST['id'])
        appointmentsAccept.accepted=request.POST['status']
        appointmentsAccept.save()
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        if appointmentsAccept.accepted=="Accept":
            send_mail(
                'Reservation Accpet BigChef',
                'Hello ' +appointmentsAccept.first_name +' '+ appointmentsAccept.last_name +' your reservation status Accepted You will have a meal on Moon with LOVE' ,
                admin_email,
                [appointmentsAccept.email],                
                fail_silently=False,
            )
        elif appointmentsAccept.accepted=="Decline":
            send_mail(
                'Reservation Declined BigChef',
                'Hello ' +appointmentsAccept.first_name +' '+ appointmentsAccept.last_name +' your reservation status Declined We are Sorry :(' ,
                admin_email,
                [appointmentsAccept.email],                
                fail_silently=False,
            )

        
        
        return redirect('appointments')          
        
    
    context= {     
        "appointments": appointments  
    }
    return render(request,'pages/appointments.html',context)

def appointmentsdetail(request,id):
    appointments= Appointment.objects.all()
    appointquery=get_object_or_404(appointments, id=id)
    context= {     
        "appointquery": appointquery 
    }

    return render(request,'detail/appointdetail.html',context)


