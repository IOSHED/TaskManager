from django.views.generic import TemplateView


class CalendarView(TemplateView):
    template_name = 'task/home/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
