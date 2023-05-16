# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import SeamEnvironment
from ..action_attempts.types.action_attempt import ActionAttempt
from .types.create_access_code_response import CreateAccessCodeResponse
from .types.update_access_code_response import UpdateAccessCodeResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AccessCodesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    def create(
        self,
        *,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        code: typing.Optional[str] = OMIT,
        common_code_key: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
    ) -> CreateAccessCodeResponse:
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if common_code_key is not OMIT:
            _request["common_code_key"] = common_code_key
        if sync is not OMIT:
            _request["sync"] = sync
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/create"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAccessCodeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        *,
        access_code_id: str,
        name: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
    ) -> UpdateAccessCodeResponse:
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if name is not OMIT:
            _request["name"] = name
        if code is not OMIT:
            _request["code"] = code
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/update"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateAccessCodeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, *, access_code_id: str) -> ActionAttempt:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/delete"),
            params={"access_code_id": access_code_id},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ActionAttempt, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAccessCodesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    async def create(
        self,
        *,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        code: typing.Optional[str] = OMIT,
        common_code_key: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
    ) -> CreateAccessCodeResponse:
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if common_code_key is not OMIT:
            _request["common_code_key"] = common_code_key
        if sync is not OMIT:
            _request["sync"] = sync
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/create"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateAccessCodeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        *,
        access_code_id: str,
        name: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
    ) -> UpdateAccessCodeResponse:
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if name is not OMIT:
            _request["name"] = name
        if code is not OMIT:
            _request["code"] = code
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/update"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateAccessCodeResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, *, access_code_id: str) -> ActionAttempt:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", "acccess_codes/delete"),
                params={"access_code_id": access_code_id},
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ActionAttempt, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
