from django import forms


class Contact (forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "name",
            'name': "name",
            'placeholder': "Name Here",
        }

    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        'class':"form-control" ,
        'id':"email" ,
        'name':"email" ,
        'placeholder' :"Email Here",
    }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
        'class':"form-control" ,
        'id':"message" ,
        'name':"message" ,
        'placeholder' :"Please enter your message here Bro",
        'rows' :'5',
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email :
            raise forms.ValidationError("Enter A Gmail.")
        return email