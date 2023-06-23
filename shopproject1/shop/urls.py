
from django.urls import path
from . import views
app_name='shop'

urlpatterns = [

    path('',views.allproductcategory,name='allproductcategory'),
    path('<slug:cat_slug>/',views.allproductcategory,name='products_by_category'),
    path('<slug:cat_slug>/<slug:product_slug>/',views.product_detail,name='procatdetail'),

]
