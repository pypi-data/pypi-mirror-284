import time
import httpx
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.background import BackgroundTasks
import logging

logger = logging.getLogger("fastapi_whowhywhen")

class WhoWhyWhenMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, api_key: str):
        super().__init__(app)
        self.api_key = api_key

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        response_time = time.time() - start_time

        log_data = {
            "url": str(request.url),
            "ip_address": request.headers.get("X-Forwarded-For", request.client.host),
            "user_agent": request.headers.get("User-Agent", ""),
            "response_code": response.status_code,
            "response_time": response_time
        }

        request.state.background_tasks.add_task(self.send_log_to_whowhywhen, log_data)
        return response

    async def send_log_to_whowhywhen(self, log_data):
        whowhywhen_api_url = "https://api.whowhywhen.com/api/log"
        headers = {"X-Api-Key": self.api_key}

        async with httpx.AsyncClient() as client:
            try:
                await client.post(
                    whowhywhen_api_url,
                    headers=headers,
                    json=log_data,
                    timeout=2  # Adjust the timeout as needed
                )
            except httpx.HTTPStatusError as exc:
                logger.error(f"Error sending log to WhoWhyWhen: {exc.response.status_code} - {exc.response.text}")
            except Exception as exc:
                logger.error(f"Error sending log to WhoWhyWhen: {str(exc)}")
