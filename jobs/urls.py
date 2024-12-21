from django.urls import path
from .views import Joblist
from .views import test_view

urlpatterns=[
    path('jobs/', Joblist.as_view(),name='job-list-create'),
    path('test/', test_view),

]