from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
import datetime
this_year = datetime.datetime.now().year

class Skill(models.Model):
    types = [
        ('coding' , 'coding'),
        ('other' ,'other'),
    ]
    
    name = models.CharField(max_length=100 ,null=True ,blank=True)
    progress = models.IntegerField(default =  0 ,
                                    validators=[MaxValueValidator(100), MinValueValidator(1)])
    _type = models.CharField(max_length=100 , blank=True,null=True , choices=types)
    
    def __str__(self):
        return self.name
    
    

class Education (models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(max_length=100 , blank=True ,null=True)
    year = models.IntegerField(default=this_year ,
                                validators=[MinValueValidator(2007)] )
    location = models.CharField(max_length=100, blank=True,null=True)
    
    
    def __str__(self):
        return self.title

class Experience (models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(max_length=1000 , blank=True ,null=True)
    year = models.IntegerField(default=this_year ,
                                validators=[ MinValueValidator(2007)] )
    location = models.CharField(max_length=100, blank=True,null=True)
    
    
    def __str__(self):
        return self.title


class Project(models.Model):
    types = [
        ('Web App','Web App'),
        ('Mobile App','Mobile App'),
        ('Scripting/Bot','Scripting/Bot'),
    ]
    title = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(max_length=1000 , blank=True ,null=True)
    _type = models.CharField(max_length=100, blank=True,null=True , choices=types)
    cover = models.ImageField(blank=True,null=True , upload_to='Prjoects/')
    
    def __str__(self):
        return self.title
    
    @property
    def get_type(self):
        return self._type

class Blog(models.Model):
    types = [
        ('Technology','Technology'),
        ('Social life','Social life'),
        ('Gaming','Gaming'),
    ]
    title = models.CharField(max_length=100, blank=True,null=True)
    _type = models.CharField(max_length=100 , blank=True , null=True , choices = types)
    created_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.title

    @property
    def get_type(self):
        return self._type
    
    @property
    def get_date(self):
        return str(self.created_at)

class Testimonial(models.Model):
    client = models.CharField(max_length=100, blank=True,null=True)
    image = models.ImageField(blank=True,null=True , upload_to='Clients/')
    body = models.TextField(max_length=1000 , blank=True ,null=True)
    job = models.CharField(max_length=100, blank=True,null=True)
    
    
    def __str__(self):
        return self.client




