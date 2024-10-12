from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
     path('signup/', views.sign_up, name='signup'),
     path('login/', views.login_page, name='login'),
     path('logout/', views.logout_user, name='logout'),
     path('profile/', views.profile, name='profile')
]
