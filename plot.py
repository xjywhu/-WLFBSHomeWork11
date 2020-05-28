import matplotlib.pyplot as plt
import numpy as np
def pure_ALOHA(N,P):
    return N*P*(1-P)**(2*(N-1))
P = np.arange(0, 1, 0.001)
y1 = pure_ALOHA(15,P)
y2 = pure_ALOHA(25,P)
y3 = pure_ALOHA(35,P)
plt.title('Pure ALOHA')
plt.xlabel('Efficiency')
plt.ylabel('Probability')
plt.plot(P,y1,color = 'r',label = 'N=15')
plt.plot(P,y2,color = 'g',label = 'N=25')
plt.plot(P,y3,color = 'b',label = 'N=35')
plt.legend(loc=' best')
plt.show()