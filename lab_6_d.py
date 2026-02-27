import re

text = input("Enter text: ")
matches = re.findall(r"\+?\d[\d\s()-]{9,}", text)

std = []
country_codes = []

# First pass: collect country codes
for m in matches:
    digits = re.sub(r"\D", "", m)
    if len(digits) > 10:
        cc = digits[:-10]
        if cc:
            country_codes.append(cc)

first_cc = country_codes[0] if country_codes else ""

# Second pass: normalize numbers
for m in matches:
    digits = re.sub(r"\D", "", m)
    if len(digits) >= 10:
        cc, local = digits[:-10], digits[-10:]
        if not cc and first_cc:
            cc = first_cc
        std.append("+" + cc + local)
    else:
        std.append("+" + digits)

print(std)