# app/api/ws_routes.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.ws_manager import ConnectionManager
from app.services.inference_client import InferenceClient

router = APIRouter()
manager = ConnectionManager()
client = InferenceClient()


@router.websocket("/ws/stream")
async def websocket_stream(websocket: WebSocket):
    """
    接收 Edge 連續傳來的 frame
    """
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_bytes()

            # 傳給 ai-server
            result = await client.predict(data)

            # 回傳推論結果
            await manager.send_json(websocket, result)

    except WebSocketDisconnect:
        pass

    finally:
        manager.disconnect(websocket)