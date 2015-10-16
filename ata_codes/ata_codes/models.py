from django.db import models

class ATACode(models.Model):
    """Base model for tracking commercial aircraft
    ATA codes for coding issues, repairs, etc.
    """
    primary_ata_code = models.PositiveSmallIntegerField(
        verbose_name='Primary ATA Code')
    secondary_ata_code = models.PositiveSmallIntegerField(
        verbose_name='Secondary ATA Code')
    last_change_date = models.DateField()
    name = models.CharField(max_length=64)
    severity_factor = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('primary_ata_code', 'secondary_ata_code'),)
        verbose_name = 'ATA Code'
        ordering = ['primary_ata_code', 'secondary_ata_code', 'name']

    def __unicode__(self):
        return '%02d-%02d: %s' % (self.primary_ata_code, 
            self.secondary_ata_code, self.name)
