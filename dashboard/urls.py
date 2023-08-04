from . import views
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


urlpatterns = [
path('',views.index, name="index"),  
 path('user_profile/',views.user_profile, name='user_profile'),
# path('login/' , views.render_login, name="login"),
# path("logout/", LogoutView.as_view(), name="logout"),
# path('register/', views.render_register, name='register'),

]
