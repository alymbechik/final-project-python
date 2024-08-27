from django.shortcuts import render, redirect
from .models import Category, Food, Lead
from .forms import FoodUpdateForm

def index_view(request):
    pizza = Category.objects.get(title='Пицца')
    salad = Category.objects.get(title='Салат')
    noodle = Category.objects.get(title='Лапша')

    pizzas = Food.objects.filter(category=pizza)
    salads = Food.objects.filter(category=salad)
    noodles = Food.objects.filter(category=noodle)

    return render(request=request, template_name='app/index.html', context={'pizzas': pizzas, 'salads': salads, 'noodles': noodles})

def detail_view(request, pk):
    food = Food.objects.get(id=pk)

    if request.method == 'POST':
        form = FoodUpdateForm(request.POST, request.FILES, instance=food)

        if form.is_valid():
            form.save()
    form = FoodUpdateForm(instance=food)

    return render(request=request, template_name='app/detail.html', context={'food': food, 'form': form})

def about_view(request):
    return render(request=request, template_name='app/about.html')

def contact_view(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']

        lead = Lead(
            name=name,
            email=email,
            message=message,
            subject=subject
        )
        lead.save()
    return render(request=request, template_name='app/contact.html')

def food_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        img = request.FILES['img']
        category_title = request.POST['category']

        category = Category.objects.get(title=category_title)

        food = Food(
            title=title,
            description=description,
            price=price,
            img=img,
            category=category
        )
        food.save()

    return render(request=request, template_name='app/food_create.html',)

def delete_food(request, pk):
    food = Food.objects.get(id=pk)
    food.delete()

    return redirect('index')