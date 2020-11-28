# Import Python

from datetime import datetime

# Models 

from apps.project.models import Entry

# Utility functions

def get_time_for_user_and_date(team, user, date):
    entries = Entry.objects.filter(team=team, created_by=user, created_at__date=date, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_team_and_month(team, month):
    entries = Entry.objects.filter(team=team, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_month(team, user, month):
    entries = Entry.objects.filter(team=team, created_by=user, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_project_and_month(team, project, user, month):
    entries = Entry.objects.filter(team=team, project=project, created_by=user, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)

def get_time_for_user_and_team_month(team, user, month):
    entries = Entry.objects.filter(team=team, created_by=user, created_at__year=month.year, created_at__month=month.month, is_tracked=True)

    return sum(entry.minutes for entry in entries)