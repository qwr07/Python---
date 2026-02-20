name = input("اكتب اسمك  :")
password = input("اكتب كلمة السر  :")
if name == "jek" and password == "1234" :
  print("مرحبًا")
elif name == "guest" or password =="0000":
  print("دخول محدود")
else:
  print("مرفوضة")
