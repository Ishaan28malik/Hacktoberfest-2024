import phonenumbers
from phonenumbers import timezone
from phonenumbers import carrier
from phonenumbers import geocoder

mob = phonenumbers.parse('+447986')

car = carrier.name_for_number(mob, 'en')
print(car)

location = geocoder.country_name_for_number(mob, 'en')
print(location)

tz = timezone.time_zones_for_geographical_number(mob)
print(tz)

# is number already registered
x = phonenumbers.is_valid_number(mob)
print(x)

# can be the number registered
y = phonenumbers.is_possible_number(mob)
print(y)


text = 'hii my name is xyz and my phone  number is +916387873015'

for match in phonenumbers.phonenumbermatcher(text, 'US'):
    print(match)