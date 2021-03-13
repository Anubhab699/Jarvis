import rotatescreen
screen=rotatescreen.get_primary_display()
screen.rotate_to(0)
for i in range(1):
   screen.rotate_to(i*90)