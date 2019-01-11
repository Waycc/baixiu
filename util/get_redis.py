import redis
from settings import settings

rdp = redis.ConnectionPool(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    max_connections = settings.REDIS_MAX_CONNECTIONS
)

redis_client = redis.StrictRedis(connection_pool = rdp)
