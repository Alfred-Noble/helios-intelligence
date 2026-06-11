from pydantic import BaseModel


class UploadSummary(BaseModel):
    rows_processed: int
    rows_inserted: int
    duplicates_skipped: int