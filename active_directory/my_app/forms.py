from django import forms


class add_user_form(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)


class remove_user_form(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs={'id': 'tags'}))
