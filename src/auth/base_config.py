from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from src.config import SECRET


# cookie_transport = CookieTransport(cookie_max_age=3600)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)