

# users/urls.py
from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, update_profile, home
from .views import travel_options_list, travel_option_detail, book_travel_option, my_bookings

from .views import my_bookings, cancel_booking

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('register/', register, name='register'),  # Registration view
    path('login/', CustomLoginView.as_view(), name='login'),  # Login view
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout view
    path('profile/', update_profile, name='profile'),  # Profile update view

    path('travel-options/', travel_options_list, name='travel_options_list'),  # List view
    path('travel-option/<int:travel_id>/', travel_option_detail, name='travel_option_detail'),  # Detail view

    path('book/<int:travel_id>/', book_travel_option, name='book_travel_option'),  # URL for booking
    path('my-bookings/', my_bookings, name='my_bookings'), # URL for viewing user's bookings

    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', cancel_booking, name='cancel_booking')
]

