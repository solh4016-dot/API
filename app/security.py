"""
JWT mínimo (HS256) implementado con la librería estándar de Python,
para no agregar dependencias. Contiene el id del usuario en "sub", igual
que el token de fakestoreapi.com, de modo que la app pueda decodificarlo
y mapear el rol (US01 - Escenario 1).
"""
import base64
import hashlib
import hmac
import json
import os
import time

JWT_SECRET = os.getenv("JWT_SECRET", "cambia-este-secreto-antes-de-entregar")
TOKEN_TTL_SECONDS = 60 * 60  # 1 hora


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64url_decode(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def _sign(signing_input: str) -> str:
    digest = hmac.new(JWT_SECRET.encode(), signing_input.encode(), hashlib.sha256).digest()
    return _b64url(digest)


def create_token(user_id: int, username: str) -> str:
    now = int(time.time())
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": user_id, "user": username, "iat": now, "exp": now + TOKEN_TTL_SECONDS}

    signing_input = (
        _b64url(json.dumps(header, separators=(",", ":")).encode())
        + "."
        + _b64url(json.dumps(payload, separators=(",", ":")).encode())
    )
    return f"{signing_input}.{_sign(signing_input)}"


def decode_token(token: str) -> dict:
    """Devuelve el payload si la firma es válida y no ha expirado; si no, lanza ValueError."""
    try:
        header_b64, payload_b64, signature = token.split(".")
    except ValueError:
        raise ValueError("Formato de token inválido")

    expected = _sign(f"{header_b64}.{payload_b64}")
    if not hmac.compare_digest(expected, signature):
        raise ValueError("Firma inválida")

    payload = json.loads(_b64url_decode(payload_b64))
    if payload.get("exp", 0) < int(time.time()):
        raise ValueError("Token expirado")
    return payload
