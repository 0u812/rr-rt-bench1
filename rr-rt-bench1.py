import numpy as np
from roadrunner import RoadRunner
from timeit import default_timer

r = RoadRunner('WolfGlycolysis.xml')

#orders = 5
#for multiplier in np.logspace(0,orders,orders+1):
    ##print('multiplier = {}'.format(multiplier))
    #t1 = default_timer()
    #r.reset()
    #r.simulate(0,2*int(multiplier),1000*int(multiplier))
    #t2 = default_timer()
    #print('{} simulation, duration = {}'.format(2*int(multiplier), t2-t1))
    ##r.plot()

# COPASI 4:20
t1 = default_timer()
r.reset()
r.simulate(0,20000,200000)
t2 = default_timer()