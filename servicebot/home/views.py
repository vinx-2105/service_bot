from django.shortcuts import render
from home.forms import LocationForm
# Create your views here.
def home_view(request):
    return render(request, 'home/home.html')

def add_location_view(request):
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = LocationForm()

	context = {'form':form}	
	
	return render(request, 'home/location_form.html', context)
		
