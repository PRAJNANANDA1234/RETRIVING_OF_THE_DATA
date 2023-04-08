from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
     

class Odisha(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField(default='puri@gmail.com')
    
    

class Temple(models.Model):
    name=models.ForeignKey(Odisha,on_delete=models.CASCADE)
    father_of_temple=models.CharField(max_length=100)
    date=models.DateField()
    
