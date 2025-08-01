from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name="Document Name")
    document = models.FileField(verbose_name="Documents", upload_to="documents/")

    def __str__(self):
        return str(self.id)
