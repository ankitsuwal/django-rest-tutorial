from django.db import models

# Create your models here.


# Create your models here.
class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

