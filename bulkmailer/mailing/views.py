import csv
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import UploadCSVForm

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            for row in reader:
                email = row['email']  # Assuming your CSV has an 'email' column
                from_email = 'gtec.dev@education.com'
                recipient_list = [email]
                
                try:
                    personalized_message = message.format(**row) if '{name}' in message else message
                    send_mail(subject, personalized_message, from_email, recipient_list)
                except Exception as e:
                    # Handle exceptions, perhaps log them or return an error message
                    print(f"Failed to send email to {email}: {str(e)}")
            
            return HttpResponse('Emails sent successfully.')
    else:
        form = UploadCSVForm()
    return render(request, 'mailing/upload_csv.html', {'form': form})