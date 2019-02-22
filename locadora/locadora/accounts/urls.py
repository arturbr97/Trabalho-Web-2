from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^okay/$',views.okay),
    url(r'^okay1/$',views.okay1),
    url(r'^next/$',views.next),
    url(r'^log/$',views.log),
]
