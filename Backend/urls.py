from django.urls import path
from Backend import views

urlpatterns = [
    path('home_page/',views.home_page,name='home_page'),
    path('category_page/',views.category_page,name='category_page'),
    path('save_category/',views.save_category,name='save_category'),
    path('display_ctgry/',views.display_ctgry,name='display_ctgry'),
    path('edit_category/<int:cid>/',views.edit_category,name='edit_category'),
    path('update_category/<int:cid>/',views.update_category,name='update_category'),
    path('drop_category/<int:cid>/',views.drop_category,name='drop_category'),
    path('login_page/',views.login_page,name='login_page'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('products/', views.products, name='products'),
    path('save_products/', views.save_products, name='save_products'),
    path('display_prod/', views.display_prod, name='display_prod'),
    path('edit_prod/<int:pid>/', views.edit_prod, name='edit_prod'),
    path('update_prod/<int:pid>/', views.update_prod, name='update_prod'),
    path('drop_product/<int:pid>/', views.drop_product, name='drop_product'),
    path('contacts_data/', views.contacts_data, name='contacts_data'),
    path('drop_contact/<int:coid>/', views.drop_contact, name='drop_contact'),
]