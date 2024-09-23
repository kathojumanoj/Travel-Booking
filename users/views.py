# users/views.py
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, UserUpdateForm

from django.contrib import messages
from .models import TravelOption, Booking
from .forms import BookingForm




# Home view (optional, for redirect after login)
def home(request):
    return render(request, 'home.html')

# Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login view (using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

# Logout view (using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'

# Profile update view (requires login)
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after updating
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})




# List of travel options
def travel_options_list(request):
    travel_options = TravelOption.objects.all()
    return render(request, 'users/travel_options_list.html', {'travel_options': travel_options})

# Detail view for a specific travel option
def travel_option_detail(request, travel_id):
    travel_option = get_object_or_404(TravelOption, travel_id=travel_id)
    return render(request, 'users/travel_option_detail.html', {'travel_option': travel_option})





# users/views.py
from django.utils import timezone

@login_required
def my_bookings(request):
    # Fetch all bookings for the current user
    bookings = Booking.objects.filter(user=request.user)

    # Separate bookings into upcoming and past based on travel date
    upcoming_bookings = bookings.filter(travel_option__date_time__gte=timezone.now(), status='confirmed')
    past_bookings = bookings.filter(travel_option__date_time__lt=timezone.now(), status='confirmed')

    return render(request, 'users/my_bookings.html', {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
    })

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.status = 'canceled'
        booking.save()

        # Add the number of seats back to the available seats for the travel option
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()

        messages.success(request, 'Your booking has been canceled.')
        return redirect('my_bookings')

    return render(request, 'users/cancel_booking.html', {'booking': booking})



# users/views.py
@login_required
def book_travel_option(request, travel_id):
    # Fetch the travel option based on the ID passed in the URL
    travel_option = get_object_or_404(TravelOption, travel_id=travel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, travel_option=travel_option)  # Pass travel_option to the form
        if form.is_valid():
            # Create a new booking instance but don't save it to the database yet
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the current logged-in user
            booking.travel_option = travel_option  # Assign the selected travel option
            booking.total_price = booking.calculate_total_price()  # Calculate the total price
            booking.save()  # Now save the booking object to the database

            # Update the available seats for the selected travel option
            travel_option.available_seats -= booking.number_of_seats
            travel_option.save()

            messages.success(request, 'Booking confirmed successfully!')
            return redirect('my_bookings')  # Redirect to the user's bookings page
    else:
        form = BookingForm(travel_option=travel_option)  # Pass travel_option to the form

    # Render the booking form
    return render(request, 'users/book_travel_option.html', {'form': form, 'travel_option': travel_option})

# users/views.py
from django.db.models import Q
from .forms import TravelOptionSearchForm
from .models import TravelOption

def travel_options_list(request):
    travel_options = TravelOption.objects.all()  # Start with all travel options
    form = TravelOptionSearchForm(request.GET or None)  # Pass GET data to the form

    if form.is_valid():
        # Apply filters based on the form input
        travel_type = form.cleaned_data.get('travel_type')
        source = form.cleaned_data.get('source')
        destination = form.cleaned_data.get('destination')
        date = form.cleaned_data.get('date')

        # Filter by travel type
        if travel_type:
            travel_options = travel_options.filter(travel_type=travel_type)

        # Filter by source
        if source:
            travel_options = travel_options.filter(source__icontains=source)

        # Filter by destination
        if destination:
            travel_options = travel_options.filter(destination__icontains=destination)

        # Filter by date
        if date:
            travel_options = travel_options.filter(date_time__date=date)

    return render(request, 'users/travel_options_list.html', {
        'form': form,
        'travel_options': travel_options,
    })
