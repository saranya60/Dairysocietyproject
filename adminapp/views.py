from datetime import datetime

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from adminapp.models import employeedb, postdb, farmerdb, attendancedb,imagedb, orderdb, messagedb
from empapp.models import salesdb, milkdb, billdb
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Create your views here.
def adminpage(request):
    far = farmerdb.objects.all()
    data = employeedb.objects.all()
    return render(request, "adminhome.html", {'data':data, 'far':far})

def emppage(req):
    des = postdb.objects.all()
    return render(req, "addemployee.html", {'des':des})
def saveemployee(req):
    if req.method == "POST":
        na = req.POST.get('empname')
        ds = req.POST.get('desg')
        ad = req.POST.get('adrs')
        dob = req.POST.get('dob')
        gr = req.POST.get('gender')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        sal = req.POST.get('salary')
        im = req.FILES['simage']
        obj = employeedb(Empname=na, Designation=ds, Address=ad, Dateofbirth=dob, Gender=gr, Mobile=mob, Email=em, Salary=sal, Image=im)
        obj.save()
        messages.success(req, "Employee Registered Successfully....!")
        return redirect(emppage)
def empdisplay(req):
    data = employeedb.objects.all()
    return render(req, "display_emp.html", {'data':data})
def designation(req):
    return render(req, "addpost.html")
def savepost(req):
    if req.method == "POST":
        ds = req.POST.get('desg')
        obj = postdb(Designation=ds)
        obj.save()
        messages.success(req, "Designation Registered Successfully....!")
        return redirect(designation)
def postdisplay(req):
    data = postdb.objects.all()
    return render(req, "displaypost.html", {'data':data})

def farmerpage(req):
    return render(req, "addfarmer.html")

def savefarmer(req):
    if req.method == "POST":
        cn = req.POST.get('card')
        na = req.POST.get('name')
        ad = req.POST.get('adrs')
        dob = req.POST.get('dob')
        gr = req.POST.get('gender')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        im = req.FILES['fimage']
        obj = farmerdb(Cardno=cn, Name=na, Address=ad, Dateofbirth=dob, Gender=gr, Mobile=mob, Email=em, Image=im)
        obj.save()
        messages.success(req, "Farmer Registered Successfully....!")
        return redirect(farmerpage)

def editemp(req, dataid):
    des = postdb.objects.all()
    emp = employeedb.objects.get(id=dataid)
    return render(req, "editemployee.html", {'emp':emp, 'des':des})
