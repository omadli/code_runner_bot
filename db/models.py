from tortoise.models import Model
from tortoise import fields

class DbUser(Model):
    uuid = fields.UUIDField(pk=True)
    id = fields.BigIntField(unique=True, index=True)
    full_name = fields.CharField(max_length=255)
    username = fields.CharField(max_length=255, null=True)
    join_date = fields.DatetimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.id} {self.full_name}"
