from django.contrib import admin
from .models import TravelOption, Booking

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_type', 'source', 'destination', 'date_time', 'price', 'available_seats')
    list_filter = ('travel_type', 'source', 'destination')
    search_fields = ('source', 'destination')




# users/admin.py
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'booking_date', 'status')
    list_filter = ('status', 'travel_option__travel_type')

