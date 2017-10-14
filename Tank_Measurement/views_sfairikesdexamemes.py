# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

#from .views import ModelFormWidgetMixin

from django_addanother.views import UpdatePopupMixin
from django_addanother.views import CreatePopupMixin

########################################################################################################
from .models import SfairikesDexamemes

class SfairikesDexamemesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = SfairikesDexamemes
#        fields = ['eidos', 'katigoriaid', 'upokatigoriaid', 'solines', 'sortnumber', 'solines_m3_15', 'solines_m3_thk']
        exclude = ['id']

class SfairikesDexamemesTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = SfairikesDexamemes
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['id', 'code' ,'detail' ,'...']

    def render_detail(self, record):
        rev = reverse('Tank_Measurment:editSfaDex', kwargs={'pk': str(record.pk)})
#        rev = reverse('Tank_Measurment:list', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def SfairikesDexamemesList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = SfairikesDexamemesTable(SfairikesDexamemes.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Sfairikes Dexamenes',
                    'page_title': u'Sfairikesdexamemes Dexamenes',
                    'form_name': u'sfairikesdexamemesList',
                    'param_action1': reverse('Tank_Measurment:createSfaDex'),
                    'param_action1_name': 'Προσθήκη'})

class SfairikesDexamemesCreate(CreatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SfairikesDexamemes
    form_class = SfairikesDexamemesForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

#class KausimaEdit(UpdatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class SfairikesDexamemesEdit(UpdatePopupMixin, UpdateView):
    model = SfairikesDexamemes
    form_class = SfairikesDexamemesForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################
