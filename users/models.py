from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# users/models.py
# from django.db import models
from django.contrib.auth import get_user_model
# from .models import TravelOption

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
    
# users/models.py
# from django.db import models

class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ('flight', 'Flight'),
        ('train', 'Train'),
        ('bus', 'Bus'),
    ]

    travel_id = models.AutoField(primary_key=True)  # Auto-generated travel ID
    travel_type = models.CharField(max_length=10, choices=TRAVEL_TYPES)  # Flight/Train/Bus
    source = models.CharField(max_length=100)  # Starting point
    destination = models.CharField(max_length=100)  # Destination
    date_time = models.DateTimeField()  # Travel date and time
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    available_seats = models.PositiveIntegerField()  # Available seats

    def __str__(self):
        return f"{self.get_travel_type_display()} from {self.source} to {self.destination}"
    
User = get_user_model()

class Booking(models.Model):
    BOOKING_STATUS = [
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the booking
    travel_option = models.ForeignKey('TravelOption', on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=BOOKING_STATUS, default='confirmed')

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username}"

    # Helper method to determine if the booking is for a past travel option
    def is_past(self):
        return self.travel_option.date_time < timezone.now()
       # Method to calculate total price based on the number of seats
    def calculate_total_price(self):
        return self.travel_option.price * self.number_of_seats





