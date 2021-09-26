
from django.urls import path
# from.views import address,add_to_cart,mobile,checkout,orders,ProductView,ProductDetailView,CustomerRegistrationView,ProfileView,show_cart,laptop,fashion_top,fashion_bottom,gym_product,home_decor,plus_cart,minus_cart,remove_cart,payment_done,orders
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from fashion.views import HomeView,perfume_view,product_view,shoes_view,watch_view,tshirt_view,ProductDetailView,add_to_cart,CustomerRegistrationView,ProfileView,address,show_cart,remove_cart,checkout,orders
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm
# ,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('alldata/',product_view,name="alldata"),
    path('perfume/',perfume_view,name="perfume"),
    path('perfume/<slug:data>/',perfume_view,name="perfume"),
    path('watches/',watch_view,name="watches"),
    path('watches/<slug:data>/',watch_view,name="watches"),
    path('tshirts/',tshirt_view,name="tshirts"),
    path('tshirts/<slug:data>/',tshirt_view,name="tshirts"),
    path('shoes/',shoes_view,name="shoes"),
    path('shoes/<slug:data>/',shoes_view,name="shoes"),
    path('product-detail/<int:pk>',ProductDetailView.as_view(),name="product-detail"),
    path('add-to-cart/',add_to_cart,name="add-to-cart"),
    path('cart/',show_cart,name='cart'),
    path('removecart/<int:pk>/',remove_cart,name='removecart'),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('address/',address,name="address"),
    path('orders/',orders,name="orders"),
    path('regestration/',CustomerRegistrationView.as_view(),name="customerregistration"),
    path('login/', auth_views.LoginView.as_view(template_name='fashion/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login') ,name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='fashion/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name="passwordchange"),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='fashion/passwordchangedone.html'), name='passwordchangedone'),
    path('checkout/',checkout,name='checkout'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
