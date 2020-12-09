# Import Django

from django.contrib.auth.models import User
from django.db import models

# Models

class Plan(models.Model):
    title = models.CharField(max_length=255)
    max_projects_per_team = models.IntegerField(default=0)
    max_members_per_team = models.IntegerField(default=0)
    max_tasks_per_project = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

class Team(models.Model):
    #
    # Status

    ACTIVE = 'active'
    DELETED = 'deleted'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )

    #
    # Plan status

    PLAN_ACTIVE = 'active'
    PLAN_CANCELED = 'canceled'

    CHOICES_PLAN_STATUS = (
        (PLAN_ACTIVE, 'Active'),
        (PLAN_CANCELED, 'Canceled')
    )

    #
    # Fields

    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    plan_status = models.CharField(max_length=20, choices=CHOICES_PLAN_STATUS, default=PLAN_ACTIVE)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Invitation(models.Model):
    #
    # Status

    INVITED = 'invited'
    ACCEPTED = 'accepted'

    CHOICES_STATUS = (
        (INVITED, 'Invited'),
        (ACCEPTED, 'Accepted')
    )

    team = models.ForeignKey(Team, related_name='invitations', on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=INVITED)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email