from rest_framework import routers
from thread.views import ThreadViewset

router = routers.DefaultRouter()
router.register(r"threads", ThreadViewset, "threads")
