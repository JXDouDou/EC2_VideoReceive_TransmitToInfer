# app/services/ws_manager.py

from fastapi import WebSocket
from typing import List


class ConnectionManager:
    """
    管理所有 WebSocket 連線
    """

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        # 安全移除：避免重複 disconnect 時噴 ValueError
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_json(self, websocket: WebSocket, data: dict):
        await websocket.send_json(data)