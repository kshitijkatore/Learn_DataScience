import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger =logging.getLogger("ArithematicApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def substract(a,b):
    result = a - b
    logger.debug(f"Adding {a}-{b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Divison by zero error")
        return None
    
add(10,15)
substract(15,10)
multiply(20,10)
divide(20,10)