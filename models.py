from django.db import models

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=255, unique=True)
    account_name = models.CharField(max_length=255)
    app_secret_token = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()
