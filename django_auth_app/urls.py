from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [

    path('admin/', admin.site.urls),

    ##### user related path##########################
    path('', include('user.urls')),
    path('verification/', include('verify_email.urls')),

    path('accounts/login/', user_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', user_view.register, name='register'),

]
