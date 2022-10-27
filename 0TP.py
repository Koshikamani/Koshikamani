import random
otp=random.randrange(0,10000)
print("YOUR ONE TIME PASSWORD IS:",otp)
mani=int(input("enter above 0TP:"))
if otp==mani:
	print("**successfully entered above OTP **")
        print("\nNOTE:Don't share this OTP with any one")



else:
	print("**access not granted **")



password=input("\nenter your password:")
print("\nWE WILL SAVE YOUR PASSWORD:",password)
print("SECURITY TIP : MAKE SURE THAT YOUR PASSWORD SHOULD BE STONG BY USING ALL CHARACTERS ")
