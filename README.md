

# Travel Booking System

A web-based travel booking system built with Django that allows users to book various travel options like flights, trains, and buses. It includes user registration, login, travel option search and filtering, booking management, and administrative management through the Django admin interface.

## Features

- **User Authentication**: Register, login, and manage user profiles.
- **Travel Option Management**: Book and manage travel options like flights, trains, and buses.
- **Booking Management**: Users can view, cancel, and manage their bookings.
- **Admin Dashboard**: Admin can add, edit, and delete travel options and manage bookings via the Django admin interface.
- **Search and Filtering**: Users can search and filter travel options based on type, date, source, and destination.
- **Responsive UI**: Built using Bootstrap 5 for a responsive and modern user interface.

## Technologies Used

- **Backend**: Django 5.1.1 (Python 3.11)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default, can be switched to other databases like PostgreSQL or MySQL)
- **Version Control**: Git and GitHub
- **Authentication**: Django’s built-in authentication system

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kathojumanoj/Travel-Booking.git
cd travel_booking
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install the Requirements

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Migrate the Database

Run the migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin user.

### 6. Collect Static Files

If you’re running the project in a production environment, collect the static files:

```bash
python manage.py collectstatic
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

### User Registration and Login

1. Go to `/register/` to create a new user account.
2. Log in with your credentials at `/login/`.

### Travel Options

- Browse available travel options like flights, trains, and buses.
- Search and filter by type, source, destination, or date.

### Booking

- Click on "Book" to reserve seats for a travel option.
- View all your bookings at `/my-bookings/`.
- Cancel bookings if needed.

### Admin Interface

Access the admin interface at `/admin/` and log in with the superuser account. Admin can manage:

- **Users**: Add, edit, and remove users.
- **Travel Options**: Manage travel options (flights, trains, buses).
- **Bookings**: View and manage user bookings.

## Project Structure

```
travel_booking/
│
├── manage.py               # Django management script
├── travel_booking/
│   ├── __init__.py
│   ├── settings.py          # Django settings file
│   ├── urls.py              # Project URL configurations
│   ├── wsgi.py              # WSGI configuration
│
├── users/                   # Main app for user and booking management
│   ├── migrations/
│   ├── static/              # Static files (CSS, JS, images)
│   ├── templates/           # HTML templates
│   ├── admin.py             # Django admin configurations
│   ├── models.py            # Database models
│   ├── forms.py             # Forms for user and booking management
│   ├── views.py             # Views for handling HTTP requests
│   ├── urls.py              # URLs for the 'users' app
│   └── ...
├── requirements.txt         # Python dependencies
```

## Testing

To run the unit tests for the project:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit pull requests, report bugs, or suggest new features. Contributions are welcome!

## Contact

For any questions, issues, or contributions, please contact [Kathoju Manoj] at [kathojumanoj48@gmail.com].

---
