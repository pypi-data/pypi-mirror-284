import contextvars

mysqlClient = contextvars.ContextVar('mysql Client contextvar')
request = contextvars.ContextVar('request contextvar')
packageName = contextvars.ContextVar('packageName contextvar')

packageName.set(__package__.split('.')[0])