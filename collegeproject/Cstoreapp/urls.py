from.import views
from django.urls import path
app_name='Cstoreapp'
urlpatterns = [
    path('',views.dept,name='dept'),
    # path('<slug:c_slug>/',views.dept,name='department_list'),
    path('login/',views.login,name='login'),
    path('register',views.register,name='register'),
    path('shop',views.shop,name='shop',),
    path('order/',views.order,name='order',),
    path('logout',views.logout,name='logout'),
    ]
