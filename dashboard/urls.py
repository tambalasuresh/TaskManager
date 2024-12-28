from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),  # Ensure this line has the name 'Homepage'
    path('login/', views.login_view, name='login'),
    path('register/', views.Registrationpage, name='Registration'),
    path('logout/', views.logout_view, name='logout'),
]
