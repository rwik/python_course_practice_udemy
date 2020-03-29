# Class definition goes here
class MobilePhone:
    display_size = 0
    ram = 0
    os = 0

    def __init__(self,param1,param2,param3):
        self.display_size = param1
        self.ram = param2
        self.os = param3


pearphone = MobilePhone(5.5, "3GB", "yOS 11.2")
simsun = MobilePhone(5.4, "4GB", "Cyborg 8.1")
print(f"The new Pear phone has a {pearphone.display_size}"
      f" inch display. {pearphone.ram} of RAM and runs on "
      f"the latest version of {pearphone.os}. Its biggest competitor is "
      f"the Simsun phone which sports a similar AMOLED {simsun.display_size} "
      f"inch display, {simsun.ram} of RAM and runs {simsun.os}."
      )
