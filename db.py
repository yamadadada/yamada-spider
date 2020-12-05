from pymongo import MongoClient
import os
import motor
import pymysql


env_dist = os.environ

# client = MongoClient(env_dist.get("MONGO_URL"))
# db = client[env_dist.get("DB_NAME")]  # 获得数据库的句柄
# async_client = motor.motor_tornado.MotorClient(
#     env_dist.get(env_dist.get("DB_NAME")))
#
# async_db = async_client[env_dist.get("DB_NAME")]
mysql_db = pymysql.connect("111.230.220.64", "root", "3116004646")
