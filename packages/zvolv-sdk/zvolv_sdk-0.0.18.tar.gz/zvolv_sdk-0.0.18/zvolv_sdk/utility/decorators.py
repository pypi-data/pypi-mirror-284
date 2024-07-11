from functools import wraps

def enforce_pydantic_model(model_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, model_class):
                    break
            else:
                raise TypeError(f"Expected instance of {model_class.__name__}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def attach_status_log(func):
    def wrapper(*args, **kwargs):
        context = args[0]
        event = args[1]
        automation_uuid = event['headers']['x-nuclio-function-name']
        context.client.logger.initExecutionLog(automation_uuid)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            context.client.logger.closeExecutionLog('failed', str(e), None)
            raise
        finally:
            context.client.logger.closeExecutionLog('success', 'Execution completed', None)
    return wrapper
