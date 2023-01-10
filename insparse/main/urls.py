from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inspections', views.detail, name='inspections_list'),
    # ex: /incpection/5/
    path('inspection/<int:insp_id>/', views.detail, name='detail'),  
]
