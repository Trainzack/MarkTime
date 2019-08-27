from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'What is your name?',
                                                         'class': 'mb-4 contact-form-input'}),
                           )

    contacter_email = forms.EmailField(required=True,
                                       widget=forms.TextInput(attrs={'placeholder': 'How do we contact you?',
                                                                     'class': 'mb-4 contact-form-input'}),
                                       )

    instrument = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What instrument do you play? (optional)',
                                                               'class': 'mb-4 contact-form-input'}))

    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'placeholder': 'Please write us a message!',
                                                           'class': 'contact-form-input'}),
                              )
