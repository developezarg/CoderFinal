from django.db import models

#Prevención de emails duplicados
class Registro_email(models.Model):
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email
