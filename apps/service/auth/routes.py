from apps.service.auth import router

@router.get("/auth-read-user/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
