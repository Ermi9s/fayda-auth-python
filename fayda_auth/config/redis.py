import redis
import os
import logging

class RedisConfig:
    def __init__(self):
        self.redis_client = None

    def init_redis(self):
        # redis_host = os.getenv('REDIS_HOST', 'redis-12565.c8.us-east-1-2.ec2.redns.redis-cloud.com')
        # redis_port = int(os.getenv('REDIS_PORT', '12565'))
        # redis_username = os.getenv('REDIS_USERNAME', 'default')
        # redis_password = os.getenv('REDIS_PASSWORD', 'k6hJ8j31Lm3O3iXMdhsjKzjefzxBxl8U')

        redis_host =  'redis-12565.c8.us-east-1-2.ec2.redns.redis-cloud.com'
        redis_port = 12565
        redis_username = 'default'
        redis_password = 'k6hJ8j31Lm3O3iXMdhsjKzjefzxBxl8U'

        try:
            self.redis_client = redis.Redis(
                host=redis_host,
                port=redis_port,
                decode_responses=True,
                username=redis_username,
                password=redis_password
            )
            self.redis_client.ping()
            logging.info("Connected to Redis successfully!")
        except redis.ConnectionError as e:
            logging.error(f"Failed to connect to Redis: {e}")
            raise

        return self.redis_client
