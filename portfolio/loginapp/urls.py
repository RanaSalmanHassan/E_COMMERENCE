app_name = 'loginapp'
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('user_profile',views.user_profile,name='user_profile'),
]

