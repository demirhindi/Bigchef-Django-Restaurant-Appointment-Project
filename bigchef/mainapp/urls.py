from django.urls import path


from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/', views.blog, name='blog'),
    
    
    path('blogdetail/<slug:category_slug>/',views.blogdetail, name='blogdetail'),
    path('chefdetail/<int:id>/', views.chefdetail, name='chefdetail'),
    path('fooddetail/<int:id>/', views.fooddetail, name='fooddetail'),
    path('appointments/', views.appointments, name='appointments'),    
    path('appointment/<int:id>/',views.appointmentsdetail, name='appointmentsdetail'),
   
    #path('contact/', views.contact, name='contact'),  
     

] 
