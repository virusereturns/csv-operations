import csv
from time import perf_counter

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib import messages

import pandas as pd
from faker import Faker

from .models import Person
from .utils import generate_people_list, people_generator
from core import tasks

from icecream import ic


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
        writer = csv.writer(response)
        writer.writerow(['name', 'age', 'email', 'phone'])
        list_of_people = generate_people_list(amount)
        writer.writerows(list_of_people)
        tend = perf_counter()
        if settings.DEBUG:
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

        df = pd.DataFrame(people_generator(amount))
        filetype = request.POST.get('filetype', 'csv')
        if filetype == "xls":
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={amount}_people.xlsx'
            df.to_excel(response, index=False)
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={amount}_people.csv'
            df.to_csv(response, index=False)
        tend = perf_counter()
        if settings.DEBUG:
            print(f"Time taken: {tend - tstart:.5f}s")

        return response


class StoredFilesListView(ListView):
    model = tasks.StoredFile
    template_name = 'core/stored_files.html'
    context_object_name = 'files'