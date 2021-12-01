from django.db import models


class Data(models.Model):
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    luminosity = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'PK: {self.pk} - Temperature: {self.temperature} - Humidity: {self.humidity} - Luminosity: {self.luminosity} - Date and time: {self.date}-{self.time}'

    class Meta:
        verbose_name = 'Dado'
        verbose_name_plural = 'Dados'