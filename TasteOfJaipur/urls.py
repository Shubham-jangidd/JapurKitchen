from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from TasteOfJaipur import views
urlpatterns = [
    path('', views.Home.as_view(), name="homepage"),
    path('login/', auth_views.LoginView.as_view(template_name="app/login.html", authentication_form=LoginForm), name="login"),
    path('about/', views.about.as_view(), name="about"),
    # path('contact/', views.contactus.as_view(), name="contact"),
    # path('login/', views.login.as_view(), name="login"),
    # path("", views.homepage, name="homepage"),
    path("contact/", views.contactus, name="contact"),
    path('saveenquiry/', views.saveEnquiry, name="saveenquiry"),
    path('logout/', auth_views.LogoutView.as_view(next_page="homepage"), name="logout"),
    path('Signup/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    


]
