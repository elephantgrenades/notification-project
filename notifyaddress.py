input_var = raw_input("Please enter a phone number or an email address: ")

file = open("address.txt", "w")
file.write(input_var)
file.close()

print "We will notify", str(input_var), "thank you."

    


