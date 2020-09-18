from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

# Registration form for users.

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,)

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
        labels = {"email": "Email", "username": "Full Name", "password1": "Password", "password2": "Password Confirmation" }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_custom_user_A = True # this is where you can take advantage of your custom user model. In this case, we are flagging the user to be a custom user as well, a field we set up in our model.
        if commit:
            user.save()
        return user