def empupdate(req, dataid):
    if req.method == "POST":
        na = req.POST.get('empname')
        ds = req.POST.get('desg')
        ad = req.POST.get('adrs')
        dob = req.POST.get('dob')
        gr = req.POST.get('gender')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        sal = req.POST.get('salary')

        try:
            im = req.FILES['simage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = employeedb.objects.get(id=dataid).Image
        employeedb.objects.filter(id=dataid).update(Empname=na, Designation=ds, Address=ad, Dateofbirth=dob, Gender=gr,
                                                    Mobile=mob, Email=em, Salary=sal, Image=file)
        messages.success(req, "Data Updated Successfully....!")
        return redirect(empdisplay)
def empdelete(req, dataid):
    data = employeedb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Employee Deleted Successfully....!")
    return redirect(empdisplay)
def loginpage(req):
    return render(req, "adminlogin.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Log In Successfully....!")
                request.session['username']=uname
                request.session['password']=pwd
                return redirect(adminpage)
            else:
                messages.success(request, "Invalid Username or Password....!")
                return redirect(loginpage)
        else:
            messages.success(request, "Invalid Username or Password....!")
            return redirect(loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully....!")
    return redirect(loginpage)
def empdata(req):
    data = employeedb.objects.all()
    return render(req, "employeedata.html", {'data':data})

def dispfarmer(req):
    data = farmerdb.objects.all()
    return render(req, "displayfarmer.html", {'data':data})

def editfarmer(req, dataid):
    far = farmerdb.objects.get(id=dataid)
    return render(req, "editfarmer.html", {'far':far})
def farmerupdate(req, dataid):
    if req.method == "POST":
        cn = req.POST.get('card')
        na = req.POST.get('name')
        ad = req.POST.get('adrs')
        dob = req.POST.get('dob')
        gr = req.POST.get('gender')
        mob = req.POST.get('mobile')
        em = req.POST.get('email')
        try:
            im = req.FILES['simage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = farmerdb.objects.get(id=dataid).Image
        farmerdb.objects.filter(id=dataid).update(Cardno=cn, Name=na, Address=ad, Dateofbirth=dob, Gender=gr,
                                                    Mobile=mob, Email=em, Image=file)
        messages.success(req, "Data Updated Successfully....!")
        return redirect(dispfarmer)
def farmerdelete(req, dataid):
    data = farmerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(dispfarmer)
def attendance(req):
    data = employeedb.objects.all()
    return render(req, "empattendance.html", {'data':data})
def saveatn(req):
    if req.method == "POST":
        dt = req.POST.get('date1')
        na = req.POST.get('name')
        at = req.POST.get('atn')
        if attendancedb.objects.filter(Date=dt, Empname=na).exists():
            messages.warning(req, "Record Already Exists....!")
            return redirect(attendance)
        else:
            obj = attendancedb(Empname=na, Attendance=at)
            obj.save()
            messages.success(req, "Attendance Recorded Successfully....!")
            return redirect(attendance)
def viewatn(req):
    emp = employeedb.objects.all()
    atn = attendancedb.objects.all()

    return render(req, "viewattendance.html", {'atn':atn, 'emp':emp})
def editpost(req, dataid):
    des = postdb.objects.get(id=dataid)
    return render(req, "editpost.html", {'des':des})
def postupdate(req, dataid):
    if req.method == "POST":
        ds = req.POST.get('desg')
        postdb.objects.filter(id=dataid).update(Designation=ds)
        messages.success(req, "Data Updated Successfully....!")
        return redirect(postdisplay)
def postdelete(req, dataid):
    data = postdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Data Deleted Successfully....!")
    return redirect(postdisplay)
def viewbydate(request):
    if request.method=="POST":
        sd = request.POST.get('dt1')
        ed = request.POST.get('dt2')
        emp = request.POST.get('ename')
        prs = attendancedb.objects.filter(Date__range=(sd, ed), Empname=emp, Attendance="Present")
        rows = prs.count()
        date1 = attendancedb.objects.filter(Date__range=(sd, ed), Empname=emp)
        return render(request, "viewbydate.html", {'date1':date1, 'emp':emp, 'sd':sd, 'ed':ed, 'prs': prs, 'rows':rows})
def viewbyemp(req):
    if req.method=="POST":
        

        emp = req.POST.get('ename')
        data = attendancedb.objects.filter(Empname=emp)
        return render(req, "viewbyemployee.html", {'data':data})
def viewallatn(req):
    atn = attendancedb.objects.all()
    return render(req, "viewatnall.html", {'atn':atn})
def viewfarmer(req):
    far = farmerdb.objects.all()
    return render(req, "farmerdata.html", {'far':far})
def atndelete(req, dataid):
    data = attendancedb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewallatn)
def imgupload(req):
    return render(req, "imageupload.html")
def saveimg(req):
    if req.method == "POST":
        im = req.FILES['image']
        obj = imagedb(Image=im)
        obj.save()
        messages.success(req, "Image Uploaded Successfully....!")
        return redirect(imgupload)
def viewimage(req):
    gal = imagedb.objects.all()
    return render(req, "gallery.html", {'gal':gal})
def dltimg(req, dataid):
    data = imagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewimage)
def orders(req):
    data = orderdb.objects.all()
    return render(req, "vieworders.html", {'data': data})
def adminsales(req):
    data = billdb.objects.all()
    return render(req, "salerecord.html", {'data': data})
def milkrecord(req):
    data = milkdb.objects.all()
    return render(req, "milkcollection.html", {'data': data})
def viewmsg(req):
    data = messagedb.objects.all()
    return render(req, "viewmessage.html", {'data':data})
