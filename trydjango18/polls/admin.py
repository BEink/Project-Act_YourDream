from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','pub_date']


admin.site.register(Question,QuestionAdmin)