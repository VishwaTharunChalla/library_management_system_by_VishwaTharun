from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from quickstart.views import index,category,book
from quickstart import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/(?P<category_id>\d+)$',category,name="category"),
    url(r'^book/(?P<book_id>\d+)$',book,name="book"),
    url(r'^$',index,name="index"),
    url(r'^', include(router.urls)),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^accounts/signup/$', auth_views.LoginView.as_view(template_name="signup.html"), name="login"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]