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
from .models import KulindrikesDexamenes

class KulindrikesDexamenesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = KulindrikesDexamenes
#        fields = ['eidos', 'katigoriaid', 'upokatigoriaid', 'solines', 'sortnumber', 'solines_m3_15', 'solines_m3_thk']
        exclude = ['id']

import django_filters

class KulindrikesDexamenesDetailFilter(django_filters.FilterSet):
    class Meta:
        model = KulindrikesDexamenes
        exclude = ('id',)
        fields = {
            'code': ['exact', ],
            'katigoriaid' : ['exact', ],
            'Kausimaid': ['exact', ],
        }

class KulindrikesDexamenesTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = KulindrikesDexamenes
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        fields = ['code','detail','pl_orofi','katigoriaid','Kausimaid','date','ogkos']
        sequence = ['id', 'code' ,'detail' ,'...']

    def render_detail(self, record):
        rev = reverse('Tank_Measurment:editKulDex', kwargs={'pk': str(record.pk)})
#        rev = reverse('Tank_Measurment:list', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

def KulindrikesDexamenesDetailFiltered(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    data = KulindrikesDexamenes.objects.all()
    filter = KulindrikesDexamenesDetailFilter(request.GET, queryset=data)
    table = KulindrikesDexamenesTable(filter.qs)
    #     table = BioExaminationDetTable(BioExaminationDetail.objects.all().filter(BioExaminationId=exampk))

    RequestConfig(request, paginate={'per_page': 15}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                    {'objects': table,
                    'filter': filter,
                    'page_title': u'Ανάληση Εργαστηριακών για ',
                    'form_name': u'Ανάληση Εργαστηριακών για ',
                    'param_action1_name': 'Προσθήκη'})


        #@login_required
def KulindrikesDexamenesList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = KulindrikesDexamenesTable(KulindrikesDexamenes.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table, 'page_title': u'Kulindrikes Dexamenes',
                    'page_title': u'Kulindrikes Dexamenes',
                    'form_name': u'KulindrikesDexamenesList',
                    'param_action1': reverse('Tank_Measurment:createKulDex'),
                    'param_action1_name': 'Προσθήκη'})

class KulindrikesDexamenesCreate(CreatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = KulindrikesDexamenes
    form_class = KulindrikesDexamenesForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

#class KausimaEdit(UpdatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class KulindrikesDexamenesEdit(UpdatePopupMixin, UpdateView):
    model = KulindrikesDexamenes
    form_class = KulindrikesDexamenesForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################
