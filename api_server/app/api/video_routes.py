# app/api/video_routes.py

from fastapi import APIRouter, UploadFile, File
from app.services.inference_client import InferenceClient

router = APIRouter()
client = InferenceClient()


@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """
    接收 Edge 上傳的圖片
    """
    image_bytes = await file.read()

    # 呼叫 ai-server
    result = await client.predict(image_bytes)

    return {
        "status": "ok",
        "inference": result
    }