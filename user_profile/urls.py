from django.urls import path, include
from . import views
from .views import Login

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('register/', views.register, name = "register"),
    path('login/', Login.as_view(), name = "login"),
]