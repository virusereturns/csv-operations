# csv-operations
A sandbox to play with different CSV generation and reading with Django

I'm planning to work using different methods of generating very large CSV files, and testing celery and other methods to test the performance of different CSV files generation.

Requirements

* Python 3.10
* Redis

Installation:

* A python 3.10 virtualenv is highly recommended.
* Install requirements
```
python -m pip install -r requirements.txt
```
* Install migrations
```
python manage.py migrate
```
* All done, you can run the server and access it via localhost:port in your browser. Eg:
```
python manage.py runserver 0:8000
```
* To run the celery worker, in a different terminal run the following command. Although it's not necessary until you use the celery tasks. For celery to run we require Redis to be running. I've decided Redis over RabbitMQ because of the simplicity of the project.
```
celery -A csv_operations worker -l info
```

## Demo soon
