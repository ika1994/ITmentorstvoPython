import re

pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"

mail="test@mail.net"

if re.match(pattern, mail):
    print("true")
else:
    print("false")