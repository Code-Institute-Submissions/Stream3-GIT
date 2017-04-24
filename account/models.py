from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
  #This field is required. 
  user = models.OneToOneField(User)

  #Other fields here
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  image = models.ImageField(upload_to="images", blank=True, null=True)
  """docstring for UserProfile"models.Modelef __init__(self, arg):
    super(UserProfile,models.Model.__init__()
    self.arg = arg"""

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')
 
        email = self.normalize_email(email)
        ##profile_img = models.ImageField(upload_to="profile_img", blank=True, null=True)

        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
 
        return user
 
"""class User(AbstractUser):
    objects = AccountUserManager()
 
    def is_subscribed(self, magazine):
        try:
            purchase = self.purchases.get(magazine__pk=magazine.pk)
        except Exception:
            return False
 
        if purchase.subscription_end > timezone.now():
            return False
 
        return True"""