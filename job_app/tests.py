from django.test import TestCase

# Create your tests here.
from .models import Job

class JobsTestCase(TestCase):

	def setup(self):
		j = Job(title='Quantum Software Developer', 
			salary=250000,
			city='Seattle',
			latitude='47.6062',
			longitude='122.3321')
		j.save()

		jobs = Job.objects.all()

	def test_job(self):
		self.setup()

		test_job = Job.objects.get(title='Quantum Software Developer')

		self.assertEqual(test_job.salary, 250000)
		self.assertEqual(test_job.city, 'Seattle')