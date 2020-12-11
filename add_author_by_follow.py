from time import sleep
from biliob import BiliobSpider
import logging
from config import redis_key


class AddAuthorByFollowSpider(BiliobSpider):

    def __init__(self):
        super().__init__("add author by follow")
        self.except_content_type = 'application/json'
        pass

    async def gen_url(self):
        ps = 50
        pn_list = [1, 2, 3]
        url = 'http://api.bilibili.com/x/relation/followings?vmid={mid}&pn={pn}&ps={ps}'
        while True:
            try:
                mid = self.redis_db.lpop(redis_key["follow_list"])
                for pn in pn_list:
                    yield url.format(mid=mid, pn=pn, ps=ps)
            except Exception as e:
                logging.exception(e)
                sleep(10)

    async def parse(self, res):
        item = []
        try:
            j = res.json_data
            for each_member in j['data']['list']:
                item.append({
                    'mid': each_member['mid'],
                    'name': each_member['uname'],
                    'face': each_member['face'],
                    'official': each_member['official_verify']['desc']
                })
        except Exception as e:
            self.logger.exception(e)
            return None
        return item

    async def save(self, item):
        if item is None:
            return 0
        # 检查这个用户是否已在爬取列表
        for each in item:
            if self.redis_db.get(redis_key['author_interval_prefix'] + str(each['mid'])) is None:
                self.redis_db.set(redis_key['author_interval_prefix'] + str(each['mid']), 86400)
                cursor = self.mysql_db.cursor()
                sql = "insert into `author`(`mid`, `name`, `face`, `official`) values ({}, '{}', '{}', '{}')"\
                    .format(each['mid'], each['name'], each['face'], each['official'])
                cursor.execute(sql)
        self.mysql_db.commit()
        return 1


if __name__ == "__main__":
    s = AddAuthorByFollowSpider()
    s.run()
