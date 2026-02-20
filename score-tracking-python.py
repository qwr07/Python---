score= 0
def add_score(points):
    global score
    if points>7:
     score+=points
    else :
      score+=2

add_score(4)
add_score(8)
add_score(6)
add_score(9)

for i in range(4):
  if score >=25:
   print("ممتازة")
else:
  print("اجتهد اكثر :")


print("النقاط النهائية:",score)



