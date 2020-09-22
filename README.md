# PythonDjango_code_CustomUserModel
Setting up custom user model in Python/Django


Setting up a custom user model will require modification to models.py, settings.py, on your associated project.
Custom user model will allow you to change the parameters that comes otb for django and use features like using email as the username. Example attached here is to give directions towards creating your own custom model. 
You will most likely need to tweak the code to meet your need. But the example here will give you insight on how to do the changes.
Tips:
I suggest creating a separate app to house your custom user model and referencing the user data in setting files.
Changes needed in setting.py file includes adding the following: AUTH_USER_MODEL = 'users.User'
I have also listed here views and forms file to understand how to take advantage of the custom user model.
Its best if you apply custom user model at the beginning of project, otherwise consider deleting your migration files and db, and starting fresh with db migration steps to avoid errors.

Good luck
