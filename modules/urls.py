from rest_framework.routers import SimpleRouter

from modules.views import ModuleViewSet
from modules.apps import ModulesConfig

app_name = ModulesConfig.name

router = SimpleRouter()
router.register("modules", ModuleViewSet, basename="modules")

urlpatterns = []

urlpatterns += router.urls
