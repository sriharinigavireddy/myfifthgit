from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'),
    path('user/',user,name='user'),
]