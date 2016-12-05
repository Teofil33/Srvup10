from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
	# Customization, dob not needed, username needed
    #def create_user(self, email, date_of_birth, password=None):
    def create_user(self, username=None, email=None,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # Customization
        if not username:
            raise ValueError('Must Include Username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
        	# Customization
        	username = username,
            email=self.normalize_email(email),
            # Customization, dob not needed
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # Customization    
    # def create_superuser(self, email, date_of_birth, password):
    def create_superuser(self, username, email,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
        	# Customization
        	username = username,
            email=email,
            password=password,
            #date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
	# Customization
	username = models.CharField(
		#verbose_name = "username",
		max_length = 333,
		unique = True
	)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
    # Customization
	first_name = models.CharField(
		max_length=120,
		null=True,
		blank=True,
	)

	# Customization
	last_name = models.CharField(
		max_length=120,
		null=True,
		blank=True,
	)

	# Customization
    #date_of_birth = models.DateField()

    # Customization
	is_member = models.BooleanField(default=False, verbose_name="Is Paid Member")
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	# Customization
	#USERNAME_FIELD = 'email'

	# Customization
	USERNAME_FIELD = 'username'

	# Customization
	# REQUIRED_FIELDS = ['date_of_birth']

	# Customization
	REQUIRED_FIELDS = ['email']

	def get_full_name(self):
		# Customization
		return "%s %s" %(self.first_name, self.last_name)

		# The user is identified by their email address
		#return self.email

	def get_short_name(self):
		# Customization
		return self.first_name

		# The user is identified by their email address
		#return self.email

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.email

    # Customization    
	def __unicode__(self):              # __unicode__ on Python 2
		return self.email    

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin


class UserProfile(models.Model):
	user = models.OneToOneField(MyUser)
	bio = models.TextField(null=True, blank=True)
	facebook_link = models.CharField(
			max_length=320,
			null=True,
			blank=True,
			verbose_name="Facebook Profile Link")
	twitter_handle = models.CharField(
			max_length=320,
			null=True,
			blank=True,
			verbose_name="Twitter handle")

	def __unicode__(self):
		return self.user.username




