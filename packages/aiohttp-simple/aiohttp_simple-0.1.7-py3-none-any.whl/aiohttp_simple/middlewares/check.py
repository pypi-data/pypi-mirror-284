from aiohttp.web import middleware
from pydantic import ValidationError
from aiohttp_simple.template import error_response


@middleware
async def check_request_params(request, handler):
    try:
        response = await handler(request)
        return response
    except ValidationError as e:
        return error_response(code="0001", body=e.errors(), message="参数校验失败")
