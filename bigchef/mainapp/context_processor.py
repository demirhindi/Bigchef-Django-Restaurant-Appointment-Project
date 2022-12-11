from .models import Contact

def menu_links2(request):
    links2 = Contact.objects.all()
    return dict(links2=links2)
