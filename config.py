import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'server223.web-hosting.com'
    #MAIL_PORT =  int(os.environ.get('MAIL_PORT') or 465) #or int(465)
    MAIL_PORT = 465
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = False
    # MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'info@metamova.com'
    MAIL_PASSWORD = 'metamova_info'
    ADMINS = os.environ.get('ADMINS') or ['oksana@metamova.com']
    LANGUAGES = os.environ.get('LANGUAGES') or ['en', 'uk', 'pseudo', 'ids']


    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    # POSTS_PER_PAGE = 25
    
