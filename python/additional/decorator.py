"""
Decorator with logging for function
"""
import logging.config
import logging
import time

logging.config.fileConfig("logging.ini")
logger = logging.getLogger('decor_logger')


def log(func):
    """
    Decorator
    """
    def wrapper(*args, **kwargs):
        logger.info('Start ')
        time.sleep(0.1)
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        logger.info('Finish in %d sec.', finish - start)
    return wrapper


def progression(base=1, inc=10, num=2):
    """
    Returns arithmetic progression num times from number base with inc step
    :param base: int
    :param inc: int
    :param num: int
    :return:
    """
    while num > 0:
        yield base
        base += inc
        num -= 1

@log
def main():
    """
    Main function
    :return:
    """
    prg = progression(1, 12, 20)
    for item in prg:
        print(item)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
