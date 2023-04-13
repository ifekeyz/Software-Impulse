from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages,auth
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout

from route.models import Bin, Stock,CustomUser

# Create your views here.
def index(request):
    return render(request,'screens/index.html')

def register(request):
    if request.method == 'POST':
    # Get from values
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        # check if passwords match
        if password == password2:

            # check Username
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('newstaff')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                    return redirect('newstaff')
                else:
                    # return


                    user = CustomUser.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    user.save()
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You have successfully added new staff')
                    return redirect('newstaff')

                    # user.save()
                    # messages.success(request, 'you are now registered and can log in')
                    # return redirect('login')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('newstaff')
    return render(request,'screens/staff.html')

def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('features')
       
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request,'screens/login.html')


def logout(request):
    auth_logout(request)
    messages.info(request, 'you are now logged out...come back soon')
    return redirect('login')

def features(request):
    return render(request,'screens/features.html')

def availabilty(request):
    queryset_list = Bin.objects.order_by('-id')
    stoke = Stock.objects.all()

    if 'code' and 'litre' in request.GET:
        code =  request.GET['code']
        litre =  request.GET['litre']
        if Bin.objects.filter(product_code = code, litre = litre):
            if code:
                queryset_list = queryset_list.filter(product_code__icontains = code, litre__icontains=litre)
        else:
            messages.error(request, f'{code} is not valid product code in the stock')
            return redirect('availabilty')


    return render(request,'screens/availabilty.html',{
        
    })

def singleqty(request):

    queryset_list = Bin.objects.order_by('-id')
    stoke = Stock.objects.all()

    if 'code' and 'litre' in request.GET:
        code =  request.GET['code']
        litre =  request.GET['litre']
        if Bin.objects.filter(product_code = code, litre = litre):
            if code:
                queryset_list = queryset_list.filter(product_code__icontains = code, litre__icontains=litre)
                messages.success(request, f'{code} is valid product code in the stock')
                
        else:
            messages.error(request, f'{code} is not valid product code in the stock')
            return redirect('availabilty')


    return render(request,'screens/availabilty.html',{
        'queryset_list':queryset_list
    })

    
def release_stoke(request):
    stoke = Stock()
    if request.method == 'POST':
        product_code = request.POST.get('code')
        color_type = request.POST.get('ctype')
        invoice_code = request.POST.get('icode')
        qty_issued  = request.POST.get('qty')
        litre = request.POST.get('litre')
        client_name = request.POST.get('cname')
        officer = request.POST.get('name')
        stock_keeper = request.POST.get('s_keper')

        if Bin.objects.filter(product_code = product_code):


            stoke.product_code = product_code
            stoke.color_type = color_type
            stoke.invoice_code = invoice_code
            stoke.qty_issued = qty_issued
            stoke.client_name = client_name
            stoke.litre = litre
            stoke.officer = officer
            stoke.stoke_keeper = stock_keeper
            stoke.qty_receieved = None
        
            stoke.save()


            messages.success(request, f'{qty_issued} quantities of {product_code} and {litre} product code request is successful, await for approval')       
            return redirect('bin')
       
        else:
            messages.error(request, f'product code {product_code} is not valid or known in the database')
            return redirect("release_stoke")




    return render(request,'screens/release_stoke.html')

def bin(request):
    return render(request,'screens/bin.html')

def filter_report(request):
    



    return render(request,'screens/filter_report.html')

def report(request,*args,**kwargs):
    queryset_list = Bin.objects.order_by('list_date')
    # stoke = Stock.objects.all()

    if 'code' and 'litre' and 'fromdate' and 'todate' in request.GET:
        code =  request.GET['code']
        litre = request.GET['litre']
        fromdate = request.GET['fromdate']
        print(fromdate)
        todate = request.GET['todate']
        if Stock.objects.filter(litre = litre,product_code = code,created__gte=fromdate,created__lte=todate):
            stoke = Stock.objects.filter(product_code = code,litre = litre,created__gte=fromdate,created__lte=todate).order_by('id')
            
            
            if Bin.objects.filter(product_code = code,litre = litre,list_date__gte=fromdate,list_date__lte=todate):
                if code and litre and fromdate and todate:
                    queryset_list = queryset_list.filter(product_code__icontains = code,litre__icontains = litre,list_date__gte=fromdate,list_date__lte=todate)
                    paginator = Paginator(stoke,2) 
                    page = request.GET.get('page')
                    paged_stock = paginator.get_page(page)
                    
            # else:
            #     messages.error(request, f'invalid date sorting from inputed by you from {fromdate} to {todate} for {code} and {litre}')
            #     return redirect('report')
        else:
            messages.error(request, f'invalid date sorting from inputed by you from {fromdate} to {todate} for {code} and {litre}')
            return redirect('bin')


    return render(request,'screens/bin_portal.html',{
        'queryset_list':queryset_list,
        'stoke':stoke
        })


def stock_position(request):
    all_stock = Bin.objects.order_by('-id')
    content = {
        'all_stock':all_stock
    }
    return render(request,'screens/stock position.html', content)

def singlebin(request, singlebin_id):
    
    bin = get_object_or_404(Bin,pk=singlebin_id)
    code = bin.product_code
    litre = bin.litre
    stoke = Stock.objects.filter(product_code = code,litre = litre).order_by('id')
    paginator = Paginator(stoke,4) 
    page = request.GET.get('page')
    paged_stock = paginator.get_page(page)


    return render(request,'screens/bin_portal_single.html',{
        'bin':bin,
        'stoke':paged_stock
        })

def bin_portal(request, *args, **kwargs):
    
    queryset_list = Bin.objects.order_by('-id')


    return render(request,'screens/bin_portal.html',{
        'queryset_list':queryset_list
    })

def search(request, *args, **kwargs):
    

    queryset_list = Bin.objects.order_by('list_date')

    if 'code' and 'litre' in request.GET:
        code =  request.GET['code']
        litre = request.GET['litre']
        if Stock.objects.filter(litre = litre,product_code = code):
            stoke = Stock.objects.filter(product_code = code,litre = litre).order_by('id')
            
            if Bin.objects.filter(product_code = code,litre = litre):
                if code and litre:
                    queryset_list = queryset_list.filter(product_code__icontains = code,litre__icontains = litre)
            else:
                messages.error(request, f'{code} is not valid product code in the stock')
                return redirect('bin')
        else:
            messages.error(request, f'either {code} code or {litre} litre is not valid in the stock')
            return redirect('bin')

  

    return render(request,'screens/search.html',{'queryset_list':queryset_list,'stoke':stoke})
    