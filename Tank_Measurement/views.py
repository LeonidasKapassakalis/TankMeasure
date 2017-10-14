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


from forms import ExampleForm
from django.views.generic.edit import FormView

class FormContainersMixin(object):
    def get_versions(self):
        return {
            "django_crispy_forms": 1,
            "crispy_forms_foundation": 1,
        }
#    def get_context_data(self, **kwargs):
#        context = super(FormContainersMixin, self).get_context_data(**kwargs)
#        context.update(self.get_versions())
#        print context
#        return context


    def get_success_url(self):
        return reverse('Tank_Measurment:list', args=[])


class FormF5ByTabView(FormContainersMixin, FormView):
    template_name = 'tabs.html'
    form_class = ExampleForm

    def clean(self):
        cleaned_data = super(ExampleForm, self).clean()
        checkbox_input = cleaned_data.get("checkbox_input")

        if checkbox_input and checkbox_input == True:
            raise forms.ValidationError([
            'This is a global error',
            'This is another global error',
            'Uncheck the "Checkbox input" to ignore these errors']
            )

        # Always return the full collection of cleaned data.
        print cleaned_data
        print 'Leonidas'
        return cleaned_data


#class ModelFormWidgetMixin(object):
#    def get_form_class(self):
#        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)



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
from models import InputForm
from compute import compute
from django.shortcuts import *
from django.template import RequestContext
import os

from django.shortcuts import render


def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
            result = result.replace('static/', '')
    else:
        form = InputForm()

#    return render_to_response('vib1.html',
#            {'form': form,
#             'result': result,
#             }, context_instance=RequestContext(request))
    context = {'form': form,'result': result}
    return render(request, 'vib1.html', context)

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
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
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

class KausimaEdit(UpdatePopupMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#class KausimaEdit(UpdatePopupMixin, UpdateView):
    model = Kausima
    form_class = KausimaForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################
