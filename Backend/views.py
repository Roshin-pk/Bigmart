from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from webapp.models import contact_db
from django.contrib import messages

from Backend.models import category_db, Product_db


# Create your views here.
def home_page(rqst):
    return render(rqst,'index.html')
def category_page(rqst):
    return render(rqst,'category.html')
def save_category(rqst):
    if rqst.method=="POST":
        cn=rqst.POST.get('categoryname')
        d=rqst.POST.get('description')
        pic=rqst.FILES['img']
        obj=category_db(CategoryName=cn,Description=d,CategoryPhoto=pic)
        obj.save()
        messages.success(rqst,"Category saved successfully...!")
        return redirect(category_page)
def display_ctgry(rqst):
    data=category_db.objects.all()
    return render(rqst,'display_category.html',{'data':data})

def edit_category(rqst,cid):
    data=category_db.objects.get(id=cid)
    return render(rqst,'edit_category.html',{'data':data})
def update_category(rqst,cid):
    if rqst.method=="POST":
        cn = rqst.POST.get('categoryname')
        d = rqst.POST.get('description')
        try:
            img = rqst.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=cid).CategoryPhoto
        category_db.objects.filter(id=cid).update(CategoryName=cn,Description=d,CategoryPhoto=file)
        messages.success(rqst,'Updated successfully...!')
        return redirect(display_ctgry)
def drop_category(rqst,cid):
    d=category_db.objects.filter(id=cid)
    d.delete()
    messages.success(rqst,'Deleted successfully...!')
    return redirect(display_ctgry)
def login_page(rqst):
    return render(rqst,'login.html')

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,'Welcome...')
                return redirect(home_page)
            else:
                messages.error(request,'Invalid Password or Username ')
                return redirect(login_page)
        else:
            messages.warning(request,'User is not found')
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,'Have a Good Day')
    return redirect(login_page)

def products(rqst):
    data = category_db.objects.all()
    return render(rqst,'products.html',{'data':data})

def save_products(rqst):
    if rqst.method=='POST':
        cs=rqst.POST.get('categoryselect')
        pn=rqst.POST.get('productname')
        pp=rqst.POST.get('productprice')
        pd=rqst.POST.get('productdescription')
        ppic=rqst.FILES['pimg']
        obj=Product_db(CategorySelect=cs,ProductName=pn,ProductPrice=pp,Description=pd,ProductPhoto=ppic)
        obj.save()
        messages.success(rqst,'Product saved successfully...!')
        return redirect(products)

def display_prod(rqst):
    data=Product_db.objects.all()
    return render(rqst,'display_prod.html',{'data':data})
def edit_prod(rqst,pid):
    pr_data=Product_db.objects.get(id=pid)
    data=category_db.objects.all()
    return render(rqst,'edit_prod.html',{'data':pr_data,'x':data})
def update_prod(rqst,pid):
    if rqst.method=="POST":
        cs=rqst.POST.get('categoryselect')
        pn=rqst.POST.get('productname')
        pp=rqst.POST.get('productprice')
        pd=rqst.POST.get('description')
        try:
            img = rqst.FILES['pimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Product_db.objects.get(id=pid).ProductPhoto
        Product_db.objects.filter(id=pid).update(CategorySelect=cs,ProductName=pn,ProductPrice=pp,Description=pd,ProductPhoto=file)
        messages.success(rqst,'Updated successfully..!')
        return redirect(display_prod)

def drop_product(rqst,pid):
    d= Product_db.objects.filter(id=pid)
    d.delete()
    messages.success(rqst,'Deleted successfully..!')
    return redirect(display_prod)
def contacts_data(rqst):
    cont=contact_db.objects.all()
    return render(rqst,'contact_details.html',{'cont':cont})
def drop_contact(rqst,coid):
    d= contact_db.objgects.filter(id=coid)
    d.delete()
    return redirect(contacts_data)