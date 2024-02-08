from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'),
]