import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='ex1.log',
    filemode='a', # w - write, a - append
    format='%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s',
)


test_message = 'Someone'

logging.debug(f'debug message shows: {test_message}')  # 10
logging.info('info') # 20
logging.warning('warning') # 30
logging.error('error') # 40
logging.critical('critical') # 50
