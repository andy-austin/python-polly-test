from django.urls import include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Polly Loan Payment Calculator",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    re_path('', include('loan.urls')),
    re_path(r'^(?P<format>\.json|\.yaml)$', schema_view.without_ui()),
    re_path(r'^$', schema_view.with_ui('swagger')),
]
