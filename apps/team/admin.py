#
#

from django.contrib import admin

#
#

from .models import Team, Invitation

#
#

admin.site.register(Team)
admin.site.register(Invitation)