from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [ 
	path('',views.counter, name='counter'), 
    path('counter',views.counter, name='counter'), 
]
