# PythonDjango_code_CustomUserModel
Setting up custom user model in Python/Django


# Setting up a custom user model will require modification to models.py, settings.py, on your associated project.
# Custom user model will allow you to change the parameters that comes otb for django and use features like using email as the username. Example below goes in that direction. It keeps both email and username as part of the registration form, to remove username complete, just remove those lines from code.
# Suggest creating a separate app to house your custom user model and referencing the user data in setting files.
# changes needed in setting.py file includes adding the following: AUTH_USER_MODEL = 'users.User'
# listed here is a custom user model. review the views and forms file to understand how to take advantage of the custom user model.

Good luck
