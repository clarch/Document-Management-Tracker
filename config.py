# import os


# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config:
# 	SECRET_KEY = 'non is notin is notin is non'
# 	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# class DevelopementConfig(Config):
#     '''This class configures the development
#     environment properties
#     '''
#     DEBUG = True
#     # DEBUG_TB_INTERCEPT_REDIRECTS = False
#     # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
#     #     os.path.join(basedir, 'Docmanager.sqlite')

# # class ProductionConfig(Config):
# #     '''This class configures the development
# #     environment properties
# #     '''
# #     DEBUG = True
# #     DEBUG_TB_INTERCEPT_REDIRECTS = False
# #     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
# #         os.path.join(basedir, 'Docmanager.sqlite')


# config = {
#     'development': DevelopementConfig,
#     'default': DevelopementConfig
# }