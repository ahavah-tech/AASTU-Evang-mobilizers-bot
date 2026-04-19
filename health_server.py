"""
Health server for Kuberns deployment monitoring.
Provides /health endpoint on port 8080 while the Telegram bot runs.
"""
import os
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse, PlainTextResponse


async def health(request):
    return JSONResponse({"status": "healthy", "service": "telegram-bot"})


async def root(request):
    return PlainTextResponse("OK", status_code=200)


app = Starlette(routes=[
    Route("/", root),
    Route("/health", health),
])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
