from fastapi import FastAPI
from app.api import video_routes, ws_routes, webrtc_routes
from app.core.config import settings

# 整個 API Server 的入口
# When running: uvicorn app.main:app --reload
app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def root():
    # 健康檢查用
    return {"msg": "api-server running"}

# REST routes
app.include_router(video_routes.router)

# WebSocket routes
app.include_router(ws_routes.router)

# WebRTC signaling routes
app.include_router(webrtc_routes.router)