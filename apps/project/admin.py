#
# Import Django

from django.contrib import admin


#
# Import models

from .models import Project, Task


#
# Register

admin.site.register(Project)
admin.site.register(Task)