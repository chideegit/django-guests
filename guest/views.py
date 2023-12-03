import csv
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import * 
from .models import * 

@login_required
def add_guest(request):
    if request.method == 'POST':
        form = AddGuestForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.author = request.user 
            var.save()
            messages.success(request, 'New Guest info is now added and saved in Database')
            return redirect('signed-in-guests')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors')
            return redirect('add-guest')
    else:
        form = AddGuestForm()
        context = {'form':form}
    return render(request, 'guest/add_guest.html', context)

@login_required
def update_guest(request,pk):
    guest = Guest.objects.get(pk=pk)
    if guest.has_signed_out:
        messages.warning(request, 'Cannot change guest properties. Please reach out to an Admin')
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UpdateGuestForm(request.POST, instance=guest)
            if form.is_valid():
                form.save()
                messages.success(request, 'Guest information has been updated and saved')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong. Please check form errors')
                #return redirect('update-guest')
        else:
            form = UpdateGuestForm(instance=guest)
            context = {'form':form}
        return render(request, 'guest/update_guest.html', context)

@login_required
def signed_in_guests(request):
    guests = Guest.objects.filter(has_signed_out=False).order_by('-time_in')
    context = {'guests':guests}
    return render(request, 'guest/signed_in_guests.html', context)

@login_required
def signed_out_guests(request):
    guests = Guest.objects.filter(has_signed_out=True).order_by('-time_out')
    context = {'guests':guests}
    return render(request, 'guest/signed_out_guests.html', context)

@login_required
def guest_sign_out(request, pk):
    guest = Guest.objects.get(pk=pk)
    guest.has_signed_out = True
    guest.time_out = datetime.datetime.now()
    guest.save()
    messages.success(request, 'Guest has been signed out and all info updated!')
    return redirect('dashboard')

@login_required
def export_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="guest_list.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["First Name", "Surname", "Email", "Phone", "Address", "To See", "Time In", "Time Out", "Signed Out?"])
    for guest in Guest.objects.all():
        writer.writerow([guest.first_name, guest.surname, guest.email_id, 
                         guest.phone_number, guest.address, guest.to_see, guest.time_in, guest.time_out, guest.has_signed_out])
    return response
    # https://docs.djangoproject.com/en/4.2/howto/outputting-csv/