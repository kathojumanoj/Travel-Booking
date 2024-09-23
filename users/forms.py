# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser ,TravelOption, Booking

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
# users/forms.py (continued)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']

# users/forms.py


class TravelOptionForm(forms.ModelForm):
    class Meta:
        model = TravelOption
        fields = ['travel_type', 'source', 'destination', 'date_time', 'price', 'available_seats']




# users/forms.py
# from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Get travel_option from kwargs and remove it from kwargs so we can pass the remaining to the parent class
        self.travel_option = kwargs.pop('travel_option', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Booking
        fields = ['number_of_seats']  # Only ask the user for the number of seats

    # Custom validation for seat availability
    def clean_number_of_seats(self):
        number_of_seats = self.cleaned_data['number_of_seats']

        # Use the travel_option passed in __init__ instead of self.instance.travel_option
        if self.travel_option and number_of_seats > self.travel_option.available_seats:
            raise forms.ValidationError(f"Only {self.travel_option.available_seats} seats are available.")
        return number_of_seats

class TravelOptionSearchForm(forms.Form):
    TRAVEL_TYPES = [
        ('', 'All'),  # Allow 'All' as an option
        ('flight', 'Flight'),
        ('train', 'Train'),
        ('bus', 'Bus'),
    ]

    # Search fields
    travel_type = forms.ChoiceField(choices=TRAVEL_TYPES, required=False, label="Travel Type")
    source = forms.CharField(max_length=100, required=False, label="Source")
    destination = forms.CharField(max_length=100, required=False, label="Destination")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label="Travel Date")
    


