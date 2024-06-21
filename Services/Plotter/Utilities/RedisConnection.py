#Redis connection goes here.
import redis
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

class RedisConnections:
    def __init__(self, client=None, host='redis', port=6379, db=0, max_retries=5, retry_delay=5):
        self.client = client or redis.Redis(host=host, port=port, db=db)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def _handle_redis_operation(self, func, *args, **kwargs):
        """Manejar operaciones Redis con reintentos y manejo de errores."""
        retries = 0
        while retries <= self.max_retries:
            try:
                return func(*args, **kwargs)
            except (redis.ConnectionError, redis.TimeoutError) as e:
                logger.error(f"Redis error: {e}. Retrying in {self.retry_delay} seconds.")
                retries += 1
                sleep(self.retry_delay)
        logger.error("Max retries reached. Giving up.")
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __contains__(self, key):
        return self._handle_redis_operation(self.client.exists, key)

    def get_from_cache(self, key):
        value = self._handle_redis_operation(self.client.get, key)
        if value:
            try:
                return value.decode('utf-8')
            except UnicodeDecodeError:
                return value
        return None

    def add_to_cache(self, key, value, time=None):
        if time:
            return self._handle_redis_operation(self.client.setex, key, time, value)
        else:
            return self._handle_redis_operation(self.client.set, key, value)

    def remove_from_cache(self, key):
        return self._handle_redis_operation(self.client.delete, key)

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            logger.error(f"Error closing Redis connection: {e}")