CELERY_RESULT_BACKEND = 'rpc://'
BROKER_URL = 'amqp://admin:mypass@rabbit:5672/'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
