from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

router = APIRouter()

class PaymentRequest(BaseModel):
    amount: float
    phone_number: str
    transaction_id: str

class PaymentResponse(BaseModel):
    status: str
    message: str

@router.post("/process_payment", response_model=PaymentResponse)
async def process_payment(payment_request: PaymentRequest):
    # Replace with actual PhonePe API endpoint and headers
    phonepe_api_url = "https://api.phonepe.com/v3/transaction/initiate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_PHONEPE_API_KEY"
    }

    payload = {
        "amount": payment_request.amount,
        "phone_number": payment_request.phone_number,
        "transaction_id": payment_request.transaction_id
    }

    try:
        response = requests.post(phonepe_api_url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            return PaymentResponse(status="success", message="Payment processed successfully")
        else:
            raise HTTPException(status_code=response.status_code, detail=response_data.get("message", "Payment processing failed"))

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))