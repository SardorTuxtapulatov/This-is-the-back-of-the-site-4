from django.shortcuts import render
from django.views.generic import TemplateView

def home_page(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'
class AboutView(TemplateView):
    template_name = 'about.html'
class SkatingView(TemplateView):
    template_name = 'skating.html'
class ShopView(TemplateView):
    template_name = 'shop.html'
class ContactusView(TemplateView):
    template_name = 'contact.html'

















