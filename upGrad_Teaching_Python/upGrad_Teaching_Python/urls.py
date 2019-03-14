from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('UserAuth.urls',namespace='userauth')),
    url(r'^schedule/', include('Schedule.urls',namespace='Schedule')),
]
