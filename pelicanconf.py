AUTHOR = 'LuBan'
SITENAME = 'LuBan Robotic'
SITEURL = ""

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ("Docs", "https://docs.frc-9597.com"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
'''
额外现实部分
'''
# 副标题
SITESUBTITLE = "TEAM 9597, HEAD TO MAKE IT"

'''
主题与外观设置
'''
# 设置主题,主题文件已放置到项目根目录下的theme文件中

THEME = './themes/notmyidea'
# 设置通过文件夹的方式进行文档分类
USE_FOLDER_AS_CATEGORY = True
# 输出到Docs
OUTPUT_PATH = 'docs'

# 构建前删除旧的网页文档，删除时将会删除所有OUTPUT_PATH指向的文件夹下的内容
DELETE_OUTPUT_DIRECTORY = True
# output_path文档指定的文件不会被删除
OUTPUT_RETENTION = [
        'CNAME',
        ]
