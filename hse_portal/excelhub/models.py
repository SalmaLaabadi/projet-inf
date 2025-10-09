from django.db import models

class DailyWorkbook(models.Model):
    date = models.DateField(db_index=True, unique=True)
    kind = models.CharField(max_length=50, default="tests")
    file = models.FileField(upload_to="excel/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.file.name}"

class DailyWorkbookVersion(models.Model):
    workbook = models.ForeignKey(DailyWorkbook, on_delete=models.CASCADE, related_name="versions")
    version = models.PositiveIntegerField()
    file = models.FileField(upload_to="excel_versions/%Y/%m/%d/")
    saved_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("workbook", "version")

    def __str__(self):
        return f"{self.workbook.date} v{self.version}"
