from fastapi import APIRouter, Depends, HTTPException, status
import logging
from sqlalchemy.orm import Session

# directory dependency
from SSSP.api.models import models
from SSSP.api.core import auth
from SSSP.config import settings

from SSSP.api.core.database import *

router = APIRouter()


@router.post("/delete", status_code=status.HTTP_200_OK)
def delete_current_user(
    token: str = Depends(settings.oauth2_scheme), db: Session = Depends(get_db)
):
    logging.info(f"[*] DELETE_ROUTER>> Request with {token}")
    delete_target_user = auth.get_current_user_by_jwt(token, db)

    if not delete_target_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(delete_target_user)
    db.commit()

    return {"message": "User deleted successfully"}
