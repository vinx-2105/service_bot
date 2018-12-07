from tastypie.resources import ModelResource
from tastypie import fields
from home.models import Location, Order
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        allowed_methods = ['post', 'get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'location'

class OrderResource(ModelResource):
    source = fields.CharField(attribute="source")
    destination = fields.CharField(attribute="destination")
    class Meta:
        queryset = Order.objects.all()
        allowed_methods = ['post', 'get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'order'
