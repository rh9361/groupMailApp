from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.HomePage.as_view(),name='homepage'),
    
    path(r'^index/$',views.index,name='index'),

]
