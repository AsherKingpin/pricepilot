from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from pricing.pricing_engine import calculate_price
from .models import Product
from .serializers import ProductSerializer
from accounts.permissions import IsAdmin, IsAdminOrManager, IsReadOnlyOrAuthenticated
# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [
                IsAdmin,
            ]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [
                IsAdminOrManager
            ]
        elif self.action in ['view', 'purchase']:
            permission_classes = [
                
            ]
        else:
            permission_classes = [
                IsReadOnlyOrAuthenticated
            ]
        
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods = ['POST'])
    def view(self, request, pk=None):
        product = self.get_object()
        product.views += 1
        product.save()
        new_price = calculate_price(product)
        product.current_price = new_price
        product.save()
        return Response(
            {"message":"Product viewed"},
            status = status.HTTP_200_OK
        )

    @action(detail=True, methods = ['POST'])
    def purchase(self, request, pk=None):
        product = self.get_object()
        if product.stock <= 0:
            return Response(
                {"error":"Stock not available"},
                status = status.HTTP_400_BAD_REQUEST
            )
        else:
            product.purchased += 1
            product.stock -=1
            product.save()
            new_price = calculate_price(product)
            product.current_price = new_price
            product.save()
            return Response(
                {"message": "Product Purchased"},
                status = status.HTTP_200_OK
            )
        

