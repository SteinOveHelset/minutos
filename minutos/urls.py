"""minutos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from apps.core.views import frontpage, privacy, terms, plans, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('plans/', plans, name='plans'),
    path('admin/', admin.site.urls),

    #
    # Auth

    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', include('apps.userprofile.urls')),
    path('myaccount/teams/', include('apps.team.urls')),
]
