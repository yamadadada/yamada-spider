from pymongo import MongoClient
import os
import motor
import pymysql
import redis
from local_config import db_host, db_user, db_password, db_database, redis_host, redis_port, redis_db_index, \
    redis_password


env_dist = os.environ

# client = MongoClient(env_dist.get("MONGO_URL"))
# db = client[env_dist.get("DB_NAME")]  # 获得数据库的句柄
# async_client = motor.motor_tornado.MotorClient(
#     env_dist.get(env_dist.get("DB_NAME")))
# async_db = async_client[env_dist.get("DB_NAME")]

mysql_db = pymysql.connect(db_host, db_user, db_password, db_database)

redis_db = redis.Redis(host=redis_host, port=redis_port, db=redis_db_index, password=redis_password,
                       decode_responses=True, health_check_interval=30)
