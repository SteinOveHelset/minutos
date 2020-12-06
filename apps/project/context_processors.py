# Import Python

from datetime import datetime, timezone

# Import Django

from django.shortcuts import get_object_or_404

# Import Models

from apps.project.models import Entry
from apps.team.models import Team

# Context processors

def active_entry(request):
    if request.user.is_authenticated:
        if request.user.userprofile.active_team_id:
            team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
            untracked_entries = Entry.objects.filter(team=team, created_by=request.user, minutes=0, is_tracked=False)

            if untracked_entries:
                active_entry = untracked_entries.first()
                active_entry.seconds_since = int((datetime.now(timezone.utc) - active_entry.created_at).total_seconds())

                return {'active_entry_seconds': active_entry.seconds_since, 'start_time': active_entry.created_at.isoformat()}
    
    return {'active_entry_seconds': 0, 'start_time': datetime.now().isoformat()}