# one time setup
import logging

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func): 
    def wrapper(*args, **kwargs): 
  
        result = func(*args, **kwargs)

        # To write a log record:
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        
        return result

    return wrapper

# Decorating the function
@logger_decorator
def greeting():
        print("Hello, World!")

@logger_decorator
def positional_arguments(*args):
    return True

@logger_decorator
def keyword_arguments(**kwargs):
    return logger_decorator


# Decorating the function
greeting()
positional_arguments(100, 200, 300)
keyword_arguments(name="Khalilah", age=25)


