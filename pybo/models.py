from django.db import models

# Create your models here.

class Question(models.Model): # 함수들을 저장해놓는 주머니
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): # 제목이 보이도록 설정
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()