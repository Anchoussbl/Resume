from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my_site-home'),
    path('skills/', views.skills, name='my_site-skills'),
    path('education/', views.education, name='my_site-education'),
    path('experience/', views.experience, name='my_site-experience'),
    path('base/', views.base, name='my_site-base')
]
