from django.db import models

class ATACode(models.Model):
    """Base model for tracking commercial aircraft
    ATA codes for coding issues, repairs, etc.
    """
    primary_ata_code = models.PositiveSmallIntegerField()
    secondary_ata_code = models.PositiveSmallIntegerField()
    last_change_date = models.DateField()
    name = models.CharField(max_length=64)
    severity_factor = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('primary_ata_code', 'secondary_ata_code'),)

    def __unicode__(self):
        return '%02d%02d: %s' % (self.primary_ata_code, 
            self.secondary_ata_code, self.name)
