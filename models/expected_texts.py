from pydantic import BaseModel


class ExpectedTexts(BaseModel):
    simple_alert: str
    confirm_alert: str
    confirm_result_ok: str
    prompt_alert: str
