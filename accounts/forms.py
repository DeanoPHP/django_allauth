from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self, request):
        # Go to my parent class — SignupForm — and use its save() method.
        user = super().save(request)

        # Assign that value to the existing first_name field on this Django User.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Return the user object back to allauth
        return user
