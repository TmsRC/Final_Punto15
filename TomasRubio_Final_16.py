import numpy as np

x_barcos = np.array([4,10,12,80,50,40])
y_barcos = np.array([100,5,80,50,50,200])
t = np.array([3673,3628,3659,3652,3639,3737])
dt = 1;

def logprior(v,x,y):
    if v > 10000 or v < 360:
        return 0

def loglikelihood(v,x,y):
    distx = x_barcos-x
    disty = y_barcos-y
    dist = np.sqrt(distx**2+disty**2)
    epsilon = np.abs(dist - v*t)
    chi2 = np.square(np.divide(epsilon,v*1))
    return -(1/2)*np.sum(chi2)

def mcmc(n_points):
    N = n_points
    v = [1000]
    x = [np.random.rand(-100,100)]
    y = [np.random.rand(-100,100)]
    for i in range(N):
        x_new = x[i] + np.random.normal(loc=0,scale=10)
        y_new = y[i] + np.random.normal(loc=0,scale=10)
        v_new = v[i] + np.random.normal(loc=0,scale=10)
        
        logViejo = loglikelihood(v[i],x[i],y[i]) + logprior(v[i],x[i],y[i])
        logViejo = loglikelihood(v_new,x_new,y_new) + logprior(v_new,x_new,y_new)
        
        
        
    return 0

print("coordenada x:","+/-",)
print("coordenada y:","+/-",)
print("tiempo lanzamiento:","+/-",)
print("velocidad del sonido:","+/-",)