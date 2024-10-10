from django.urls import path

from .views import detail,meetings_list_view

#domain.com/website/...
urlpatterns=[
    path('',meetings_list_view, name='meetings'),
    path('details/<int:id>',detail, name='detail'),
]