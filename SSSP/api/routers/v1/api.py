from fastapi import APIRouter

# directory dependency

from SSSP.api.routers.v1.auth import (
    auth_check, 
    register, 
    login,
    logout,
)

from SSSP.api.routers.v1.user import (
    delete_current_user,
    get_current_user,
    get_user_list,
    update_current_user,
)

from SSSP.api.routers.v1.challange import (
    get_challenges,
    create_challenge,
    delete_challenge,
    update_challenge,
    submit_challenge,
)

from SSSP.api.routers.v1.score import (
    get_all_score,
)

from SSSP.api.routers.v1.notice import (
    get_all_notice,
)

router = APIRouter()

# non prefix
router.include_router(get_all_score.router, tags=["scoring"])
router.include_router(get_all_notice.router, tags=["notice"])
# auth
router.include_router(login.router, prefix="/auth", tags=["auth"])
router.include_router(logout.router, prefix="/auth", tags=["auth"])
router.include_router(register.router, prefix="/auth", tags=["auth"])
router.include_router(auth_check.router, prefix="/auth", tags=["auth"])

# user
router.include_router(delete_current_user.router, prefix="/user", tags=["user"])
router.include_router(get_user_list.router, prefix="/user", tags=["user"])
router.include_router(get_current_user.router, prefix="/user", tags=["user"])
router.include_router(update_current_user.router, prefix="/user", tags=["user"])

# challenge
router.include_router(get_challenges.router, prefix="/challenges", tags=["challenge"])
router.include_router(create_challenge.router, prefix="/challenges", tags=["challenge"])
router.include_router(delete_challenge.router, prefix="/challenges", tags=["challenge"])
router.include_router(update_challenge.router, prefix="/challenges", tags=["challenge"])
router.include_router(submit_challenge.router, prefix="/challenges", tags=["challenge"])
