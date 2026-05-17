import re

def clean():
    txt = "Tod%^&^&ay^, I want^&* play with 3 frien#ds, whose%^$ are 16@@ year*&(s old, ga(*)me \" 20980 T--=itule \" !"
    x = re.split("[-=!@#$%^&*()_+]", txt)
    print(x)
clean()