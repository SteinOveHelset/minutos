# Import Django

from django.urls import path

# 

from .views import team, add, edit, activate_team

#

app_name = 'team'

#

urlpatterns = [
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('<int:team_id>/', team, name='team')
]