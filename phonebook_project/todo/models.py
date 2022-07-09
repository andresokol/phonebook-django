from django.db import models


class TodoTask(models.Model):
    title = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"[{'x' if self.is_done else ' '}] {self.title}"
