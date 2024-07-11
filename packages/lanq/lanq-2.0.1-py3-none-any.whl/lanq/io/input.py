from typing import Optional, List
from pydantic import BaseModel


class InputModel(BaseModel):
    """
    Input model, output of converter.
    """
    data_id: str
    prompt: str
    content: str


class RawInputModel(BaseModel):
    """
    Dataset model, output of converter.
    """
    dataset_id: Optional[str] = None
    eval_models: List[str]
    input_path: str
    output_path: Optional[str] = None
    data_type: str
    column_content: Optional[List[str]] = None
    column_id: Optional[List[str]] = None
    column_prompt: Optional[List[str]] = None
    custom_config_path: Optional[str] = None