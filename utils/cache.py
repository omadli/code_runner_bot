from aiocache import caches
import aiocache
from settings import USE_REDIS, REDIS_DB, REDIS_PASSWORD


caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
        'serializer': {
            'class': "aiocache.serializers.PickleSerializer"
        }
    },
    'redis_alt': {
        'cache': "aiocache.backends.redis.RedisCache",
        "endpoint": "127.0.0.1",
        'port': 6379,
        'db': REDIS_DB,
        'password': REDIS_PASSWORD,
        "create_connection_timeout": 1,
        'serializer': {
            'class': "aiocache.serializers.PickleSerializer"
        },
        'plugins': [
            {'class': "aiocache.plugins.HitMissRatioPlugin"},
            {'class': "aiocache.plugins.TimingPlugin"}
        ]
    }
})

if USE_REDIS:
    cache = caches.get("redis_alt")
    cache : aiocache.RedisCache
else:
    cache = caches.get("default")
    cache: aiocache.SimpleMemoryCache
