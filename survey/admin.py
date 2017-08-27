# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Question, Choice, Answer


class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 0
	
	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		field = super(ChoiceInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		if db_field.name == 'choice':
			question = Question.objects.get(id=request.resolver_match.args[0])
			field.queryset = field.queryset.filter(question_id = question.id)  
		return field


class questionAdmin(admin.ModelAdmin):
	list_display = ["label", "timestamp"]
	ordering = ['-timestamp']
	inlines = [ChoiceInline]

admin.site.register(Question, questionAdmin)
admin.site.register(Answer)