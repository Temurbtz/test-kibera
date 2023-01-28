from django.urls import path
from .views import *
urlpatterns = [
   path('new/create', CreateNewView.as_view()),
   path('new/list',NewsListView.as_view()),
   path('new/get/<str:name>',GetSingleNewView.as_view()),
    path('new/updatedestroy/<str:name>',UpdateDestroyView.as_view())
]