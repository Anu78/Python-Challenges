with open("contacts.vcf") as f:
    contacts = f.read().strip().split("\n")

names = []

name = ""
number = ""

for contact in contacts:
    if 'FN' in contact:
        name = contact.split(':')[-1]
    if 'CELL' in contact:
        number = contact.split(':')[-1]
    if contact == "END:VCARD":
        names.append("{}, {}".format(name,number))

for name in names:
    print(name)