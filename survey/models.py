# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


class Question(models.Model):
	label = models.CharField(max_length=200)
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	
	def __str__(self):
		return self.label

	@property
	def sorted_choice_set(self):
	    return self.choice_set.annotate(answer_count=models.Count('answer_set')).order_by('-answer_count')

class Choice(models.Model):
	question = models.ForeignKey(Question, related_name='choice_set',  on_delete=models.CASCADE)
	label = models.CharField(max_length=200)

class Answer(models.Model):
	visitor = models.CharField(max_length=100)
	question = models.ForeignKey(Question, related_name='answer_set',  on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, related_name='answer_set',  on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	last_update = models.DateTimeField(default=datetime.datetime.now())

	def update(self):
		self.last_update = datetime.datetime.now()
		self.save()