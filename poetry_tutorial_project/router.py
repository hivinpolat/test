from leanapi.server import router
from leanapi.path import controller
@controller("personnel", router)
class Personnel:

    @router.get("/get/{personnel_id}")
    def get_personel(self, personnel_id: int) -> dict:
        return {"personnel_id": personnel_id}