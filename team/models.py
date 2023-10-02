from django.db import models

# Create your models here.

# class TeamMember(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='team_photos')

#     def __str__(self):
#         return self.title
    
class Event(models.Model):
    photo = models.ImageField(upload_to='event_photos')
    date = models.DateField()
    time=models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    location = models.TextField(max_length=100,default='IU Auditorium')
    content = models.TextField(max_length=1000)

    def formatted_date(self):
        return self.date.strftime("%d %B %Y")
    def __str__(self):
        return self.title
    
class Team(models.Model):

    photo = models.ImageField(upload_to='event_photos')
    name=models.CharField(max_length=300)
    title=models.CharField(max_length=300)

    def __str__(self):
        return self.title
    
class Upcomming_event(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    time=models.CharField(max_length=300)
    location = models.CharField(max_length=100,default='IU Auditorium')

    def formatted_date(self):
        return self.date.strftime("%d %B %Y")
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000,default=" ",null=True)
    

    def __str__(self):
        return self.subject
    
class ExCom(models.Model):
    photo = models.ImageField(upload_to='Excom_photo')
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=1000,default=" ",null=True)
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.name

