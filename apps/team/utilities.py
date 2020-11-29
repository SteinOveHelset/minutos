# Import Django

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

#

def send_invitation(to_email, code, team):
    from_email = settings.DEFAULT_EMAIL_FROM
    acceptation_url = settings.ACCEPTATION_URL

    subject = 'Invitation to Minutos'
    text_content = 'Invitation to Minutos. Your code is: %s' % code
    html_content = render_to_string('team/email_invitation.html', {'code': code, 'team': team, 'acceptation_url': acceptation_url})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def send_invitation_accepted(team, invitation):
    from_email = settings.DEFAULT_EMAIL_FROM
    subject = 'Invitation accepted'
    text_content = 'Your invitation was accepted'
    html_content = render_to_string('team/email_accepted_invitation.html', {'team': team, 'invitation': invitation})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [team.created_by.email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()