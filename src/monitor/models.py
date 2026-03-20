from django.db import models

# Create your models here.
from django.db import models

class BuildJob(models.Model):
    STATUS_CHOICES = [
        ('passing', 'Passing'),
        ('failing', 'Failing'),
        ('running', 'Running'),
    ]
    run_id       = models.BigIntegerField(unique=True, null=True, blank=True)
    name         = models.CharField(max_length=200)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='running')
    branch       = models.CharField(max_length=100, default='main')
    triggered_by = models.CharField(max_length=100, default='push')
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    logs         = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} — {self.status}"

    class Meta:
        ordering = ['-created_at']