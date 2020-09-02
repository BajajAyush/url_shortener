from django import forms


too_long_error = "Your custom name is too long. Are you sure you wanted a shortening service? :)"


class LinkSubmitForm(forms.Form):
    url = forms.URLField(label='URL to be shortened',widget=forms.TextInput(attrs={'placeholder': 'url'}))
    short = forms.CharField(label='Custom shortened extension',widget=forms.TextInput(attrs={'placeholder': 'extension'}))
