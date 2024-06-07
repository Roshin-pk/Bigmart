from django.urls import path
from webapp import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('about/',views.AboutPage,name='about'),
    path('contact/',views.ContactPage,name='contact'),
    path('urproducts/',views.Our_prod,name='urproducts'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('prod_filtered/<cat_name>',views.prod_filtered,name='prod_filtered'),
    path('Single_product/<int:pro_id>/',views.Single_product,name='Single_product'),
    path('register_page',views.register_page,name='register_page'),
    path('save_register',views.save_register,name='save_register'),
    path('User_Login_page',views.User_Login_page,name='User_Login_page'),
]