import logging

from django import forms
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="E-mail", blank=True)
    message = forms.CharField(label="Message", widget=forms.Textarea, max_length=600)

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = (
            f"From: {self.cleaned_data['name']}\nEmail: {self.cleaned_data['email']}\n{self.cleaned_data['message']}"
        )
        send_mail(
            "Site message",
            message,
            "site@bookstore.domain",
            ["customerservice@bookstore.domain"],
            fail_silently=False,
        )
