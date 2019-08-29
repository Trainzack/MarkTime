from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'What is your name?',
                                                         'class': 'mb-4 contact-form-input'}),
                           )

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'How do we contact you?',
                                                            'class': 'mb-4 contact-form-input'}),
                             )

    instrument = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'What instrument do you play? (optional)',
                                                               'class': 'mb-4 contact-form-input'}))

    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'placeholder': 'Please write us a message!',
                                                           'class': 'contact-form-input'}),
                              )


class PerformanceRequestForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'What is your name?',
                                                         'class': 'mb-4 contact-form-input'}),
                           )

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'How do we contact you?',
                                                            'class': 'mb-4 contact-form-input'}),
                             )

    event_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder': "What's the name of the event?",
                                                               'class': 'mb-4 contact-form-input'}),
                                 )

    # Note : I tried using forms.TimeField and forms.DateField but the validation provided for those is wonky
    # So Instead details regarding date and time are asked for here.
    event_details = forms.CharField(required=True,
                                    widget=forms.Textarea(attrs={'placeholder': 'Tell us as much about your '
                                                                                'event as you can! '
                                                                                'Where is the event going '
                                                                                'to take place? What day is the event '
                                                                                'taking place? What time will we be '
                                                                                'performing at and how long do '
                                                                                'you want us to play? What does '
                                                                                'the event itself consist of?',
                                                          'class': 'contact-form-input'}),
                                    )