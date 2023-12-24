from django.urls import path
from .views import HomeView, SkatingView, AboutView, ShopView, ContactusView

app_name = 'sbs'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('skating/', SkatingView.as_view(), name="skating_page"),
    path('shop/', ShopView.as_view(), name="shop_page"),
    path('contact-us/', ContactusView.as_view(), name='contact_page'),
]