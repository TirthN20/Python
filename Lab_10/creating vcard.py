file=open("Vcard.vcf",'w')
name = input("Enter name: ")
phone = int(input("Enter phone: "))
email = input("Enter email: ")
file.write("BEGIN:VCARD\n")
file.write("VERSION:3.0\n")
file.write("N:{name}\n")
file.write("TEL:{phone}\n")
file.write("EMAIL:{email}\n")
file.write("END:VCARD\n")
file.close()




