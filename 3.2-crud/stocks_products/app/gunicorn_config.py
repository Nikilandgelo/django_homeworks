import os

bind = '0.0.0.0:5555'
workers = os.cpu_count() * 2
accesslog = './gunicorn/access.log'
errorlog = './gunicorn/error.log'
loglevel = 'info'