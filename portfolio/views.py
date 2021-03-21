from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# manages the homepage
def index(request):
    if request.method == 'POST':
        # email variables
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message_text = request.POST['message']

        # send email
        send_mail(str(message_name) + ' - ' + str(message_subject), message_text, message_email, ['emmanueligbinijesu@gmail.com'], fail_silently=True)

        # display message sent message
        messages.success(request, ('Thanks for getting in touch!'))
        return render(request, 'index.html', {'message_name' : message_name, 'message_text' : message_text, 'message_email' : message_email})
    else:
        return render(request, 'index.html', {})
