from django import forms


class add_user_form(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email1 = forms.EmailField(label='Email1', max_length=100)
    email2 = forms.EmailField(label='Email2', max_length=100, required=False)
    phone1 = forms.CharField(label='Phone1', max_length=12)
    phone2 = forms.CharField(label='Phone2', max_length=12, required=False)

class remove_user_form(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs={'id': 'tags'}))
