# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject=f"[Blog] - {subject}",
                    message=f"Message de la part de {name} - {from_email}: \n {message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL]
                )
                messages.success(request, 'Votre message a bien été envoyé.')
            except BadHeaderError:
                messages.error(request, "Le formulaire est incomplet, le message n'est pas parti.")
            return redirect('contact:email')
    return render(request, "contact.html", {'form': form})
