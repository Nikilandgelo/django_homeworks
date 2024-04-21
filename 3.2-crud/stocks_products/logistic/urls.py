from rest_framework.routers import SimpleRouter
from logistic.views import ProductViewSet, StockViewSet

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls