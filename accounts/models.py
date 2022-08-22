# accounts/models.py
# Django modules
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    """
    Create new users
    """
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo eletrónico')
        
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        
        # Set some parameters
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
    Redifine the user
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # Field attributes of Django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Login with email
    USERNAME_FIELD = 'email'
    # Required fields to register a new user
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # MyAccountManager instance
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        """
        To see if a user has permissions
        """
        return self.is_admin
    

    def has_module_perms(self, add_label):
        """
        If it is admin, it will have access to modules
        """
        return True