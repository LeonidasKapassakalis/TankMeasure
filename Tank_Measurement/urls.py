from django.conf.urls import url


from . import views
from . import views_kulindrikesdexamenes
from . import views_sfairikesdexamemes


from models import Kausima
from dal import autocomplete

app_name = 'Tank_Measurment'
urlpatterns = [
#    url(r'^$', views.index, name='index'),

#    url(r'^list/$', views.PublisherList.as_view(), name='list'),
    url(r'^list/$', views.KausimaList, name='list'),
    url(r'^listk/$', views.KausimaList, name='listKausima'),
    url(r'^editkaysima/(?P<pk>[0-9]+)/$', views.KausimaEdit.as_view(), name='edit'),

#    url(r'^listKD/$', views_kulindrikesdexamenes.KulindrikesDexamenesList, name='listKulDex'),
    url(r'^listKD/$', views_kulindrikesdexamenes.KulindrikesDexamenesDetailFiltered, name='listKulDex'),

    url(r'^createKD/$', views_kulindrikesdexamenes.KulindrikesDexamenesCreate.as_view(), name='createKulDex'),
    url(r'^editKD/(?P<pk>[0-9]+)/$', views_kulindrikesdexamenes.KulindrikesDexamenesEdit.as_view(), name='editKulDex'),

    url(r'^listSD/$', views_sfairikesdexamemes.SfairikesDexamemesList, name='listSfaDex'),
    url(r'^createSD/$', views_sfairikesdexamemes.SfairikesDexamemesCreate.as_view(), name='createSfaDex'),
    url(r'^editSD/(?P<pk>[0-9]+)/$', views_sfairikesdexamemes.SfairikesDexamemesEdit.as_view(), name='editSfaDex'),

    url(r'^calc/$', views.index),
    url(r'^crisp/$', views.FormF5ByTabView.as_view(), name='editSfaDex'),

    # url(r'^detail/(?P<pk>[0-9]+)/$', views.PeopleDetailView.as_view(), name='detail'),
    # url(r'^update/(?P<pk>[0-9]+)/$', views.PeopleUpdate.as_view(), name='update'),
    # url(r'^delete/(?P<pk>[0-9]+)/$', views.PeopleDelete.as_view(), name='delete'),
    # url(r'^create/$', views.PeopleCreare.as_view(), name='create'),
    # url(r'^listd/', views.doctor_list, name='doctor_list'),
    # url(r'^listp/', views.patient_list, name='patient_list'),


]