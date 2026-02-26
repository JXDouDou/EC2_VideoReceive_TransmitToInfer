from fastapi import APIRouter

# 先保留 signaling router 入口，後續再放 SDP offer/answer
router = APIRouter(prefix="/webrtc", tags=["webrtc"])


@router.get("/health")
async def webrtc_health():
	# 占位檢查點，確認 webrtc router 已掛載
	return {"status": "webrtc route ready"}
