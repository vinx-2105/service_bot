from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.serializers import Serializer
from home.models import Location, Order

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()

class OrderResource(ModelResource):
    source = fields.CharField(attribute="source")
    destination = fields.CharField(attribute="destination")
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        authorization = Authorization()