from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# directory dependency
from SSSP.api.models import models
from SSSP.api.schemas import schema_challenges
from SSSP.api.core.database import get_db
from SSSP.api.core.auth import get_current_user_by_jwt
from SSSP.config import settings

import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/get_all_challenge", response_model=list[schema_challenges.ChallengeResponse])
def get_all_challenge(
    token: str = Depends(settings.oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user_by_jwt(token, db)

    challenges = db.query(models.Challenge).all()
    challenge_responses = [
        schema_challenges.ChallengeResponse.from_orm(challenge)
        for challenge in challenges
    ]
    logging.info(f"[*] CHALLENGE_LIST>> {challenge_responses}")
    return challenge_responses


@router.get(
    "/{challenge_id}",
    response_model=schema_challenges.ChallengeResponse,
    status_code=status.HTTP_200_OK,
)
def get_challenge(
    challenge_id: int,
    token: str = Depends(settings.oauth2_scheme),
    db: Session = Depends(get_db),
):
    user = get_current_user_by_jwt(token, db)
    # admin 이면 전체
    # User 면 response 에 solved challenge 포함해서 전달

    challenge = (
        db.query(models.Challenge).filter(models.Challenge.id == challenge_id).first()
    )
    if not challenge:
        logging.warning(f"Challenge not found: ID {challenge_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Challenge not found"
        )

    logging.info(f"[*] Retrieved Challenge: {challenge}")
    return schema_challenges.ChallengeResponse.from_orm(challenge)

