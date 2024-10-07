from tortoise import fields


class BaseModel:
    id = fields.CharField(pk=True, max_length=255)
    code = fields.CharField(max_length=255, db_index=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
