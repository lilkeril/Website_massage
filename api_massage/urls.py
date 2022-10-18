from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'service', views.ServiceViewSet)
router.register(r'records', views.RecordsViewSet)



urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('user/<int:pk>/', views.UserRetrieveUpdateDelete.as_view()),
    path('', include(router.urls)),
]
