from django.urls import path

from .views import detail,meetings_list_view,add_meeting, delete_meeting, update_meeting

#domain.com/website/...
urlpatterns=[
    path('', meetings_list_view, name='meetings'),
    path('details/<int:id>', detail, name='detail'),
    path('new/', add_meeting, name='add'),
    path('delete/<int:id>/', delete_meeting, name='delete'),
    path('update/<int:id>/', update_meeting, name='update_meeting'),
    path('new/', add_meeting, name='add'),
]