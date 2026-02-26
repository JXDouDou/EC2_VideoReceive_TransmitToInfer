import os


class Settings:
	"""
	集中管理設定值（目前先用 os.getenv）
	Centralized settings for api-server
	"""

	# 顯示在 FastAPI docs 的服務名稱
	APP_NAME = os.getenv("APP_NAME", "API Server (Control Plane)")

	# ai-server 的 WebSocket endpoint（依照 PROJECT_CONTEXT 以 WS 為主）
	AI_SERVER_WS_URL = os.getenv("AI_SERVER_WS_URL", "ws://127.0.0.1:5080/ws/infer")

	# 呼叫 ai-server 的逾時秒數
	AI_SERVER_TIMEOUT_SECONDS = float(os.getenv("AI_SERVER_TIMEOUT_SECONDS", "10"))


# 給其他模組直接匯入使用：from app.core.config import settings
settings = Settings()
