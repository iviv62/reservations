from django.db import models
from django.contrib.auth.models import User,AbstractUser, BaseUserManager
from multiselectfield import MultiSelectField
from .choices import *
from django_better_admin_arrayfield.models.fields import ArrayField
import datetime

class TimeStampable(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

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
    uid 					= models.AutoField(primary_key=True, auto_created=True,blank=True,verbose_name="UID" )
    name                    = models.CharField(max_length=200)
    region                  = models.CharField(max_length=100, choices=REGIONS, default="София")
    city                    = models.CharField(max_length=100,blank=True)
    address                 = models.CharField(max_length=200,blank=True)
    
    
    def __str__(self):
        return self.name

class Account(AbstractUser):
	uid 					= models.AutoField(primary_key=True ,auto_created=True,blank=True,verbose_name="UID" )
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_staff                = models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_doctor				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	first_name 				= models.CharField(max_length=50,blank=True)
	last_name 				= models.CharField(max_length=50,blank=True)
	phone					= models.CharField(max_length=50,blank=True)
	region					= models.CharField(max_length=100,choices=REGIONS,blank=True)
	insurers                = MultiSelectField(choices=INSURERS,blank=True)
	badges					= MultiSelectField(choices=BADGES,blank=True,null=True)
	specialty               = MultiSelectField(choices=SPECIALTY ,blank = True)
	city                    = models.CharField(max_length=100,blank=True)
	address                 = models.CharField(max_length=200,blank=True)
	works_in                = models.ManyToManyField(Clinic ,blank=True)
	website                 = models.URLField(blank=True)
	
    
	

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
    image      = models.ImageField(upload_to='account-images/%Y/%m/%d/', blank=True)
    #alt_text   = models.CharField(max_length=75) 
    multiImage = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='images' )
    
class AccountInfoField(models.Model):
 	user = models.ForeignKey(Account, on_delete=models.CASCADE )
 	title = models.CharField(max_length=100,blank=True)
 	description = models.TextField(blank=True)



class Holiday(models.Model):
    doctor                 = models.ForeignKey(Account,on_delete=models.CASCADE,)
    date                   = models.DateField()
    clinic                 = models.ForeignKey(Clinic,on_delete=models.CASCADE,)
    

class Reservation(TimeStampable):
    user                   = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="userReservation")
    doctor                 = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="doctorReservation")
    clinic                 = models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name="clinicReservation")
    date                   = models.DateField()
    time_slot              = models.TimeField()
    
class TimeSlot(TimeStampable):
    clinic                 = models.ForeignKey(Clinic,on_delete=models.CASCADE,related_name="Clinic")
    doctor                 = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="doc")
    day                    = models.CharField(max_length=100, choices=DAYS_OF_WEEK)
    time_slot              = ArrayField(models.TimeField(blank=True,null=True), blank=True,)