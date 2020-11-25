from django.db import models
from django.contrib.auth.models import User,AbstractUser, BaseUserManager
from multiselectfield import MultiSelectField
from .choices import *


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not username:
			raise ValueError("Users must have an username")

		user  = self.model(
				email=self.normalize_email(email),
				username=username,
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user  = self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

	def create_doctor(self, email, username, password):
		user  = self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username,
			)
		
		user.is_doctor = True
		user.save(using=self._db)
		return user

class Clinic(models.Model):
    name                    = models.CharField(max_length=200)
    region                  = models.CharField(max_length=100, choices=REGIONS, default="София")
    city                    = models.CharField(max_length=100,blank=True)
    address                 = models.CharField(max_length=200,blank=True)
    
    
    def __str__(self):
        return self.name

class Account(AbstractUser):
    
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	image                   = models.ImageField()
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_staff                = models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_doctor				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	first_name 				= models.CharField(max_length=50,blank=True)
	last_name 				= models.CharField(max_length=50,blank=True)
	phone	                = models.CharField(max_length=50,blank=True)
	insurers                = MultiSelectField(choices=INSURERS,blank=True)
	city                    = models.CharField(max_length=100,blank=True)
	address                 = models.CharField(max_length=200,blank=True)
	region                  = models.CharField(max_length=100,choices=REGIONS,blank=True)
	specialty               = MultiSelectField(choices=SPECIALTY ,blank = True)
	works_in                = models.ManyToManyField(Clinic ,blank=True)
	website                 = models.URLField(blank=True)
	description             = models.TextField(blank=True)
    
	

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', ]

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

class Image(models.Model):
    image = models.ImageField(upload_to='account-images/%Y/%m/%d/', blank=True)
    multiImage = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='images' )