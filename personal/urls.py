from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from .models import Product

urlpatterns = [
    url(r'^$',views.index,name="index"),

    url(r'^Home/$',views.Home,name="home"),

    url(r'^About/$',views.About,name="about"),

    url(r'^Contact/$',views.Contact,name="contact"),

    url(r'^images/$',views.Image,name="img"),

    url(r'^Add/$', ListView.as_view(queryset=Product.objects.all()[:25],
	            template_name='personal/AddedProducts.html'),name="add-register"),

    url(r'^(?P<pk>[0-9]+)$',DetailView.as_view(model = Product,
         	template_name='personal/DetailProducts.html'),name="detail-pro"),

    url(r'^per/added/$',views.ProductCreate.as_view(),name="add-pro"),

    url(r'^edit/(?P<pk>[0-9]+)/$',views.ProductUpdate.as_view() , name="up-pro"),
    
    url(r'^delete/(?P<pk>[0-9]+)/delete/$',views.ProductDelete.as_view(), name="del-pro"),
  
    url(r'^register/$',views.UserFormView.as_view(),name="register"),

]