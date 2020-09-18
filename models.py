# Setting up a custom user model will require modification to models.py, settings.py, on your associated project.
# Custom user model will allow you to change the parameters that comes otb for django and use features like using email as the username. Example below goes in that direction. It keeps both email and username as part of the registration form, to remove username complete, just remove those lines from code.
# Suggest creating a separate app to house your custom user model and referencing the user data in setting files.
# changes needed in setting.py file includes adding the following: AUTH_USER_MODEL = 'users.User'
# listed below is a custom user model. review the views and forms file to understand how to take advantage of the custom user model.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username=models.CharField(max_length=30,unique=True)
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login',auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_custom_user_A=models.BooleanField(default=False) # since you are creating a custom user model, you can add data points to entend your original user model)
    is_custom_user_B=models.BooleanField(default=False) # since you are creating a custom user model, you can add data points to entend your original user model)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username'] # remove if you dont need it.

    objects=MyAccountManager()
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


