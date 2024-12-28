from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    name = models.CharField(max_length=300,null=True,blank=True)
    profile_img = models.ImageField(upload_to='profile', null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=50,null=True,blank=True)
    last_login_time = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class Address(models.Model):
    address_line1 = models.CharField(max_length=400)
    address_line2 = models.CharField(max_length=400, null=True, blank=True)  # Corrected typo and added null/blank
    user = models.ForeignKey(CustomUser, related_name='addresses', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    is_default = models.BooleanField(default=False)  # Added the missing field

    def save(self, *args, **kwargs):
        if self.is_default:
            # Set all other addresses for this user as non-default
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super(Address, self).save(*args, **kwargs)

    def __str__(self):
        # Corrected to use address_line2 instead of address_len2
        return self.address_line2 or self.address_line1

    class Meta:
        verbose_name_plural = "Addresses"
