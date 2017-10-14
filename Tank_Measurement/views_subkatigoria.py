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

class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)



#addanother
from django_addanother.views import UpdatePopupMixin
from django_addanother.views import CreatePopupMixin

from views_admin import *

from django.contrib.admin import AdminSite
class MyAdminSite(AdminSite):
        pass

mysite = MyAdminSite()


def MainMenu(request):
    return render(request, 'NewMenuBootStrap.html')

def NewMenu(request):
    return render(request, 'NewMenu.html')

def NewMenu1(request):
    return render(request, 'NewMenuBootStrap.html')


########################################################################################################
from .models import Kausima

class KausimaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Kausima
        fields = ['eidos', 'katigoriaid', 'upokatigoriaid', 'solines', 'sortnumber', 'solines_m3_15', 'solines_m3_thk']




class KausimaTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Kausima
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['eidos' , 'katigoriaid', '...']

    def render_detail(self, record):
        rev = reverse('Tank_Measurment:edit', kwargs={'pk': str(record.pk)})
#        rev = reverse('Tank_Measurment:list', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def KausimaList(request):
#    if not request.user.is_authenticated:
#        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = KausimaTable(Kausima.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'KausimaList',
                    'form_name': u'KausimaList'})
#                    'param_action1': reverse('Tank_Measurment:list'),
#                    'param_action1_name': 'Προσθήκη'})

class KausimaCreate(CreatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Kausima
    form_class = KausimaForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

#class KausimaEdit(UpdatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class KausimaEdit(UpdatePopupMixin, UpdateView):
    model = Kausima
    form_class = KausimaForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################
