from django.http import HttpResponse
from django.views import View

from task.lib.calendar import OptionCalendarChoices


class CheckOption(View):
    @staticmethod
    def post(request):
        option = request.POST.get('option')

        if option == OptionCalendarChoices.DAY.value:
            return HttpResponse("""
               <input type="date" name="date" class="form-control" placeholder="Date" id="date" required="">
            """)
        elif option == OptionCalendarChoices.MONTH.value:
            return HttpResponse("""
                <input type="month" name="date" class="form-control" placeholder="Date" id="date" required="">
            """)
        elif option == OptionCalendarChoices.YEARS.value:
            return HttpResponse("""
                <input type="number" name="date" class="form-control" placeholder="Years" id="date" required="">
            """)
        else:
            return HttpResponse("This option is not required")
