import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from guest.models import Guest

@login_required
def dashboard(request):
    guests = Guest.objects.all()
    sig = Guest.objects.filter(has_signed_out=False) # sig -> signed in guests
    context = {
        'guests':guests,
        'sig':sig
    }
    return render(request, 'dashboard/dashboard.html', context)
