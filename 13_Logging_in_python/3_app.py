import logging

#configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S ',
    handlers=[logging.FileHandler('app1.log'),logging.StreamHandler()]

)
logger=logging.getLogger("ArthemticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} + {b} ={result}")
    return result
def subtract(a,b):
    result=a-b
    logger.debug(f"subtracting {a} - {b} = {result}")
    return result
def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result
def divide(a,b):
    try:
        
        result=a/b
        logger.debug(f"Division {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("divisionn by Zero error")
        return None
add(10,15)
subtract(15,10)
multiply(10,15)
divide(20,00)