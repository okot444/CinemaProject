"""Kursach URL Configuration
"""
from django.contrib import admin
from django.urls import path
from Kursach import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path(r'^film', views.film,name='film'),
    path('timetable', views.timetable, name='table'),
    path('contacts', views.contacts, name='table'),
    path('login', views.login,name='login'),
path(r'^edit', views.edit, name='edit'),
    path(r'^editFilms', views.films, name='films'),
    path(r'^editTable', views.table, name='Etable'),
    path(r'^addRow', views.add, name="add"),
    path(r'^addFilm', views.addFilm, name="addFilm"),
    path(r'^EDFilm', views.EDFilm, name="EDFilm"),
    path(r'^delFilm', views.delFilm, name="delFilm"),
    path(r'^EDTable', views.EDTable, name="EDTable"),
    path(r'^delTable', views.delTable, name="delTable"),
path(r'^DelDate', views.DelDate, name="DelDate"),
path(r'^AddDate', views.AddDate, name="AddDate")
]
''' ,
    
    
    
    
    
    path(r'^EditUser', views.EditUser, name="EditUser"),
    path(r'^AddUser', views.AddUser, name="AddUser"),
    path(r'^DelUser', views.DelUser, name="DelUser"),
    ,
    

'''