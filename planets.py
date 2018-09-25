#lab0
def weight_on_planets():
   mass = int(input("What do you weigh on earth? "))
   Mars = mass*0.38
   Jupiter = mass*2.34
   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (Mars, Jupiter))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
