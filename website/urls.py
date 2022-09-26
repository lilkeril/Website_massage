from django.urls import path
from . import views

urlpatterns = [
    # path('', views.massage, name='home'),
    path('massage', views.massage, name='massage'),
    path('eyelashes', views.eyelashes, name='eyelashes'),
    path('registration', views.registration, name='registration')
]