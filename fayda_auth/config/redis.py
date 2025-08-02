import redis
import os
import logging

class RedisConfig:
    def __init__(self):
        self.redis_client = None

    def init_redis(self):
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = os.getenv('REDIS_PORT', '6379')
        
        # self.redis_client = redis.Redis(host=redis_host, port=int(redis_port), db=0)
        self.redis_client = redis.Redis(
                            host='redis-12565.c8.us-east-1-2.ec2.redns.redis-cloud.com',
                            port=12565,
                            decode_responses=True,
                            username="default",
                            password="k6hJ8j31Lm3O3iXMdhsjKzjefzxBxl8U",
                        )
    
        try:
            self.redis_client.ping()
            logging.info("Connected to Redis successfully!")
        except redis.ConnectionError as e:
            logging.error(f"Failed to connect to Redis: {e}")
            raise
        return self.redis_client
    



# r = redis.Redis(
#     host='redis-12565.c8.us-east-1-2.ec2.redns.redis-cloud.com',
#     port=12565,
#     decode_responses=True,
#     username="default",
#     password="k6hJ8j31Lm3O3iXMdhsjKzjefzxBxl8U",
# )

# success = r.set('foo', 'bar')
# # True

# result = r.get('foo')
# print(result)
# # >>> bar

