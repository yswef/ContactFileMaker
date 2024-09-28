name = input("enter name\n")
contact = input("enter namber\n")

with open("your contact.vcf" , "a") as keep  :
    keep.write("BEGIN:VCARD\n")
    keep.write("N:" + name + "\n")
    keep.write("TEL:" + contact + "\n")
    keep.write("END:VCARD\n\n")



