from django import forms
from task.lib.calendar import OptionCalendarChoices
import datetime


class SettingsCalendarForm(forms.Form):
    option = forms.TypedChoiceField(choices=[(e.value, e.name) for e in OptionCalendarChoices], initial="MONTH")

    date = forms.DateField(initial=datetime.date.today().strftime('%Y-%m'))

    is_display_holidays = forms.BooleanField()
    is_display_weather = forms.BooleanField()
    is_display_tasks = forms.BooleanField()
