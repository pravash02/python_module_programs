## Prequisites for celery

### install redis
> brew install redis

### install celery
> pip install celery

### Start the worker: To start the Celery worker, you can use the following command:
> celery -A folder_name.file_name worker --loglevel=info

### Start the celery beat: To start celery beat, you can use the following command:
> celery -A folder_name.file_name beat --loglevel=info

### (Optional) Start the flower: Celery Flower is a web-based tool for monitoring and managing Celery clusters. you can start it using the following command:
> celery -A your_module_name:app flower --loglevel=info
