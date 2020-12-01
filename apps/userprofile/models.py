#
#

from django.contrib.auth.models import User
from django.db import models


#
# Models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='uploads/avatars/', blank=True, null=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/static/images/avatar.png'