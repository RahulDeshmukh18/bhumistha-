from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=600)
    def __str__(self):
        return self.name
    
class Main(models.Model):
    title = models.CharField(max_length=20)
    tagline = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=20)
    tagline = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(default='static/main/images/5856.jpg' , upload_to='images/')
    def __str__(self):
        return self.title
    
class Vision(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.title
    
class Mission(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    tagline = models.CharField(default="Hello" ,max_length=100)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.title
    
class Objective(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    tagline = models.CharField(default="Hello" ,max_length=100)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.title
    
class Team(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=600)
    def __str__(self):
        return self.title
    
class Research(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    tagline = models.CharField(default="Hello" ,max_length=20)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.title
    
class Innovation(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    tagline = models.CharField(default="Hello" ,max_length=100)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/main/images/5856.jpg', upload_to='images/')
    tagline = models.CharField(default="Hello" ,max_length=100)
    description = models.CharField(max_length=600)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.title
    
class Application(models.Model):
    title = models.CharField(max_length=20)
    tagline = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.title