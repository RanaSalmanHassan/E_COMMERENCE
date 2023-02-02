from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
# Create your models here.

# To automatically create one to one object
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('THE EMAIL MUST BE SET!')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser (self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super User have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super User must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email  = models.EmailField(unique=True,null=False)

    is_staff = models.BooleanField(gettext_lazy('Staff Status'),default=False,
    help_text=gettext_lazy('Designates whether the user can login or not'))

    is_active = models.BooleanField(gettext_lazy('Active Status'),default=True,
    help_text=gettext_lazy('Designates whether the user is active or not'))

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email     
    def get_short_name(self):
        return self.email




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username = models.CharField(max_length=100,null=True,blank=True)
    full_name = models.CharField(max_length=200,null=True,blank=True)
    address_1 = models.TextField(max_length=300,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    zip_code = models.CharField(max_length=10,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.username + "`s Profile"


    def is_fully_filled(self):
        fields_name = [f.name for f in self.is_meta.get_fields()]

        for feild_name in fields_name:
            value = getattr(self,feild_name)

            if value is None:
                return False
        return True        



@receiver(post_save,sender= User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender= User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

