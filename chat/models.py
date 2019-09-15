from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_by', null=True, on_delete=models.SET_NULL)

    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name='modified_by', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'question'

class QuestionHistory(models.Model):
    question_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = 'question_history'

class Response(models.Model):
    response_text = models.CharField(max_length=255)
    question_history = models.ForeignKey(QuestionHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'response'