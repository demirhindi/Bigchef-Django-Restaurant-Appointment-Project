from re import T
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.urls import reverse


class HomeSlider(models.Model):
    title= models.CharField(max_length=150,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    photo = models.ImageField(upload_to="slider/slide",blank=True)
    
    class Meta:
        verbose_name='slider'
        verbose_name_plural='sliders'

    

    def __str__(self):
        return self.title

class Meal(models.Model):
    title= models.CharField(max_length=150,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    photo = models.ImageField(upload_to="meal/meal",blank=True)
    cinsi = models.CharField(max_length=250,blank=True)
    
    class Meta:
        verbose_name='meal'
        verbose_name_plural='meal'

    def get_url(self):
        return reverse('fooddetail',kwargs={"id":self.id})

    def __str__(self):
        return self.title

class Chef(models.Model):
    name = models.CharField(max_length=150,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    photo = models.ImageField(upload_to="chef/chef",blank=True)
    
    
    class Meta:
        verbose_name='chef'
        verbose_name_plural='chefs'

    def get_url(self):
        return reverse('chefdetail',kwargs={"id":self.id})

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    content = models.TextField(max_length=1000000,blank=True)
    photo = models.ImageField(upload_to="blog/meal",blank=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    
    
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'

    def get_url(self):
        return reverse('blogdetail',kwargs={"category_slug":self.slug}) 


    def __str__(self):
        return self.title

class About(models.Model):
    title= models.CharField(max_length=150,blank=True)
    desc = models.CharField(max_length=250,blank=True)
    photo = models.ImageField(upload_to="about/about",blank=True)
    
    class Meta:
        verbose_name='about'
        verbose_name_plural='aboutinfos'

    

    def __str__(self):
        return self.title

class Contact(models.Model):
    number = models.IntegerField(blank=True)
    mail = models.CharField(max_length=150,blank=True)
    adress=models.CharField(max_length=550,blank=True)
    

    class Meta:
        verbose_name='contact'
        verbose_name_plural='contacts'

    

    def __str__(self):
        return self.adress

class Appointment(models.Model):
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    quantity= models.IntegerField(blank=True)
    email = models.CharField(max_length=50, blank=True)
    message=models.TextField(max_length=10000000, blank=True)
    sent_date = models.DateField(auto_now_add=True, blank=True)
    desire_date=models.DateField(blank=True)
    desire_time = models.TimeField(blank=True)
    accepted = models.CharField(max_length=50, blank=True, default="iswaiting")

    

    class Meta:
        verbose_name='Appointment'
        verbose_name_plural='Appointments'
        ordering = ["-sent_date"]

    def get_url(self):
        return reverse('appointmentsdetail',kwargs={"id":self.id})

    

    def __str__(self):
        return self.first_name



def pre_save_blog(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)

pre_save.connect(pre_save_blog,sender=Blog)

