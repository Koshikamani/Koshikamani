import instaloader
ig=instaloader.Instaloader()

user=input("enter user name:")
ig.download_profile(user,profile_pic=True)