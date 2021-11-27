from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.loginpage,name='loginpage'),
    url(r'^loginpage',views.loginpage,name='loginpage'),
    url(r'^admin_inherit',views.admin_inherit,name='admin_inherit'),
    url(r'^dashboard_control',views.dashboard_control,name='dahboard_control'),
    url(r'^validate_user',views.validate_user,name='validate_user'),
    url(r'^add_subject',views.add_subject,name='add_subject'),
    url(r'^create_subject',views.create_subject,name='create_subject'),
    url(r'^subject_show',views.subject_show,name='subject_show'),
    url(r'^class_add',views.class_add,name='class_add'),
    url(r'^Add_class',views.Add_class,name='Add_class'),
    url(r'delete_class/(?P<id>\d+)$',views.delete_class,name='delete_class'),
    url(r'^class_show',views.class_show,name='class_show'),
    url(r'^data_form',views.data_form,name='data_form'),
    url(r'deletesubject/(?P<id>\d+)$',views.deletesubject,name='deletesubject'),
    url(r'^upload_pdf',views.upload_pdf,name='upload_pdf'),
    url(r'^upload_data',views.upload_data,name='upload_data'),
    url(r'^delete_data_pdf/(?P<id>\d+)$',views.delete_data_pdf,name='delete_data_pdf'),
]