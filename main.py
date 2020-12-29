import phonenumbers
print("Enter your phone number alongwith the country code, For Example, if your number is XXXXXXXX58 and you are from India, then enter '+91XXXXXXX58'")
number = input("Phone Number :")
from phonenumbers import geocoder
Country = phonenumbers.parse(number, "CH")
from phonenumbers import carrier
Provider = phonenumbers.parse(number, "RO")

print("Country : " + geocoder.description_for_number(Country, "en"))
print("Service Provider : " + carrier.name_for_number(Provider, "en"))