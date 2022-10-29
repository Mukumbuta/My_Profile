from django.urls import path
from myprofile import views


urlpatterns = [
    path('details/', views.profile_details),
]