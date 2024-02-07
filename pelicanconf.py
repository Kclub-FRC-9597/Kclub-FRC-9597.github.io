'''
站点基础设置
'''
AUTHOR = 'LuBan'
SITENAME = 'LuBan Robotic' # 站点标题
SITESUBTITLE = "TEAM 9597, HEAD TO MAKE IT" # 副标题
SITEURL = ""
LOGO_PATH = "../src/logo_slogon.png" #自定义标签，用于显示logo

'''
编译选项
'''
PATH = "content"         #源文件
OUTPUT_PATH = 'docs'     #输出到
THEME = './themes/inUse' #使用主题
STATIC_PATH ='src'       #静态文件，如图片等
DEFAULT_PAGINATION = 20  #每页显示博文数量
USE_FOLDER_AS_CATEGORY = True   #使用用户文件夹作为分类依据
DELETE_OUTPUT_DIRECTORY = True  #编译前删除OUTPUT_PATH文件夹下的文档
OUTPUT_RETENTION = ['CNAME','src\*']    #编译时不需要删除的旧文档

'''
其他选项
'''
TIMEZONE = 'UTC'         # 时区
DEFAULT_LANG = 'en'      #默认语言

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

'''
友情链接
'''
SOCIAL = (              #社交平台
    ("Github", "https://github.com/Kclub-FRC-9597"),
)
LINKS = (               #友情链接
        ("Docs", "https://docs.frc-9597.com"),
)

