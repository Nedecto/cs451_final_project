from django.shortcuts import render

import json
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.conf import settings
from django import forms

from django.views import generic 
from geopy import distance
from geopy import Nominatim

from .models import Job

APP_LOCATION = settings.DEFAULT_LOCATION

class HomeView(generic.TemplateView):
    template_name = 'home.html'

class JobView(generic.DetailView):
	model = Job
	template_name = 'job.html'

	# Method override to provide additional context variables to template.
	def get_context_data(self, **kwargs):
		context = super(JobView, self).get_context_data(**kwargs)
		job_obj = self.get_object()

class JobListView(generic.ListView):
	model = Job
	template_name = 'jobs.html'

class SearchForm(forms.Form):
    jobs = forms.ModelMultipleChoiceField(queryset=Job.objects.all(), widget=forms.widgets.CheckboxSelectMultiple)

class SelectJobsView(generic.TemplateView):
    template_name = 'job_map.html'

    def get_context_data(self, **kwargs):
        context = super(SelectJobsView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


class JobsResultsRestView(generic.View):
	def post(self, request, *args, **kwargs):
		form = SearchForm(request.POST)

		title = ''
		wage = 0
		city = ''

		data = {'locations': [], 'title': title, "salary": wage, 'city': city}

		if form.is_valid:
			form_data = request.POST.getlist('jobs')
			job_objects = []
			for i in form_data:
				job_obj = Job.objects.get(pk=i)
				job_objects.append(job_obj)

			for i in job_objects:
				lat = i.latitude
				lon = i.longitude
				data['locations'].append({
					'lat': lat, 
					'lon': lon, 
					'title': i.title, 
					'salary': i.salary, 
					'city': i.city})
			print(data);
		return JsonResponse(data, safe=False)