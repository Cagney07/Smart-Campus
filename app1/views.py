from django.shortcuts import render, redirect
from django.http import HttpResponse
from twilio.rest import Client
from .forms import *

from django.shortcuts import render
import subprocess  # Used to run external scripts

import cv2
import pickle

from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def home(request):
    return render(request, 'web.html')

def find_donors_view(request):
    # You can add any logic or data retrieval specific to this page here
    return render(request, 'find_donors.html')


def donate_blood(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('donate_blood_success')
    else:
        form = DonorForm()
    return render(request, 'donate_blood.html', {'form': form})

@login_required
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save()  # Save the form data to the database
            # Send an SMS using Twilio
            send_twilio_message(blood_request)
            return redirect('request_blood_success')
    else:
        form = BloodRequestForm()
    return render(request, 'request_blood.html', {'form': form})
    pass

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('request_blood')

import os
import smtplib
from email.message import EmailMessage
from twilio.rest import Client  # Import Twilio client

def send_twilio_message(blood_request):
    # Twilio credentials and phone numbers
    twilio_account_sid = "AC59b75df210b05be3ce66c789d301028b"
    twilio_auth_token = "c7cdfb0f4b626f19fbf46e2a5f368029"
    twilio_number = "+12516169015"
    target_number = "+919390031859"

    # Create a Twilio client
    client = Client(twilio_account_sid, twilio_auth_token)

    # Compose the SMS message
    sms_message = f"Alert: Blood request - Patient Name: {blood_request.patient_name}, Blood Group: {blood_request.blood_group}, Location: {blood_request.location}, Age: {blood_request.age}, Condition: {blood_request.patient_condition}"

    # Send the SMS
    sms = client.messages.create(
        body=sms_message,
        from_=twilio_number,
        to=target_number
    )

    # Print a success message (you can log this as needed)
    print(f"SMS sent successfully with SID: {sms.sid}")

    # # Send an email
    # email_id = 'ab4032@srmist.edu.in'
    # email_pass = 'Sathya*06'
    # recipient_list = ['pp2549@srmist.edu.in']

    # email_message = EmailMessage()
    # email_message['Subject'] = 'Blood Request'
    # email_message['From'] = email_id
    # email_message['To'] = recipient_list
    # email_message.set_content(sms_message)

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(email_id, email_pass)
    #     smtp.send_message(email_message)

# Usage:
# Call send_twilio_message(blood_request) where blood_request is an instance of your BloodRequest model.

def donate_blood_success(request):
    return render(request, 'donate_blood_success.html')

def request_blood_success(request):
    return render(request, 'request_blood_success.html')

def parking_videos(request):
    return render(request, 'parking_videos.html')
    # # You can add any logic or data retrieval specific to the parking page here
    # return render(request, 'parking.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # The template for the login page
    success_url = '/request_blood/'  # The URL to redirect to upon successful login

def parking(request):
    # Add your view logic here
    return render(request, 'parking.html')
def logout_view(request):
    logout(request)
    return redirect('find_donors')  # Redirect to the page after logging out, e.g., 'find_donors'
# class CustomLoginView(LoginView):
#     template_name = 'login.html'  # The template for the login page
#     success_url = '/request_blood/'  # The URL to redirect to upon successful login

# # def run_parking_script(request):
#     try:
#         # Run the ParkingSpacePicker.py script using subprocess
#         subprocess.run(["python", "ParkingSpacePicker.py"])
#         return render(request, 'parking.html')  # Redirect to a new page after script execution
#     except Exception as e:
#         return render(request, 'error.html', {'error_message': str(e)})



