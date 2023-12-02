from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def email_function(request):
    subject = "test subject"
    message = "<h1>hello world</h1>"
    from_email = "from-user@gmail.com"
    to_email = "to-user@gmail.com"
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [to_email,])
        except :
            print("Error sending mail")