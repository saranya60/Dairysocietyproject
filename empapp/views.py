
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from adminapp.models import employeedb, orderdb
from empapp.models import productdb,customerdb, salesdb, billdb, pricechart,milkdb, invoicedb
from adminapp.models import farmerdb
# Create your views here.


def emploginpage(req):
    return render(req, "emplogin.html")
def employeelogin(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        pwd = req.POST.get('password')
        if employeedb.objects.filter(Empname=uname, Mobile=pwd, Designation="Milk Collector").exists():
            req.session['Empname'] = uname
            req.session['Mobile'] = pwd
            messages.success(req, "Log In Successfully....!")
            return redirect(mchome)
        elif employeedb.objects.filter(Empname=uname, Mobile=pwd, Designation="Sales Manager").exists():
            req.session['Empname'] = uname
            req.session['Mobile'] = pwd
            messages.success(req, "Log In Successfully....!")
            return redirect(saleshome)

        else:
            messages.success(req, "Invalid Username or Password....!")
            return redirect(emploginpage)
    messages.success(req, "Invalid Username or Password....!")
    return redirect(emploginpage)


def emplogout(request):
    del request.session['Empname']
    del request.session['Mobile']
    messages.success(request, "Logout Successfully....!")
    return redirect(emploginpage)

def mchome(req):
    data = pricechart.objects.all()
    return render(req, "milkcollectorhome.html", {'data': data})
def saleshome(req):
    return render(req, "saleshome.html")
def addproduct(req):
    return render(req, "addproduct.html")
def saveproduct(req):
    if req.method == "POST":
        prd = req.POST.get('product')
        ds = req.POST.get('desc')
        pr = req.POST.get('price')
        im = req.FILES['image']
        obj = productdb(Product=prd, Description=ds, Price=pr, Image=im)
        obj.save()
        messages.success(req, "Product Saved Successfully....!")
        return redirect(addproduct)
def dispproduct(req):
    data = productdb.objects.all()
    return render(req, "displayproduct.html", {'data':data})
def editproduct(req, dataid):
    data = productdb.objects.get(id=dataid)
    return render(req, "editprod.html", {'data':data})
def deleteproduct(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Product Deleted Successfully....!")
    return redirect(dispproduct)
def updateproduct(req, dataid):
    if req.method =="POST":
        ds = req.POST.get('desc')
        prd = req.POST.get('product')
        pr = req.POST.get('price')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Product=prd, Description=ds, Price=pr, Image=file)
        messages.success(req, "Product Updated Successfully....!")
        return redirect(dispproduct)
def customer(req):
    return render(req, "addcustomer.html")
def savecustomer(req):
    if req.method == "POST":
        cs = req.POST.get('customer')
        pl = req.POST.get('place')
        mob = req.POST.get('mobile')
        obj = customerdb(Customer=cs, Place=pl, Mobile=mob)
        obj.save()
        messages.success(req, "Customer Saved Successfully....!")
        return redirect(customer)
def sales(req):
    cus = customerdb.objects.all()
    prd = productdb.objects.all()
    return render(req, "salesrecord.html", {'prd': prd, 'cus': cus})

def savesales(req):
    if req.method == "POST":
        dt = req.POST.get('date')
        cs = req.POST.get('customer')
        pr = req.POST.get('product')
        prc = req.POST.get('sprice')
        qt = req.POST.get('quantity')
        tot = req.POST.get('total')
        obj = salesdb(Product=pr, Quantity=qt, Customer=cs, Price=prc, Total=tot)
        obj.save()
        messages.success(req, "Data Saved Successfully....!")
        data = salesdb.objects.filter(Date=dt, Customer=cs)
        totalprice = 0
        for i in data:
            totalprice = totalprice + i.Total
        if billdb.objects.filter(Date=dt, Customer=cs, Total=totalprice).exists():
            messages.warning(req, "Already Recorded...!")
        else:
            if billdb.objects.filter(Date=dt, Customer=cs).exists():
                billdb.objects.filter(Date=dt, Customer=cs).update(Total=totalprice)
                messages.success(req, "Data Added Successfully....!")
                return redirect(sales)
            else:
                obj = billdb(Customer=cs, Total=totalprice)
                obj.save()
                messages.success(req, "Data Added Successfully....!")
                return redirect(sales)
        return redirect(sales)



def viewsalesrecord(req):
    sales = salesdb.objects.all()
    return render(req, "viewsales.html", {'sales':sales})
def salebill(req):
    cs = customerdb.objects.all()
    return render(req, "salesbill.html", {'cs':cs})
def billview(req):

        dt = req.POST.get('date1')
        cs = req.POST.get('customer')
        data = salesdb.objects.filter(Date=dt, Customer=cs)

        totalprice = 0
        for i in data:
            totalprice = totalprice + i.Total

        return render(req, "viewbill.html", {'data':data, 'dt':dt, 'cs':cs, 'totalprice':totalprice})

def savebill(req):
    if req.method == "POST":
        dt = req.POST.get('date1')
        cs = req.POST.get('customer')
        tot = req.POST.get('totalprice')

        if billdb.objects.filter(Date=dt, Customer=cs, Total=tot).exists():
            messages.warning(req, "Already Recorded...!")
        else:
            if billdb.objects.filter(Date=dt, Customer=cs).exists():
                billdb.objects.filter(Date=dt, Customer=cs).update(Total=tot)
                messages.success(req, "Updated Successfully....!")
                return redirect(sales)
            else:
                obj = billdb(Customer=cs, Total=tot)
                obj.save()
                messages.success(req, "Recorded Successfully....!")
                return redirect(sales)
        return redirect(sales)



def addpricechart(req):
    return render(req, "pricechart.html")
def savepc(req):
    if req.method == "POST":
        fat = req.POST.get('fat')
        snf = req.POST.get('snf')
        rate = req.POST.get('rate')
        obj = pricechart(fat=fat, snf=snf, rate=rate)
        obj.save()
        messages.success(req, "Data Added Successfully....!")
        return redirect(addpricechart)

def milkcollection(req):
    data = farmerdb.objects.all()
    return render(req, "milkcollect.html", {'data':data})
def savemc(req):
    if req.method == "POST":
        dt = req.POST.get('date1')
        far = req.POST.get('farmer')
        ml = req.POST.get('milk')
        if milkdb.objects.filter(Date=dt, Farmer=far).exists():
            messages.warning(req, "Record Already Saved....!")
            return redirect(milkcollection)
        else:
            obj = milkdb(Farmer=far, Milk=ml)
            obj.save()
            return redirect(milkcollection)
def milktest(req):
    data = farmerdb.objects.all()
    return render(req, "testresult.html", {'data':data})
def savetest(req):
    if req.method == "POST":
        dt = req.POST.get('date1')
        far = req.POST.get('farmer')
        fat = req.POST.get('fat')
        snf = req.POST.get('snf')

        prc = pricechart.objects.filter(fat=fat, snf=snf)

        for i in prc:
            rate = i.rate
        milkdb.objects.filter(Date=dt, Farmer=far).update(FAT=fat, SNF=snf, Rate=rate)

        mk = milkdb.objects.filter(Date=dt, Farmer=far)
        for d in mk:
            tot = d.Milk * d.Rate
        milkdb.objects.filter(Date=dt, Farmer=far).update(Totalrate=tot)
        messages.success(req, "Data Recorded Successfully....!")
        cn = farmerdb.objects.filter(Name=far)
        return render(req, "totalrate.html", {'prc':prc, 'mk':mk, 'cn':cn, 'dt':dt, 'far':far})
def savetotal(req):
    if req.method == "POST":
        dt = req.POST.get('date1')
        far = req.POST.get('farmer')
        rt = req.POST.get('rate')
        tot = req.POST.get('total')
        milkdb.objects.filter(Date=dt, Farmer=far).update(Rate=rt, Totalrate=tot)
        return redirect(milktest)
def totalbill(req):
    data = billdb.objects.all()
    return render(req, "billdata.html", {'data':data})
def customerview(req):
    cus = customerdb.objects.all()
    return render(req, "viewcustomer.html", {'cus':cus})
def editcustomer(req, dataid):
    data = customerdb.objects.get(id=dataid)
    return render(req, "editcust.html", {'data':data})
def dltcustomer(req, dataid):
    data = customerdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Customer Deleted Successfully....!")
    return redirect(customerview)
def updatecustomer(req, dataid):
    if req.method =="POST":
        cs = req.POST.get('customer')
        pl = req.POST.get('place')
        mob = req.POST.get('mobile')

        customerdb.objects.filter(id=dataid).update(Customer=cs, Place=pl, Mobile=mob)
        messages.success(req, "Customer Data Updated Successfully....!")
        return redirect(customerview)
def milkrecordview(req):
    data = milkdb.objects.all()
    return render(req, "viewmilkrecord.html", {'data': data})
def milkview(req):
    far = farmerdb.objects.all()
    return render(req, "viewmilk.html", {'far':far})
def viewbydatemilk(req):
    if req.method == "POST":
        dt = req.POST.get('dt1')
        data = milkdb.objects.filter(Date=dt)
        return render(req, "viewmilkdate.html", {'data': data, 'dt':dt})
def viewbyfarmer(request):
    if request.method == "POST":
        sd = request.POST.get('dt1')
        ed = request.POST.get('dt2')
        fr = request.POST.get('name')

        data = milkdb.objects.filter(Date__range=(sd, ed), Farmer=fr)
        return render(request, "viewbyfarm.html", {'data': data, 'fr': fr, 'sd': sd, 'ed': ed})
def viewsalesdate(req):
    if req.method == "POST":
        dt = req.POST.get('date')
        data = salesdb.objects.filter(Date=dt)
        return render(req, "viewsalesdt.html", {'data':data})
def viewdaysales(req):
    return render(req, "daysales.html")
def viewsalesday(req):
    if req.method == "POST":
        dt = req.POST.get('date')
        data = billdb.objects.filter(Date=dt)
        totalprice = 0
        for i in data:
            totalprice = totalprice + i.Total
        if invoicedb.objects.filter(Date=dt, Total=totalprice).exists():
            messages.success(req, "today Income....!")

        else:
            if invoicedb.objects.filter(Date=dt).exists():
                invoicedb.objects.filter(Date=dt).update(Total=totalprice)


            else:
                obj = invoicedb(Total=totalprice)
                obj.save()



        return render(req, "viewsaleday.html", {'data':data, 'totalprice':totalprice})

def viewpc(req):
    data = pricechart.objects.all()
    return render(req, "viewpricechart.html", {'data': data})
def pcdlt(req, dataid):
    data = pricechart.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Data Deleted Successfully....!")
    return redirect(viewpc)
def salerange(req):
    return render(req, "viewsalesrange.html")
def incomerange(request):
    if request.method == "POST":
        sd = request.POST.get('dt1')
        ed = request.POST.get('dt2')
        data = invoicedb.objects.filter(Date__range=(sd, ed))
        total = 0
        for i in data:
            total = total + i.Total
        return render(request, "income.html", {'data': data, 'sd': sd, 'ed': ed, 'total':total})
def orderspage(req):
    data = orderdb.objects.all()
    return render(req, "empvieworders.html", {'data':data})
def savestatus(request, dataid):
    if request.method == "POST":
        sd = request.POST.get('status')
        na = request.POST.get('name')
        ad = request.POST.get('address')
        tot = request.POST.get('total')
        mob = request.POST.get('mobile')
        dt = request.POST.get('date')
        data = salesdb.objects.filter(Date=dt, Customer=na)
        totalprice = 0
        for i in data:
            totalprice = totalprice + i.Total
        orderdb.objects.filter(id=dataid).update(Status=sd)
        messages.success(request, "Status Saved Successfully....!")
        if orderdb.objects.filter(Status='Delivered'):
            if billdb.objects.filter(Date=dt, Customer=na, Total=tot).exists():
                messages.warning(request, "Already Recorded...!")
            else:
                if billdb.objects.filter(Date=dt, Customer=na).exists():
                    billdb.objects.filter(Date=dt, Customer=na).update(Total=totalprice)
                    messages.success(request, "Status Saved Successfully....!")
                    return redirect(orderspage)
                else:
                    obj = billdb(Customer=na, Total=tot)
                    obj.save()
                    messages.success(request, "Recorded Successfully....!")
                    return redirect(orderspage)
            if customerdb.objects.filter(Customer=na).exists():
                messages.success(request, "Status Saved Successfully....!")
            else:
                obj = customerdb(Customer=na, Place=ad, Mobile=mob)
                obj.save()
                messages.success(request, "Status Saved Successfully....!")

        return redirect(orderspage)
def amount(req):
    far = farmerdb.objects.all()
    return  render(req, "monthamount.html", {'far':far})
def calculateamount(request):
    if request.method == "POST":
        sd = request.POST.get('dt1')
        ed = request.POST.get('dt2')
        fr = request.POST.get('name')

        data = milkdb.objects.filter(Date__range=(sd, ed), Farmer=fr)
        totalprice = 0
        for i in data:
            totalprice = totalprice + i.Totalrate
        return render(request, "farmeramount.html", {'data': data, 'fr': fr, 'sd': sd, 'ed': ed, 'totalprice':totalprice})