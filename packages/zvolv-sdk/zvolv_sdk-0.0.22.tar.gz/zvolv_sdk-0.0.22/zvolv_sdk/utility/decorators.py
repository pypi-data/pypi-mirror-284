from functools import wraps
import traceback

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

def zvolv_wrapper(func):
    def wrapper(context, event):
        print('in decorator warpper')
        headers = event.headers
        automation_uuid = headers['X-Nuclio-Function-Name']
        print('check context')
        print(context.__dict__)
        print('check uuid')
        print(automation_uuid)
        context.client.logger.initExecutionLog(automation_uuid, event.body)
        try:
            result = func(context, event)
            context.client.logger.closeExecutionLog('success', 'Execution completed', result, None)
            return result
        except Exception as e:
            trace = traceback.format_exc()
            context.client.logger.closeExecutionLog('failure', str(e), None, trace)
            raise
    return wrapper
