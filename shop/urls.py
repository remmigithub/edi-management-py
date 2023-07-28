from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    

    path("", views.index, name="index"),

    path("add_cart/<int:myid>/", views.add_cart, name="add_cart"),
    path("update_cart/<int:myid>/<oper>/", views.update_cart, name="update_cart"),  

    path("search/", views.search, name="search"), 
    
   
    path("products/<int:myid>", views.productView, name="ProductView"),

    path("checkout/", views.checkout, name="Checkout"),

    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),

    path("<cat_name>/", views.shop, name="home"),

   
]