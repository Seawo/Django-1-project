from django import forms   # 장고에서 forms 모듈/ 꾸밈부분
from pybo.models import Question, Answer # 만들어논 Question 클래스 가지고 오면 subject, content 입력유형을 가지고 오기 위해

#forms.ModelForm : 입력할 수 있는 폼을 제공 
class QuestionForm(forms.ModelForm):
    class Meta:  # 클래스 오버라이딩 
        model = Question # 데이터 베이스 지정 table 지정
        fields = ['subject', 'content']
        labels={
            'subject':'제목',
            'content':'내용',
        }
# widgets --> form.as_p 로 들어간다.

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
        