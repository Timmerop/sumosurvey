# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth
from django.views.generic.base import TemplateResponseMixin, View
from django.db.models import OuterRef, Subquery

from django.contrib.auth.decorators import login_required

from .models import Question, Answer, Choice

def survey(request):
	visitor = request.session.session_key
	
	if not visitor:
		request.session.save()
		visitor = request.session.session_key

	if request.method == 'POST':	
		question = get_object_or_404(Question, pk=request.POST['question'])
		choice = question.choice_set.get(pk=request.POST['choice'])

		answer, created = Answer.objects.get_or_create(
			question=question,
			visitor=visitor,
			defaults={'choice': choice} 
		)

		if not created:
			answer.choice = choice
		answer.update()

	visitor_answers = Answer.objects.filter(question=OuterRef('pk'), visitor=visitor).order_by('last_update')
	question_set = Question.objects.annotate(last_update=Subquery(visitor_answers.values('last_update'))).order_by('last_update', '?')

	if not question_set.exists():
		return redirect('warning')

	template_args = {
		'question' : question_set[0]
	}
	return render(request, 'survey.html', template_args)

def warning(request):
	if request.user.is_authenticated():
		return redirect('/create-question')
	return render(request, 'warning.html')

@login_required()
def results(request):
	question_set = Question.objects.all().order_by('-timestamp')
	template_args = {
		'question_set' : question_set
	}
	return render(request, 'results.html', template_args)


@login_required()
def create_question(request):
	if request.method == 'POST':
		question_label = request.POST.get('label').strip()
		if question_label[-1] == '?':
			question_label = question_label[:-1]
		question = Question.objects.create(
			label=question_label
		)
		for label in request.POST.getlist('choice_set'):
			if len(label):
				Choice.objects.create(
					question=question,
					label=label
				)
		return redirect(request.GET.get('from','/'))
	return render(request, 'create_question.html')