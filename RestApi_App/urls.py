

from django.urls import path
from RestApi_App import views

urlpatterns = [
      path('',views.home,name=''),
      path('home',views.Home.as_view(),name='home'),
]
        