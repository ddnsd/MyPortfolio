from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project
from .models import Photo
from .models import SocialLink

# Create your views here.
def base(request):
    return render(request, 'base.html')

def biography(request):
    return render(request, 'biography.html')

def photos(request):
    return render(request, 'photos.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def socials(request):
    social_links = SocialLink.objects.all()
    return render(request, 'socials.html', {'social_links': social_links})

def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can add email sending logic here)
            # For now, let's just redirect to the home page after form submission
            return redirect('home')

    return render(request, 'home.html', {'form': form})

def photos(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos': photos})

def toggle_theme(request):
    current_theme = request.session.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    request.session['theme'] = new_theme
    return redirect(request.META.get('HTTP_REFERER', '/'))