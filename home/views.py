from django.shortcuts import render


from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,JsonResponse
import work.settings as settings
from django.template import loader
from home.models import Contact, Subscribe, Strories
from home.forms import ContactForm, ContactForm2, SubscribeForm 
import os

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(requset):
    form = ContactForm2()
    if requset.method == 'POST':
        # name = requset.POST.get('name')
        # email = requset.POST.get('email')
        # subject = requset.POST.get('subject')
        # message = requset.POST.get('message')

        form = ContactForm2(requset.POST)
        if form.is_valid():
            form.save()
            form = ContactForm2()
            #  Contact.objects.create(name = form.cleaned_data['name'], email = form.cleaned_data['email'], subject = form.cleaned_data['subject'], message = form.cleaned_data['message'])

    context = {
        'forms': form,
        'aboutme':{'address':'xetai rayonu qum adasi', 'phone':'+994558910805','email':'hesenzadeh663@gmail.com','site':'http://127.0.0.1:8000/'}
    }
    return render(requset,'contact.html', context=context)

def recipes(request):
    return render(request,'recipes.html')

def create_story(request):
    return render(request,'create_story.html')

def emailsubscribers(request):
    return render(request,'email-subscribers.html')
 
def strories(request, slug = None):
    stories = Strories.objects.all() #select * from home_stories
    if slug:
        stories = stories.filter(category__slug = slug)
    context = {
        'stories':stories
    }
    return render(request,'strories.html', context)

def single(request, slug = None):
    if not slug:
        slug = 1
    story = Strories.objects.get(slug = slug)
    context = {
        'story':story
    }
    return render(request,'single.html', context)
   
def subscribe(request):
    if request.method =='POST':
        # email = request.POST.get('email')
        # Subscribe.objects.create( email = email)
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                JsonResponse.status_code = 201 
                return JsonResponse({'Messages': 'Ugurlu'})
            except:
                return JsonResponse({'Messages': 'Ugurlu'})
        
        # JsonResponse.status_code = 404
        return JsonResponse({'Messages':form.errors})
            
def comment(request):
    pass

