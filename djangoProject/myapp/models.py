from django.db import models


# Create your models here.
class Question(models.Model):
    sl_no = models.IntegerField(default=0)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_1 = models.CharField(max_length=200)
    choice_2 = models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_1 
    def __str__(self):
        return self.choice_2 
    def __str__(self):
        return self.choice_3