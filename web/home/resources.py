from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.serializers import Serializer
from home.models import Location, Order
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
<<<<<<< HEAD
=======
        allowed_methods = ['post', 'get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'location'
>>>>>>> 6aad511241448763b8acc66ebaf8e1be2b8327a3

class OrderResource(ModelResource):
    source = fields.CharField(attribute="source")
    destination = fields.CharField(attribute="destination")
    class Meta:
        queryset = Order.objects.all()
<<<<<<< HEAD
        resource_name = 'order'
        authorization = Authorization()
=======
        allowed_methods = ['post', 'get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'order'
>>>>>>> 6aad511241448763b8acc66ebaf8e1be2b8327a3
