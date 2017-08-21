from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):                                          
    def new():                                                              
        new = Question.objects.order_by('added_at')
        return new                                                            
    def popular():                                                          
        popular = Question.objects.order_by('rating')
        return popular 


class Question(models.Model):
    
    objects = QuestionManager()
	    
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField()
    author = models.ForeignKey(User, blank=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')    

    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ['-added_at']
        verbose_name_plural = "Question"
    
class Answer(models.Model):
    
    text = models.TextField()
    added_at = models.DateTimeField()
    author = models.ForeignKey(User, blank=True)
    question = models.ForeignKey(Question, blank=True)     
    
    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ['-added_at']
        verbose_name_plural = "Answer"
