#changes you can make to your registration form.

from django.contrib.auth import login, authenticate
from users.forms import RegistrationForm
from users.models import User

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect ('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render (request, 'users/register.html', context) # render to your specific template, not the one referenced here.
