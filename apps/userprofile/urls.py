#
#

from django.urls import path


#
#

from .views import myaccount, edit_profile

#
#

urlpatterns = [
    path('', myaccount, name='myaccount'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]