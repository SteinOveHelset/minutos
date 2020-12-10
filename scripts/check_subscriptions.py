# Import Python packages

import django
import os
import sys
import stripe

# Init Django

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minutos.settingsprod")
django.setup()

from django.conf import settings

# Import models

from apps.team.models import Team, Plan

# Init Stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Loop through teams

for team in Team.objects.all():
    sub = stripe.Subscription.retrieve(team.stripe_subscription_id)

    if sub.status == 'canceled':
        plan_default = Plan.objects.get(is_default=True)

        team.plan = plan_default
        team.plan_status = Team.PLAN_CANCELED
        team.save()