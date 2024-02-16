from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import update_amount
urlpatterns = [
    path("",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\index\\index.html"), name = "index"),
    path("schools/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\school\\schools.html"), name = "teachers"),    
    path('students/', views.student_detail, name='student_detail'),
    path("parents/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\parents\\parents.html"), name = "parents"),
    path("balance/", views.balance, name="balance"),    path("parental_manage/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\manage(P)\\manage(P).html"), name = "manage(P)"),
    path("school_manage/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\manage(S)\\manage(S).html"), name = "manage(S)"),
    path("menu/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\menu\\menu.html"), name = "menu"),
    path("menu-schools/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\menu_S\\menu_S.html"), name = "menu_S"),
    path("payNow/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\payNow\\payNow.html"), name = "payNow"),
    path("quick-top-up/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\qTopUp\\qTopUp.html"), name = "qTopUp"),
    path("reserve/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\reserve\\reserve.html"), name = "reserve"),
    path("student-details/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\sDetails\\sDetails.html"), name = "sDetails"),
    path("statistics/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\stats\\stats.html"), name = "stats"),
    path('update_amount/', update_amount, name='update_amount'),
    path("register/",TemplateView.as_view(template_name = "C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\register\\register.html"), name = "register"),
    path('register_1/', views.register_1, name='register_1'),
    path('login/', views.login, name='login'),
]

