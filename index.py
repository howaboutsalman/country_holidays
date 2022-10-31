from datetime import date

import holidays
varCountry = input('inter a Country: ')
varYear = input('inter a Year: ')

for ptr in holidays.country_holidays(varCountry, years=varYear).items():
    print(ptr)
