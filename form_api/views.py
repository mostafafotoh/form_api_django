from django.shortcuts import render
from .forms import Contact

def contact_form (request):
    contact = Contact(request.POST or None)
    context = {
        'contact' : contact ,
    }
    return render(request,'contact.html',context)