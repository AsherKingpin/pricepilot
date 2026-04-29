from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializer import ProductSerializer
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
        else:
            permission_classes = [
                IsReadOnlyOrAuthenticated
            ]
        
        return [permission() for permission in permission_classes]

