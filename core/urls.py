from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('generate-random-people-csv/', views.GenerateRandomPeopleCsv.as_view(), name='generate-random-people-csv'),
    path(
        'generate-random-people-pandas/',
        views.GenerateRandomPeopleWithPandas.as_view(),
        name='generate-random-people-pandas',
    ),
]
