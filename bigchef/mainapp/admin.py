from django.contrib import admin

# Register your models here.
from .models import About, HomeSlider,Contact, Blog,Chef,Meal,Appointment
from accounts.models import Comment
admin.site.register(About)
admin.site.register(HomeSlider)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Chef)
admin.site.register(Meal)
admin.site.register(Appointment)
admin.site.register(Comment)


