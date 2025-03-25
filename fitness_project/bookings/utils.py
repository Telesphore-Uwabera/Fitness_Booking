from django.core.mail import send_mail

def send_booking_confirmation(user_email, class_name, schedule):
    subject = f'Booking Confirmation for {class_name}'
    message = f'You have successfully booked a class scheduled on {schedule}.'
    send_mail(subject, message, 'no-reply@fitness.com', [user_email])
