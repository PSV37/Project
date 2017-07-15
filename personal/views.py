from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Product
from django.views.generic import View
from .forms import UserFoms
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
	return render(request,'personal/Home.html')

def Home(request):
    return render(request,'personal/index.html')	

def About(request):
    return render(request,'personal/About.html')

def Contact(request):
    return render(request , 'personal/Contact.html')

def Image(request):
    return render(request , 'personal/img.html')     

 
class ProductCreate(CreateView):
    model = Product
    fields = ['product_name','product_price','product_date','product_image']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['product_name','product_price','product_date','product_image']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('add-register')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
      

class  UserFormView(View):
    form_class = UserFoms
    template_name = 'personal/Registration_form.html'

    #display balnk form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

     #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

        if form.is_valid():

           user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()


           user = authenticate(username=username , password=password)

           if user is not None:

              if user.is_active:
                 login(request,user)
                 return  render('index')

        return render(request, self.template_name, {'form': form})
