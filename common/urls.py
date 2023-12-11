from django.urls import path
from django.contrib.auth import views as auth_views 
            # 로그인 뷰는 따로 만들지 않고 django.contrib.auth앱의 LoginView를 사용 
from . import views


app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]