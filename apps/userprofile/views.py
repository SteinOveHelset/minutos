#
#

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


#
# Import models

from .models import Userprofile
from apps.team.models import Team, Invitation
from apps.team.utilities import send_invitation_accepted


#
# Views

@login_required
def myaccount(request):
    teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    invitations = Invitation.objects.filter(email=request.user.email, status=Invitation.INVITED)

    return render(request, 'userprofile/myaccount.html', {'teams': teams, 'invitations': invitations})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        if request.FILES:
            avatar = request.FILES['avatar']
            userprofile = request.user.userprofile
            userprofile.avatar = avatar
            userprofile.save()

        messages.info(request, 'The changes was saved')

        return redirect('myaccount')
    
    return render(request, 'userprofile/edit_profile.html')

@login_required
def accept_invitation(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        invitations = Invitation.objects.filter(code=code, email=request.user.email)

        if invitations:
            invitation = invitations[0]
            invitation.status = Invitation.ACCEPTED
            invitation.save()

            team = invitation.team
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            messages.info(request, 'Invitation accepted')

            send_invitation_accepted(team, invitation)

            return redirect('team:team', team_id=team.id)
        else:
            messages.info(request, 'Invitation was not found')
    else:
        return render(request, 'userprofile/accept_invitation.html')