for i in range (0,346,15):
    b = float( i * (m.pi/180))
    print ( "" + str(i) + " --- " + str(round(m.sin(b),4)) + "    " + str(round(m.cos(b),4)))
    