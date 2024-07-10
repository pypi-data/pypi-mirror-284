import os
from typing import Optional

import httpx

from .raw_api.client import AuthenticatedClient
from .detection_rule import AsyncDetectionRule, DetectionRule
from .event_sink import AsyncEventSink, EventSink
from .query import AsyncQuery, Query


class Scanner():
    _api_url: str
    _api_key: str
    _client: AuthenticatedClient

    detection_rule: DetectionRule
    event_sink: EventSink
    query: Query


    def __init__(self, api_url: str, api_key: Optional[str] = None) -> None:
        if api_key is None:
            api_key = os.environ.get("SCANNER_API_KEY")

        if api_key is None:
            raise ValueError(
                "No API key provided. Pass `api_key` to the client "
                "or set `SCANNER_API_KEY` environment variable."
            )

        self._api_url = api_url
        self._api_key = api_key
        self._client = AuthenticatedClient(
            base_url=api_url, token=api_key, timeout=httpx.Timeout(60),
        )

        self.detection_rule = DetectionRule(self._client)
        self.event_sink = EventSink(self._client)
        self.query = Query(self._client)


class AsyncScanner():
    _api_url: str
    _api_key: str
    _client: AuthenticatedClient

    detection_rule: AsyncDetectionRule
    event_sink: AsyncEventSink
    query: AsyncQuery


    def __init__(self, api_url: str, api_key: Optional[str] = None) -> None:
        if api_key is None:
            api_key = os.environ.get("SCANNER_API_KEY")

        if api_key is None:
            raise ValueError(
                "No API key provided. Pass `api_key` to the client "
                "or set `SCANNER_API_KEY` environment variable."
            )

        self._api_url = api_url
        self._api_key = api_key
        self._client = AuthenticatedClient(
            base_url=api_url, token=api_key, timeout=httpx.Timeout(60),
        )

        self.detection_rule = AsyncDetectionRule(self._client)
        self.event_sink = AsyncEventSink(self._client)
        self.query = AsyncQuery(self._client)
