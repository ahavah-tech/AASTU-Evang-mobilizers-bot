"""
Health server for Kuberns deployment monitoring.
Provides /health endpoint on port 8080 while the Telegram bot runs.
"""
import os
import threading
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


async def health(request):
    return JSONResponse({"status": "healthy", "service": "telegram-bot"})


app = Starlette(routes=[Route("/health", health)])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
