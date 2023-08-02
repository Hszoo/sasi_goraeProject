from django.urls import path
from . import views

# http://128.0.0.1/api/swagger/
urlpatterns = [
    path('swagger/', views.ExampleView.as_view(), name='swagger'),
    # 다른 API 뷰들과 URL 패턴을 여기에 추가할 수 있습니다.
]
