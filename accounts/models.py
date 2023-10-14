from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


# Define CustomUserManager to handle user creation, validation, and authentication
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Check if email is provided
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        # Create user object and set password
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set is_staff and is_superuser to True for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# Define CustomUser model that extends AbstractBaseUser
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.TextField(max_length=255, null=True)
    surname = models.TextField(max_length=255, null=True)

    birthday_at = models.DateField(null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verification = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'birthday_at']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def is_admin(self):
        return self.is_superuser

    def has_perm(self, _):
        return self.is_staff

    def has_module_perms(self, _):
        return self.is_staff


# Define CustomGroup model that proxies the built-in Group model
class CustomGroup(Group):
    class Meta:
        # Field 'proxy' allows you to add extra methods or fields to the existing models without
        # having to redefine all of their built-in functionality.
        proxy = True


# Define CustomPermission model that proxies the built-in Permission model
class CustomPermission(Permission):
    class Meta:
        # Field 'proxy' allows you to add extra methods or fields to the existing models without
        # having to redefine all of their built-in functionality.
        proxy = True


# Define UserRole model to associate users with groups using ManyToManyField
class UserRole(models.Model):
    # Mean 'on_delete=models.CASCADE' it means that if a user or group is deleted,
    # all User Role objects that reference that user or group will also be deleted (cascaded)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        # Field 'unique_together' means that a user cannot belong to the same group multiple times,
        # and a group cannot have the same user multiple times.
        unique_together = ('user', 'group')
