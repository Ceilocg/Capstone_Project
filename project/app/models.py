from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

class RequestNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
class CertificateRequest(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    certificate_type = models.CharField(max_length=50)
    reason = models.TextField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='Pending')  # e.g., 'Pending', 'Approved', 'Rejected'
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.certificate_type}"
    
class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')  # Stores the file in the 'media/excel_files/' folder
    name = models.CharField(max_length=255)  # Name of the file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the upload date

    def __str__(self):
        return self.name
