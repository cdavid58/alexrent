from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Index,name="Index"),
	url(r'^List_Property/$',List_Property,name="List_Property"),
	url(r'^Property_Detail/$',Property_Detail,name="Property_Detail"),
	url(r'^About/$',About,name="About"),
	url(r'^Contact/$',Contact,name="Contact"),
]