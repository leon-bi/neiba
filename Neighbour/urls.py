from django.urls import path
from Neighbour import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'Neighbour'

urlpatterns = [
    path('',views.home,name='home'), 
    # path('police',views.home,name=''),
    # path('health',views.home,name=''),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)