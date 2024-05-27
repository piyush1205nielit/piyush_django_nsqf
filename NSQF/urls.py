from django.contrib import admin
from django.urls import path,include
from employee.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', save_data, name='save_data'),
    path('download_report/',download_report,name='download_report'),
    path('',index),
    path('logout/',Logout),
    path('admin_login',admin_login,name='admin_login'),
    path('admin_home',admin_home,name='admin_home'),
    path('change_passwordadmin',change_passwordadmin,name='change_passwordadmin'),
    path('all_employee',all_employee, name='all_employee'),
    path('display_data/',display_data,name='display_data'),
    path('nielitheader/',nielitheader,name='nielitheader'),
    ]