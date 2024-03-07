from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,fullname,phonenumber,password,**extrafields):
        if not email:
            raise ValueError("Email should be valid and should not be empty")
        if not phonenumber:
            raise ValueError ("Phone is should be valid and not to be empty")
        email=self.normalize_email(email)
        extrafields.setdefault('is_staff',True)
        new_user= self.model(email = email , full_name = fullname, phone_number=phonenumber,**extrafields)
       
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user
    
    def create_superuser(self, email, full_name, phone_number, password, **extrafields):
        extrafields.setdefault('is_superuser', True)
        return self.create_user(email=email, fullname=full_name, phonenumber=phone_number, password=password, **extrafields)     
        



class CustomUser(AbstractUser):
    first_name=None
    last_name=None
    username=None
    full_name=models.CharField(_("Full Name"),unique=True,max_length=250)
    email = models.EmailField(_("Email Address"), unique=True)
    phone_number=PhoneNumberField(_("Phone Number"),unique=True)
    bio_pic = models.ImageField(_("Profile Image"),upload_to="profilepics/",blank=True,null=True)
    last_login=models.DateField(_("Last Login"),default=timezone.now)   
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS=["full_name","email"]   
    
    objects=CustomUserManager()

    def __str__(self) -> str:
        return self.email