# def log_exceptions(logger):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 logger.exception(e)
#
#         return wrapper
#
#     return decorator
