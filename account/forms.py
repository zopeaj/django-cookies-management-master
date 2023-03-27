from django import forms
from account.models import Account

class AccountForm(forms.Form):
    age = forms.IntegerField(default=None)
    image_field = forms.ImageField(widget=forms.FileInput)
    first_name = forms.CharField(widget=forms.TextInput, label='first_name', max_length=20, error_messages={'required': "Please, provide a name", "max_length": "This value exceeds it maximum length"})
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = Account


class AccountFormModel(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)
