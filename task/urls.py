from django.urls import path

from .view import HomeView
from .view.calendar import CalendarView, GetCalendarView
from .view.check import CheckOption
from .view.projects import ProjectsView
from .view.tasks import TasksView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/get/', GetCalendarView.as_view(), name='get-calendar'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('tasks/', TasksView.as_view(), name='tasks'),
]

htmx_patterns = [
    path('check-option/', CheckOption.as_view(), name='check-option'),
]

urlpatterns += htmx_patterns
