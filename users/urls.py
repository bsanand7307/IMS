from django.urls import path

from .views import login_page, logout_page
from . import views
urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/',views.register, name='register'),

]
