from django.urls import path
from .views import GenerateRandomUserView, HomePageView

urlpatterns = [
    path('generate/', GenerateRandomUserView.as_view(), name='generate'), 
    path('', HomePageView.as_view(), name='users_list'),


]