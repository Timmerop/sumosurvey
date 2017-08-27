from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.survey, name='survey'),
    url(r'warning/$', views.warning, name='warning'),
    url(r'results/$', views.results, name='results'),
    url(r'create-question/$', views.create_question, name='create_question'),
]