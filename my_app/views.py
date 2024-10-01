# chat/views.py
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Product,Catogory,Signup,Crud,Item,Youtube_thum
from .forms import MyForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def dashboard(request):
    if Signup.objects.exists():
        Products = None
        product = request.POST.get('product-id')
        Catogorys = Catogory.objects.all()
        category_id = request.GET.get('Catogory')
        cart = request.session.get('cart')

        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        if request.method == "POST":
            product = request.POST.get('product-id')
            print("product = ", product)

        if category_id:
            Products = Product.objects.filter(category_id=category_id)
        else:
            Products = Product.objects.all()
         # Show 10 items per page.
        data = {
            'Products': Products,
            'Catogorys': Catogorys,
        }

        return render(request, 'dashboard.html', data)
    else:
        return render(request, 'login.html')




def signup(request):
    erro_msg=None
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not username:
            erro_msg="fill username is required"
            return render(request, 'signup.html',{'erro_msg':erro_msg})
        elif len(username) < 4:
            erro_msg = "Username must be at least 4 characters long."
            return render(request, 'signup.html',{'erro_msg':erro_msg})
        
        elif Signup.objects.filter(email=email).exists():
            erro_msg = "Email is already registered."
            return render(request, 'signup.html',{'erro_msg':erro_msg})
        
        elif len(password) < 4:
            erro_msg = "Password must be at least 4  long."
            return render(request, 'signup.html',{'erro_msg':erro_msg})
        else:    
          Sign=Signup(username=username,email=email,password=password)
          Sign.save()
          return HttpResponse("Signup successful!")  
        
    return render(request, 'signup.html')


from django.shortcuts import render, HttpResponse, redirect
from .models import Signup

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Signup.objects.filter(email=email, password=password).first()
        if user:
            # Store user information in the session
            request.session['Signup_id'] = user.id
            request.session['email'] = user.email
            return redirect("/dashboard")
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password.'})
    else:
        return render(request, 'login.html')




def index(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 2) 
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        create_data=request.POST.get("create")
        cruds=Crud.objects.create(task=create_data)
        return redirect('home')

     # Handle POST request for deleting CRUD object
    
    cruds=Crud.objects.all()
    completed_task=Crud.objects.filter(is_completes=True)
    context={
        "page_obj":page_obj,
       "cruds" :cruds,
       "completed":completed_task
    }
    return render(request,'index.html',context)



def delete_view(request, pk):
    if request.method == "POST":
        if "delete" in request.POST:
            delete_id = request.POST.get("delete")
            crud_to_delete = get_object_or_404(Crud, pk=delete_id)
            crud_to_delete.delete()
            return redirect("home")
        else:
         return HttpResponse("Not deleted")

def products_view(request,id):
    Allinfo=get_object_or_404(Item,id=id)

    return render(request, 'products.html', {'item': Allinfo})

def update_view(request, pk):
    crud_instance = get_object_or_404(Crud, pk=pk)

    if request.method == "POST":
        crud_instance.task = request.POST.get('update',)
        # crud_instance.is_completes = request.POST.get('is_completes',False)
        crud_instance.save()
        return redirect('home')  # Redirect to home page after updating

    return render(request, 'update.html', {'crud_instance': crud_instance})


def logout(request):
    request.session.clear()
    return redirect('/login/')




# @login_required
def cart(request):
    # Print the contents of the cart session variable for debugging
    print(request.session.get('cart')) 
    
    # Get the keys of the cart dictionary stored in the session
    cart_keys = request.session.get('cart', {}).keys()

    # Filter out 'null' values and convert remaining keys to integers
    cart_keys_int = [int(key) for key in cart_keys if key.isdigit()]

    # If there are items in the cart, filter products based on the cart keys
    if cart_keys_int:
        products = Product.objects.filter(id__in=cart_keys_int)
    else:
        # If the cart is empty or not set, display all products
        products = Product.objects.all()   

    return render(request, 'cart.html', {'products': products})




def home(request):
    return render(request,'home.html')

import requests
from django.http import JsonResponse

def call_external_api(request):
    # Define the API URL
    api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Make the GET request
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        return JsonResponse(data, safe=False)  # Return the API response as a Django JsonResponse
    else:
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=500)
    

import re
from django.shortcuts import render, redirect
from .models import Youtube_thum  # Assuming you have this model for storing video IDs

def youtube_thub(request):
    get_id = Youtube_thum.objects.all()  # Fetch all saved video IDs from the database
    
    if request.method == "POST": 
        # Handle the delete request
        get_id_del = request.POST.get('delete_meth')
        if get_id_del:
            try:
                # Fetch the object by id and delete it
                get_id_instance = Youtube_thum.objects.get(id=get_id_del)
                get_id_instance.delete()
            except Youtube_thum.DoesNotExist:
                pass  

        search_vid = request.POST.get('search_bar')
        if search_vid:
            video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", search_vid)
            if video_id_match:
                video_id = video_id_match.group(1)
                print(f"Extracted video ID: {video_id}")

                url_data = Youtube_thum(url_name=video_id)
                url_data.save()

            return redirect('youtube')  
    context = {
        'get_id': get_id,  
    }
    return render(request, 'youtube.html', context)
