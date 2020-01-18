from django.urls import path
from Neighbour import views

app_name= 'Neighbour'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
