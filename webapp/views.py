from django.shortcuts import render, redirect

from Backend.models import Product_db,category_db
from webapp.models import contact_db, Register_db
from django.contrib import messages


# Create your views here.
def HomePage(rqst):
    cat = category_db.objects.all()
    return render(rqst,'Home.html',{'cat':cat})
def AboutPage(rqst):
    cat = category_db.objects.all()
    return render(rqst,'about.html',{'cat':cat})
def ContactPage(rqst):
    cat = category_db.objects.all()
    return  render(rqst,'contacts.html',{'cat':cat})
def Our_prod(rqst):
    pro= Product_db.objects.all()
    cat = category_db.objects.all()
    return render(rqst,'our_products.html',{'pro':pro,'cat':cat})
def save_contact(rqst):
    if rqst.method=="POST":
        nm=rqst.POST.get('name')
        em=rqst.POST.get('email')
        subj=rqst.POST.get('sub')
        msgs=rqst.POST.get('msg')
        obj=contact_db(Name=nm,Email=em,Subject=subj,Message=msgs)
        obj.save()
        return redirect(ContactPage)
def prod_filtered(rqst,cat_name):
    data = Product_db.objects.filter(CategorySelect=cat_name)
    cat = category_db.objects.all()
    return render(rqst,'Product_filtered.html',{'data':data,'cat':cat})


def Single_product(rqst,pro_id):
    data=Product_db.objects.get(id=pro_id)
    cat = category_db.objects.all()
    return render(rqst,'single_product.html',{'data':data,'cat':cat})

def register_page(rqst):
    return render(rqst,'Register.html')
def save_register(rqst):
    if rqst.method=="POST":
        un=rqst.POST.get('Usrename')
        em=rqst.POST.get('email')
        psw=rqst.POST.get('password')
        obj=Register_db(UserName=un,Email=em,Password=psw)
        if Register_db.objects.filter(UserName=un).exists():
            messages.warning(rqst,'Username is already Exist...! ')
        elif Register_db.objects.filter(Email=em).exists():
            messages.warning(rqst,'Email is already Exists...!')
        else:
            obj.save()
            return redirect(User_Login_page)
def User_Login_page(rqst):
    return render(rqst,'userlogin.html')


