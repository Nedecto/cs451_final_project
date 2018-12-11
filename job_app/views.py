from django.shortcuts import render

from django.conf import settings 

APP_LOCATION = settings.DEFAULT_LOCATION

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