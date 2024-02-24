import csv
from time import perf_counter

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

import pandas as pd
from faker import Faker

from .models import Person


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Left if necessary to add stuff
        return context


class GenerateRandomPeopleCsv(TemplateView):
    template_name = 'core/generate_random_people.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Your file is being generated. Please wait a moment.')
        tstart = perf_counter()
        amount = int(request.POST.get('amount', 10))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={amount}_people.csv'

        fake = Faker()
        writer = csv.writer(response)
        writer.writerow(['name', 'age', 'email', 'phone'])

        for _ in range(amount):
            writer.writerow([fake.name(), fake.random_int(min=18, max=100, step=1), fake.email(), fake.phone_number()])

        tend = perf_counter()
        print(f"Time taken: {tend - tstart:.5f}s")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'python csv module'
        return context


class GenerateRandomPeopleWithPandas(TemplateView):
    template_name = 'core/generate_random_people.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'pandas'
        return context

    def post(self, request, *args, **kwargs):
        tstart = perf_counter()
        amount = int(request.POST.get('amount', 0))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={amount}_people.csv'

        fake = Faker()
        people = []

        for _ in range(amount):
            people.append(
                {
                    'name': fake.name(),
                    'age': fake.random_int(min=18, max=100, step=1),
                    'email': fake.email(),
                    'phone': fake.phone_number(),
                }
            )

        df = pd.DataFrame(people)
        df.to_csv(response, index=False)
        tend = perf_counter()
        print(f"Time taken: {tend - tstart:.5f}s")
        return response
