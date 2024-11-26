from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from .models import Contact


def contact(request):
    contacts = Contact.objects.order_by('favorite', 'name')
    return render(request, 'phbapp/contacts.html', {'contacts': contacts})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    return render(request, 'phbapp/contact_create.html', {'form': form})


def delete_contact(request, contact_id):

    contacts = Contact.objects.get(id=contact_id)
    contacts.delete()

    return redirect('/')


def update_favorite(request, contact_id):

    contacts = Contact.objects.get(id=contact_id)

    if contacts.favorite == False:

        contacts.favorite = True
        contacts.save()
    else:
        contacts.favorite = False
        contacts.save()
    return redirect('/')
