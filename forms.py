from django import forms
from .models import ContactModel
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.ModelForm):
	name = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Enter your name'}))
	email = forms.CharField(label=_("Email"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'example@gmail.xom'}))
	comments = forms.CharField(max_length=254,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Enter yor comment here......'}))
	class Meta:
	  	model = ContactModel
	  	fields = ('name','email', 'comments')
