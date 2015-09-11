from django.db import models
import datetime
import django.utils.timezone

# Create your models here.
class Questions(models.Model):
    """
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',default=django.utils.timezone.now())
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    """
    """
    question = models.ForeignKey(Questions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text 