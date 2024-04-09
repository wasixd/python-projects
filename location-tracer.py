import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder0

from phonenumbers import timezone

number = "+923192173398"
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(geocoder.description_for_number(number,"en"))
