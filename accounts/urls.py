from .views import RegisterAPI,LoginAPI
from django.urls import path
from knox import views as knox_views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
