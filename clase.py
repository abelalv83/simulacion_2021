import matplotlib.pyplot as plt 
import numpy as np 
#import funciones

class aprox_ODE():
    def __init__(self,inputs): ## la calse s eva allamar sai misma
            
            self.imputs=inputs
            self.a=self.imputs['a']
            self.b=self.imputs['b']
            self.N=self.imputs['N']
            self.u0=self.imputs['u0']
            self.t,self.dt=np.linspace(self.a,self.b,self.N,retstep=True)
            self.u=np.zeros(self.N)

    def Euler(self,f):
        self.u[0]=self.u0
        for i in range(self.N-1):
           self.u[i+1]= self.u[i]+ self.dt*f(self.u[i],self.t[i]) #explicito
    


    #grafica de la solucion 
    def grafica(self):
        u=self.u
        t=self.t
        plt.plot(t,u)
        plt.title('Aproximation')
        plt.show()
