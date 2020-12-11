python_cmd = "python"

spiders = [
    # 'add_public_video.py',
    # 'author_follow.py',
    'author_data_spider.py',
    # 'rank_add.py',
    # 'tag.py'
]

redis_key = {
    "author_interval": "author::interval",
    "author_interval_prefix": "antuhor::interval::",
    "follow_list": "follow::list"
}