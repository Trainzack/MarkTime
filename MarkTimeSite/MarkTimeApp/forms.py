from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    name_placeholder = "What is your name?"

    contacter_email = forms.EmailField(required=True)
    contacter_email_placeholder = "How do we contact you?"

    instrument = forms.CharField()
    instrument_placeholder = "What do you play? (optional)"

    message = forms.CharField(widget=forms.Textarea, required=True)
    message_placeholder = "Please write us a message!"
