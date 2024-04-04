from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import update_amount
urlpatterns = [
    path("",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\index\\index.html"), name = "index"),
    path("teachers/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\schools\\schools.html"), name = "teachers"),    
    path('students/', views.student_detail, name='student_detail'),
    path("parents/",views.parents, name = "parents"),
    path("balance/", views.balance, name="balance"),    
    path("parental_manage/",views.manageP, name = "manage(P)"),
    path("school_manage/",views.manageS, name = "manage(S)"),
    path("menu/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\menu\\menu.html"), name = "menu"),
    path("menu-schools/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\menu_S\\menu_S.html"), name = "menu_S"),
    path("payNow/",views.payNow, name = "payNow"),
    path("quick-top-up/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\qTopUp\\qTopUp.html"), name = "qTopUp"),
    path("reserve/", views.reserve , name = "reserve"),
    path("student-details/",views.sDetails, name = "sDetails"),
    path("statistics/",views.stats, name = "stats"),
    path('update_amount/', views.update_amount, name='update_amount'),
    path("register/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\register\\register.html"), name = "register"),
    path('register_1/', views.register_1, name='register_1'),
    path('editDetails/',views.editDetails , name = 'editDetails'),
    path('login/', views.login, name='login'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete_menu_item/<int:menu_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('student-details-editor/<int:student_id>/',views.sDetailsEditor , name = 'student_details_editor'),
    path("scanNow/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\scanNow\\scanNow.html"), name = "scanNow"),
    path('process_qr_code/', views.process_qr_code, name='process_qr_code'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('reserve_order/', views.reserve_order, name='reserve_order'),


]

