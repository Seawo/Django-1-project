from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models의 Model 기능을 상속
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 질문 길이를 200자 이내로 제한
    content = models.TextField()  
    create_date = models.DateTimeField() #날짜와 시간에대한 기록
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # 외래키 : 외부와 연결할 수 있게 하는 키( 질문, 질문이 지워지면 답변도 지워진다)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    
