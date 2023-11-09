from django.views.generic import TemplateView


class ProjectsView(TemplateView):
    template_name = 'task/home/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
