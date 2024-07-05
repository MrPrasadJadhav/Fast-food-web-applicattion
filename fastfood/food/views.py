from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .models import Pizza, Burger
from .forms import NewUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.

def index(request):
    request.session.set_expiry(0)
    #print(request.session['order'])
    ctx = {'active_link' : 'index'}
    return render(request,"food/index.html",ctx)

def pizza(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    ctx = {'pizzas' : pizzas, 'active_link': 'pizza'}
    return render(request,"food/pizza.html",ctx)

def burger(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers' : burgers, 'active_link': 'burger'}
    return render(request,"food/burgers.html",ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        print(request.session['note'])
        request.session['order'] = request.POST.get('orders')
        print(request.session['order'])
    ctx = {'active-link' : 'order'}
    return render(request,"food/order.html",ctx)


'''
@csrf_exempt
def order(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        test = request.POST.get('test')
        message = request.POST.get('message')
        print(f"Test: {test}, Message: {message}")
        return JsonResponse({'message': 'Data received successfully', 'test': test})
    
    ctx = {'active_link': 'order'}
    return render(request, "food/order.html", ctx)
    '''



def success(request):
    order = request.session['order']
    ctx = {'order' : order}
    return render(request,"food/success.html",ctx)

def signup(request):
    ctx ={}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'food/signup.html',ctx)


def logIn(request):
    if request.POST :
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password =pwd)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'username and/or password are incorect')
    ctx = {'active_link' : 'login'}
    return render(request,'food/login.html',ctx)

def logOut(request):
    logout(request)
    return redirect('index')