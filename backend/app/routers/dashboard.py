from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.dashboard_service import dashboard_stats

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def get_dashboard(
    db: Session = Depends(get_db)
):
    return dashboard_stats(db)