import pandas as pd
from time import perf_counter
from faker import Faker
from django.conf import settings
from celery import shared_task
from core.models import StoredFile
from core.utils import people_generator


@shared_task
def generate_csv_with_people_using_pandas(amount=10, filetype='csv'):
    tstart = perf_counter()

    sf = StoredFile.objects.create(filetype=filetype)
    df = pd.DataFrame(columns=['name', 'age', 'email', 'phone'], data=people_generator(amount))

    if filetype == 'csv':
        filepath = f'media/csv/{amount}_people.csv'
        df.to_csv(filepath, index=False)
    else:
        filepath = f'media/csv/{amount}_people.xlsx'
        df.to_excel(filepath, index=False)

    tend = perf_counter()
    time_elapsed = tend - tstart
    sf.status = StoredFile.STATUS.DONE
    sf.file = filepath
    sf.time_to_process = time_elapsed
    sf.save()