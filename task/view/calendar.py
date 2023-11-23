from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class CalendarView(TemplateView):
    template_name = 'task/home/calendar.html'

    def get_context_data(self, **kwargs):
        _ = super().get_context_data(**kwargs)
