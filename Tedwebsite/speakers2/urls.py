from django.urls import path
from . import views

urlpatterns = [
    path('', views.speakers_home, name='speakers_home'),
    path('/speakers.html', views.speakers_home),
    path('/form2.html', views.nominate_yourself),
    path('/blog.html', views.blogs),
    path('/about_us.html', views.about_us),
    path('/contact.html', views.contact),

    
    
    path('/about_us.html/Titiksha', views.memberDesc1, name='member_description1'),
    path('/about_us.html/kavin', views.memberDesc2, name='member_description2'),
    path('/about_us.html/Abhiram', views.memberDesc3, name='member_description3'),
    path('/about_us.html/Shashank', views.memberDesc4, name='member_description4'),
    path('/about_us.html/Sreelakshmi', views.memberDesc5, name='member_description5'),
    path('/about_us.html/Nandini', views.memberDesc6, name='member_description6'),
    path('/about_us.html/Abhinav', views.memberDesc7, name='member_description7'),
    path('/about_us.html/Amey_Varhade', views.memberDesc8, name='member_description8'),
    path('/about_us.html/Anindya_Rajan', views.memberDesc9, name='member_description9'),
    path('/about_us.html/Anisha_Khati', views.memberDesc10, name='member_description10'),
    path('/about_us.html/Anushka', views.memberDesc11, name='member_description11'),
    path('/about_us.html/Vamsi', views.memberDesc12, name='member_description12'),
    path('/about_us.html/Anushka_Srivastava', views.memberDesc13, name='member_description13'),
    path('/about_us.html/Arpita_Mohapatra', views.memberDesc14, name='member_description14'),
    path('/about_us.html/Ayush_Srivastava', views.memberDesc15, name='member_description15'),
    path('/about_us.html/Digisha_Verma', views.memberDesc16, name='member_description16'),
    path('/about_us.html/Emily_Huiling', views.memberDesc17, name='member_description17'),
    path('/about_us.html/Abhiram', views.memberDesc18, name='member_description18'),
    path('/about_us.html/Govind_Singh', views.memberDesc19, name='member_description19'),
    path('/about_us.html/Jaideep_Buksagarmath', views.memberDesc20, name='member_description20'),
    path('/about_us.html/Janhavi_Lande', views.memberDesc21, name='member_description21'),
    path('/about_us.html/Lalika_Laya_K', views.memberDesc22, name='member_description22'),
    path('/about_us.html/Kavin', views.memberDesc23, name='member_description23'),
    path('/about_us.html/Monalisha_Majumder', views.memberDesc24, name='member_description24'),
    path('/about_us.html/Niladri_Sarkar', views.memberDesc25, name='member_description25'),
    path('/about_us.html/Nishant', views.memberDesc26, name='member_description26'),
    path('/about_us.html/Nishtha_Sharma', views.memberDesc27, name='member_description27'),
    path('/about_us.html/Pragnya_Ramjee', views.memberDesc28, name='member_description28'),
    path('/about_us.html/Pratyanshu_Raj_Singh', views.memberDesc29, name='member_description29'),
    path('/about_us.html/Ritik_Singh', views.memberDesc30, name='member_description30'),
    path('/about_us.html/Sai_Sreyas_Ray', views.memberDesc31, name='member_description31'),
    path('/about_us.html/Shatakshi_Kaushal', views.memberDesc32, name='member_description32'),
    path('/about_us.html/Shiva_Sah', views.memberDesc33, name='member_description33'),
    path('/about_us.html/Sudarshan_Birla', views.memberDesc34, name='member_description34'),
    path('/about_us.html/Titiksha', views.memberDesc35, name='member_description35'),
]




