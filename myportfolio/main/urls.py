from django.urls import path
from .views import base, home, biography, photos, portfolio, socials
from . import views 


urlpatterns = [
    path('', home, name='home'),
    path('biography/', biography, name='biography'),
    path('photos/', photos, name='photos'),
    path('portfolio/', portfolio, name='portfolio'),
    path('socials/', socials, name='socials'),
    path('home/', home, name='home'),
    path('photos/', photos, name='photos'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]
