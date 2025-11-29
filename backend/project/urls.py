from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("products/", include("project.products.urls")),
    path("cart/", include("project.cart.urls")),
    path("orders/", include("project.orders.urls")),
    path("payments/", include("project.payments.urls")),
    path("accounts/", include("project.accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
