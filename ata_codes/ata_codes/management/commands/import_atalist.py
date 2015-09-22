from ata_codes.models import ATACode

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

import csv
import datetime
#/home/dcbrowne/repos/django-ata-codes/ata_codes/ata_codes/import_support/Atalist.csv
class Command(BaseCommand):
    args = '<filename>'
    help = 'Imports and updates ATA Code database based on export from http://www.aviationsupport.com/misc/ATA/Atalist.asp'
    
    def handle(self, *args, **options):
        f = open(args[0])
        r = csv.reader(f)
        headers = r.next()
        
        updated_count = 0
        unchanged_count = 0
        new_count = 0

        for row in r:
            # parse row from CSV
            primary_ata = int(row[0][:2])
            secondary_ata = int(row[0][2:])
            last_date = datetime.datetime.strptime(row[1], '%m/%d/%Y').date()
            name = row[2]
            severity_factor = int(row[3])
            
            # check database for existing item
            try:
                ata_code = ATACode.objects.get(primary_ata_code=primary_ata,
                    secondary_ata_code=secondary_ata)
                if ata_code.last_change_date != last_date:
                    ata_code.name = name
                    ata_code.severity_factor = severity_factor
                    ata_code.name = name
                    ata_code.save()
                    updated_count += 1
                else:
                    unchanged_count += 1
            
            except ObjectDoesNotExist:
                ata_code = ATACode(primary_ata_code=primary_ata,
                                   secondary_ata_code=secondary_ata,
                                   last_change_date=last_date,
                                   name=name,
                                   severity_factor=severity_factor)
                ata_code.save()
                new_count += 1
        f.close()

        self.stdout.write('Succesffully imported ATA Codes.' \
            '\n\tAdded: %d\n\tUpdated: %d\n\tUnchanged:%d' % (
                new_count, updated_count, unchanged_count))

