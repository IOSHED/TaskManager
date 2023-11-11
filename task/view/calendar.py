from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView

from task.forms import SettingsCalendarForm
from task.lib.calendar import OptionCalendarChoices
from task.lib.filters import get_calendar


@method_decorator(login_required, name='dispatch')
class CalendarView(FormView):
    template_name = 'task/home/calendar.html'
    form_class = SettingsCalendarForm


@method_decorator(login_required, name='dispatch')
class GetCalendarView(View):
    form_class = SettingsCalendarForm

    @staticmethod
    def post(request):
        option = request.POST.get('option')
        date = request.POST.get('date')
        is_display_holidays = request.POST.get('is_display_holidays')
        is_display_weather = request.POST.get('is_display_weather')
        is_display_tasks = request.POST.get('is_display_tasks')

        data = get_calendar(option, date, is_display_holidays, is_display_weather, is_display_tasks)

        return HttpResponse(data)
