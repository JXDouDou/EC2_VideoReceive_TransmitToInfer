import json
from typing import Any


def normalize_inference_response(payload: Any) -> dict:
	"""
	將 ai-server 回傳內容正規化為 dict
	Normalize websocket payload into JSON-like dict
	"""

	# 已經是 dict：直接回傳
	if isinstance(payload, dict):
		return payload

	# bytes -> str（WebSocket 常見 binary/text 混用）
	if isinstance(payload, bytes):
		payload = payload.decode("utf-8", errors="ignore")

	# str 先嘗試當 JSON parse
	if isinstance(payload, str):
		try:
			data = json.loads(payload)
			if isinstance(data, dict):
				return data
			return {"result": data}
		except json.JSONDecodeError:
			return {"result": payload}

	# 其餘型別，包成 result 欄位
	return {"result": payload}
