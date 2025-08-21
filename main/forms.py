from django import forms
from .models import ContactMessage,PortfoiloItem

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','message']


class PortfoiloForm(forms.ModelForm):
    class Meta:
        model = PortfoiloItem
        fields = ['title', 'description', 'image','link']
