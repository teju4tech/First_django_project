from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from Home.models import Contact
# Create your views here.
def Home(request):
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('Jai Mahakal')
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse('Bajrang')
    # Handle the form here
    if request.method == 'POST':
        name = request.POST['name']
        phone= request.POST['phone']
        email= request.POST['email']
        desc= request.POST['password']
        c = Contact(name=name, phone=phone, email=email, desc=desc)
        c.save()
    return render(request, 'contact.html')