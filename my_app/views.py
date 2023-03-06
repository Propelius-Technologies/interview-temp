from django.shortcuts import render, redirect
from django.db.models import Max, Min
from my_app.models import NewProductAddModel, UserRegistraionModel
from django.contrib import messages
from django.db.models import Q


# Create your views here.


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f'email:- {email}\n, password:- {password}')

        model_obj = UserRegistraionModel.objects.filter(
            email=email, password=password).values('email', 'password')

        print(f"datas:- {model_obj}")
        for data in model_obj:
            print('email------>', data['email'])
            print('password------>', data['password'])
            if data['email'] == email and data['password'] == password:
                request.session['email'] = email
                request.session['password'] = password
                messages.success(request, "User Login Successfully")
                return redirect('product_listing')
            else:
                messages.error(
                    request, "Error. Please Enter Valid User Name Or Password")
                return redirect('login')

    return render(request, 'registration/login.html')


def register_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(
            f"user_name:- {user_name}\n, email:- {email}\n, password:-{password}")

        if user_name != "" and email != "" and password != "":
            model_obj = UserRegistraionModel.objects.create(
                user_name=user_name, email=email, password=password)
            model_obj.save()
            messages.success(request, "User Add Successfully")
        else:
            messages.error(request, "Error. Please Enter All User Data")
            return redirect('reg')

    return render(request, 'registration/login.html')


def dashbord_page(request):
    product_model = NewProductAddModel.objects.all()
    if request.method == "POST":
        search = request.POST.get('search')
        field = request.POST.get('field')
        min_price = request.POST.get("min")
        max_price = request.POST.get("max")
        print(
            f"field:- {field}\n, Search Product:- {search}\n, min_price:- {min_price}\n, max_price:- {max_price}")

        product_model = NewProductAddModel.objects.all()

        if search != "" and search is not None and field == '1':
            product_model = product_model.filter(title__startswith=search)
            print('data:------>', product_model)

        if search != "" and search is not None and field == '2':
            product_model = product_model.filter(
                description__startswith=search)
            print('data:------>', product_model)

        if min_price != '' and max_price != '':
            product_model = product_model.filter(
                Q(price__gte=min_price) & Q(price__lte=max_price))
            print('data:------>', product_model)

    return render(request, 'listing_page.html', {'data': product_model})


def form_view(request):
    if request.session.has_key('email'):
        email = request.session['email']
        return render(request, 'registration/login.html', {"email": email})
    else:
        return render(request, 'registration/login.html', {})


def delete_session(request):
    try:
        del request.session['email']
        del request.session['password']
    except:
        pass
    return render(request, "registration/login.html")
