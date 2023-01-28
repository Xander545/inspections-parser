from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from main.models import (
    InspectionSource,
    Company,
    Region,
    InspectionType,
    InspectionStatus,
    Inspection
)

import requests
from bs4 import BeautifulSoup

import hashlib
from datetime import datetime

class Command(BaseCommand):
    help = 'Rospotreb inspection loader'

    def get_data(self):
        # source settings
        source = InspectionSource.objects.get(code='rospotreb')
        
        mapping = {
            'f715de51fa7f2b476189ac3bfcc715222aace9aa': 'inn',
            '11b1b3c6def777aaa7006c3df7df716348dbec27': 'date_inspection_start',
            '0222edcc9ae867ff06e1e4b6306ae0d812273849': 'company_name',
            '002731eabf75a75d4e14b729293fa141f029885b': 'inspection_state',
            'dc105b6ab0a88b8b0a8fc15ac04eb61574a47ff0': 'inspection_place',
            '11ca794b6bd990d90ed8bb57bc130f206975a0ff': 'inspection_form',
        }        

        # get first page
        page = requests.get(source.url)
        parsed_page = BeautifulSoup(
            page.text,
            features="html.parser"
            )
        data_table = parsed_page.find('table', {'class': 'tlist'})
        rows = data_table.find_all('tr')

        parsed_data = []
        field = {}

        for row in rows:
            if row.find('hr'):
                if field:
                    parsed_data.append(field)
                    field = {'number': row.text}
                else:
                    field = {'number': row.text}
            else:
                columns = row.find_all('td')
                param_value = columns[1].text
                param_name = columns[0].text
                param_name_hash = hashlib.sha1(param_name.encode()).hexdigest()

                if param_name_hash in mapping:
                    field[mapping[param_name_hash]] = param_value

        parsed_data.append(field)

        # Some strange default values
        region = Region.objects.get(id=1)
        type = InspectionType.objects.get(id=1)
        status = InspectionStatus.objects.get(id=1)        

        # Load parsed data in database
        for dt in  parsed_data:
            try:
                c = Company.objects.get(inn=dt['inn'])
            except Company.DoesNotExist:
                c = Company(
                    inn=dt['inn'], 
                    company_name=dt['company_name'])
                c.save()

            inspect = Inspection(
                inspection_date=make_aware(
                    datetime.strptime(
                        dt['date_inspection_start'][:10], 
                        "%d.%m.%Y")),
                inspection_place=dt['inspection_place'][:490],
                company=c,
                source=source,
                region=region,
                type=type,
                status=status,
            )

            inspect.save()

    def handle(self, *args, **options):
        self.get_data()