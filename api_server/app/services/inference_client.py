from asyncio import timeout

import websockets
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK

from app.core.config import settings
from app.protocols.websocket_protocol import normalize_inference_response


class InferenceClient:
    """
    InferenceClient = api-server 呼叫 ai-server 的唯一入口（single gateway）
    """

    def __init__(self):
        # 從 config 讀取 ai-server WS URL，不把 endpoint 寫死在業務邏輯
        self.ws_url = settings.AI_SERVER_WS_URL
        self.timeout_seconds = settings.AI_SERVER_TIMEOUT_SECONDS

    async def predict(self, image_bytes: bytes):
        """
        將 frame/image 送到 ai-server（WS）並回傳推論結果
        """
        try:
            # timeout: 防止 ai-server 停機或網路異常造成無限等待
            async with timeout(self.timeout_seconds):
                # 這裡每次請求建立一條短連線，簡單且隔離性高
                async with websockets.connect(self.ws_url) as websocket:
                    # 傳入 binary frame
                    await websocket.send(image_bytes)

                    # 等待 ai-server 推論結果
                    payload = await websocket.recv()

            # 統一包裝成 dict，讓 route 層不用判斷型別
            return normalize_inference_response(payload)

        except TimeoutError:
            return {"error": "AI server timeout"}

        except OSError:
            return {"error": "AI server unreachable"}

        except (ConnectionClosedError, ConnectionClosedOK):
            return {"error": "AI server websocket closed"}

        except Exception:
            return {"error": "AI server unexpected error"}

