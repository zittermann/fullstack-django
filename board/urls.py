from rest_framework import routers
from board.views import BoardViewset

router = routers.DefaultRouter()
router.register(r"boards", BoardViewset, "boards")
