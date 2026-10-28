from fastapi import Header
from .security import require_auditor_or_admin

def authorized_reader(authorization: str | None = Header(default=None)) -> int:
    return require_auditor_or_admin(authorization)
