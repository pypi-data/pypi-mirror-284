from typing import Union, Optional, Dict, Any

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from fastgenerateapi.settings.register_settings import settings
from starlette.background import BackgroundTask
from starlette.responses import JSONResponse, Response

from fastgenerateapi.pydantic_utils.base_model import JSON_ENCODERS
from fastgenerateapi.schemas_factory import response_factory


# class CustomSuccessJsonResponse(JSONResponse):
#     def __init__(self, content: Any, *args, **kwargs):
#         if not isinstance(content, Response) or not (hasattr(content, "success") or hasattr(content, "code")):
#             if isinstance(content, dict) and ("success" in content or "code" in content):
#                 super().__init__(content, *args, **kwargs)
#             else:
#                 content = response_factory()(**{
#                     "success": True,
#                     "code": settings.app_settings.CODE_SUCCESS_DEFAULT_VALUE,
#                     settings.app_settings.MESSAGE_RESPONSE_FIELD: "请求成功",
#                     "data": content
#                 })
#                 super().__init__(content.dict(), *args, **kwargs)


class ResponseMixin:

    @staticmethod
    def success(msg: str = "请求成功",
                status_code: int = 200,
                code: Optional[int] = None,
                data: Union[BaseModel, dict, str, None] = None,
                background: Optional[BackgroundTask] = None,
                *args,
                **kwargs):
        if data is None:
            json_compatible_data = {}
        else:
            json_compatible_data = jsonable_encoder(data, custom_encoder=JSON_ENCODERS)
        if code is None:
            code = settings.app_settings.CODE_SUCCESS_DEFAULT_VALUE
        resp = response_factory()(**{
            "success": True,
            "code": code,
            settings.app_settings.MESSAGE_RESPONSE_FIELD: msg,
            "data": json_compatible_data
        })
        kwargs.update(resp.dict())
        return JSONResponse(kwargs, status_code=status_code, background=background)

    @staticmethod
    def fail(msg: str = "请求失败",
             status_code: int = 200,
             code: Optional[int] = None,
             # success: bool = False,
             data: Union[BaseModel, dict, str, None] = None,
             background: Optional[BackgroundTask] = None,
             headers: Optional[Dict[str, Any]] = None,
             *args,
             **kwargs):

        if data is None:
            json_compatible_data = {}
        else:
            json_compatible_data = jsonable_encoder(data, custom_encoder=JSON_ENCODERS)
        if code is None:
            code = settings.app_settings.CODE_FAIL_DEFAULT_VALUE
        resp = response_factory()(**{
            "success": False,
            "code": code,
            settings.app_settings.MESSAGE_RESPONSE_FIELD: msg,
            "data": json_compatible_data
        })
        kwargs.update(resp.dict())
        return JSONResponse(
            kwargs,
            status_code=status_code,
            headers=headers or {"Access-Control-Allow-Origin": '*'},
            background=background
        )

    @staticmethod
    def error(msg: str = "系统繁忙，请稍后再试...",
              status_code: int = 400,
              headers: Optional[Dict[str, Any]] = None,
              *args,
              **kwargs):

        raise HTTPException(
            status_code=status_code,
            detail=msg,
            headers=headers or {"Access-Control-Allow-Origin": '*'},
        )
