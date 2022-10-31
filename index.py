from datetime import date

import holidays
varCountry = input('inter a Country: ')

for ptr in holidays.country_holidays(varCountry, years=2028).items():
    print(ptr)
