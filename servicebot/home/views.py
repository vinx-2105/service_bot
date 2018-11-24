from django.shortcuts import render
from home.forms import LocationForm, OrderForm
from home.models import Location, Order
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def home_view(request):
    return render(request, 'home/home.html')

def add_location_view(request):
	try:
		location_instance = get_object_or_404(Location)
	except:
		location_instance = None
	form = LocationForm(request.POST or None, instance = location_instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'form': form,
	}

	return render(request, 'home/location_form.html', context)

def create_order_view(request):
	try:
		order_instance = get_object_or_404(Order)
	except:
		order_instance = None
	form = OrderForm(request.POST or None, instance = order_instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'form': form,
	}

	return render(request, 'home/create_order.html', context)

def order_history_view(request):
	context = {'orders':Order.objects.all()}
	return render(request, 'home/order_history.html', context)