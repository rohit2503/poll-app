from django.contrib import admin

# Register your models here.
from models import Questions, Choice


class ChoiceInline(admin.TabularInline): #admin.StackedInline)
    """
    """
    model = Choice
    extra = 3
class QuestionaAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
                 ('Question Text',   {'fields' : ['question_text']}),
                 ('Date Information',   {'fields' : ['pub_date'],'classes' : ['collapse']}),
                 ]
#     fields = ['pub_date','question_text']
    inlines = [ChoiceInline]

admin.site.register(Questions, QuestionaAdmin)
