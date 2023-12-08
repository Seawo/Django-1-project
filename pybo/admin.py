from django.contrib import admin
from .models import Question, Answer
# 내가 있는 위치에 Question,Answer를 불러오겠다

class QuestioAdminSearch(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question, QuestioAdminSearch)
admin.site.register(Answer)
# 등록


