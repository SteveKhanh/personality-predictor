from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Khởi tạo FastAPI
app = FastAPI(
    title="Personality Classifier API",
    description="Dự đoán Introvert hoặc Extrovert từ dữ liệu hành vi xã hội."
)

# Load pipeline và mô hình đã lưu
try:
    model = joblib.load("../models/model.joblib")
    pipeline = joblib.load("../models/pipeline.joblib")
except Exception as e:
    print(f"Lỗi khi tải pipeline hoặc model: {e}")

# Gán nhãn dự đoán (0 → Introvert, 1 → Extrovert)
labels = ["Introvert", "Extrovert"]

# Lớp đại diện cho dữ liệu đầu vào
class PersonalityInput(BaseModel):
    Time_spent_Alone: float
    Social_event_attendance: float
    Going_outside: float
    Friends_circle_size: float
    Post_frequency: float
    Stage_fear: str
    Drained_after_socializing: str

    class Config:
        schema_extra = {
            "example": {
                "Time_spent_Alone": 4,
                "Social_event_attendance": 2,
                "Going_outside": 3,
                "Friends_circle_size": 6,
                "Post_frequency": 2,
                "Stage_fear": "Yes",
                "Drained_after_socializing": "Yes"
            }
        }

# Trang chủ
@app.get("/")
def read_root():
    return {"message": "API dự đoán tính cách (Introvert vs Extrovert). Dùng /predict để gửi dữ liệu."}

# Endpoint dự đoán
@app.post("/predict")
def predict_personality(data: PersonalityInput):
    if not model or not pipeline:
        return {"error": "Model hoặc pipeline chưa được tải."}

    # Tạo DataFrame từ đầu vào
    input_df = pd.DataFrame([data.dict()])

    # Tiền xử lý đầu vào
    processed_input = pipeline.transform(input_df)

    # Dự đoán
    pred_index = model.predict(processed_input)[0]
    prediction = labels[pred_index]

    return {
        "prediction": prediction,
        "class_index": int(pred_index)
    }
