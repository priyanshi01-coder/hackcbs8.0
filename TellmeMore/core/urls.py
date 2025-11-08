from django.urls import path , include
from . import views


urlpatterns = [

    path("",views.home_view , name="home"),
    path("about/",views.about_view , name="about"),
    path("how_to/",views.how_to_view , name="how_to"),
    path('contact_us/',views.contact_view , name='contact_us'),

]