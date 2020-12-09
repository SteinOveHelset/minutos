#
#

from django.contrib import admin

#
#

from .models import Team, Invitation, Plan

#
#

admin.site.register(Team)
admin.site.register(Invitation)
admin.site.register(Plan)