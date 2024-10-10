from django.urls import path

from . import views

#domain.com/website/...
urlpatterns=[
    path('',views.meetings_list_view, name='meetings'),
]