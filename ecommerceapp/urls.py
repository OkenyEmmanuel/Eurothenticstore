from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.contact,name="about"),
    path('checkout/', views.checkout, name="Checkout"),
]
