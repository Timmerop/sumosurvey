# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from . import models

# Create your tests here.
class SurveyUnitTest(TestCase):
	def test_sorted_choice_set(self):
		question1 = models.Question.objects.create(
			label='test1'
		)
		choice1 = models.Choice.objects.create(
			question=question1,
			label='choice1'
		)
		choice2 = models.Choice.objects.create(
			question=question1,
			label='choice2'
		)
		choice3 = models.Choice.objects.create(
			question=question1,
			label='choice3'
		)

		models.Answer.objects.create(
			question=question1,
			choice=choice2,
			visitor='1'
		)

		self.assertEqual(question1.sorted_choice_set[0], choice2)

		models.Answer.objects.create(
			question=question1,
			choice=choice3,
			visitor='2'
		)

		models.Answer.objects.create(
			question=question1,
			choice=choice3,
			visitor='3'
		)

		self.assertEqual(question1.sorted_choice_set[0], choice3)

	def 
