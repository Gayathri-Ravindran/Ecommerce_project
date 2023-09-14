from django.urls import path,include
from . import views
app_name='ECommerceApp'
urlpatterns = [
    path('',views.AllProductCate,name='AllProductCate'),
    path('<slug:c_slug>/',views.AllProductCate,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
]