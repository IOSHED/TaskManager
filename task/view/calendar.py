
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from task.lib.calendar.Calendar import Calendar
from task.lib.calendar.TodayUserTasks import TodayUserTasks
from task.lib.calendar.Weather import Weather


@method_decorator(login_required, name='dispatch')
class CalendarView(TemplateView):
    template_name = 'task/home/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weather'] = Weather().get()
        context['calendar'] = Calendar().get()
        context['tasks'] = TodayUserTasks(self.request.user).get()
        return context
