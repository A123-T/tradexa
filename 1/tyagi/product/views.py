from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from .models import producti
from django.contrib.auth import authenticate
def abhinav(request):
    messages.success(request, '  Welcome to Product App ...') 
    if request.method == "POST":
        name = request.POST['name']   
        weight = request.POST['weight']   
        price = request.POST['price']  
        if len(name)<3 or len(weight)<0 or price=="":
            messages.error(request, '  Please fill the form Correctly.') 
        else:         
            pr = producti(name = name, weight = weight, price= price)
            pr.save()
            messages.info(request, '  success fully created.')
            return HttpResponseRedirect('/product/show/') 

            
    else:
        return render(request,'product.html')
        
def show_data(request):
        ab = producti.objects.all()
        return render(request,'sh.html',{'post_value':ab})

def modify123(request,id):
    if request.method == 'POST':
            name1 = request.POST.get('name')
            price1 = request.POST.get('price')
            weight1 = request.POST.get('weight')
            ab = producti.objects.get(id = id)
            ab.name = name1
            ab.price = price1
            ab.weight = weight1
            import datetime
            ab.updated_at = datetime.datetime.now()
            ab.save()
            messages.success(request,'YOU HAVE SUCCESSUFULLY UPDATED THE POST')
            return HttpResponseRedirect('/product/show/')
    else :
        ab = producti.objects.get(id = id)

        return render(request,'modefy2.html',{'fm':ab,'nam':'Productapp_Modefied_Form'})
        
         