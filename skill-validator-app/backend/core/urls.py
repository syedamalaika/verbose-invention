from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('skills/', views.skill_select, name='skill_select'),
    path('test/<int:skill_id>/', views.take_test, name='take_test'),
    path('submit-test/<int:skill_id>/', views.submit_test, name='submit_test'),
    path('result/<int:skill_id>/', views.result_page, name='result_page'),
]
