import instaloader
IG = instaloader.Instaloader()
cybersecurity = input("Enter the username instagram > ")
IG.download_profile(cybersecurity, profile_pic_only=True)
