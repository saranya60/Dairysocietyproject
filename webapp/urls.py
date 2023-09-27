from django.urls import path, include
from webapp import views
urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('registerlogin/', views.registerlogin, name="registerlogin"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('saveregistration/', views.saveregistration, name="saveregistration"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('viewgal/', views.viewgal, name="viewgal"),
    path('singleprod/<int:pid>/', views.singleprod, name="singleprod"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('allproducts/', views.allproducts, name="allproducts"),
    path('viewcart/', views.viewcart, name="viewcart"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),
    path('placeorder/', views.placeorder, name="placeorder"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('sendmsg/', views.sendmsg, name="sendmsg"),
    path('myorders/', views.myorders, name="myorders"),
]