from django import forms

from teams.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Phone Number'})