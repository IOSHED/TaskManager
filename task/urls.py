from django.urls import path

from .view import HomeView
from .view.calendar import CalendarView
from .view.projects import ProjectsView
from .view.tasks import TasksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('tasks/', TasksView.as_view(), name='tasks'),
]
