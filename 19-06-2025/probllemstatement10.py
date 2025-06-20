import numpy as np
milage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
length=len(milage)
for i in milage:
    if milage<15:
        print(i)