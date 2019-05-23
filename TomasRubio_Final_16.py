import numpy as np

x_barcos = np.array([4,10,12,80,50,40])
y_barcos = np.array([100,5,80,50,50,200])
ts = np.array([3673,3628,3659,3652,3639,3737])
dt = 1;

def logprior(v,x,y,t):
    if v > 5000 or v < 360:
        return 0
    elif t > 3800 or t < 0:
        return 0
    else:
        return 1

def loglikelihood(v,x,y,t):
    distx = x_barcos-x
    disty = y_barcos-y
    dist = np.sqrt(distx**2+disty**2)
    epsilon = dist - v*(ts-t)
    chi2 = np.square(np.divide(epsilon,v*1))
    return -(1/2)*np.sum(chi2)

def mcmc(n_points):
    N = n_points
    v = [1000]
    x = [1.0*np.random.randint(-100,100)]
    y = [1.0*np.random.randint(-100,100)]
    t = [0.0]
    for i in range(N):
        x_new = x[i] + np.random.normal(loc=0,scale=10)
        y_new = y[i] + np.random.normal(loc=0,scale=10)
        v_new = v[i] + np.random.normal(loc=0,scale=10)
        t_new = t[i] + np.random.normal(loc=0,scale=50)
        
        logViejo = loglikelihood(v[i],x[i],y[i],t[i]) + logprior(v[i],x[i],y[i],t[i])
        logNuevo = loglikelihood(v_new,x_new,y_new,t_new) + logprior(v_new,x_new,y_new,t_new)
        
        dif = logNuevo-logViejo
        
        if dif > 0: # Preferí verificar directamente sobre log(P) porque el exponencial explotaba
            r = 1
        else:
            r = np.exp(dif)

        if(r>np.random.rand()):
            v.append(v_new)
            x.append(x_new)
            y.append(y_new)
        else:
            v.append(v[i])
            x.append(x[i])
            y.append(y[i])
    
    vfin = np.mean(np.array(v))
    sigmav = np.std(np.array(v))
    xfin = np.mean(np.array(x))
    sigmax = np.std(np.array(x))
    yfin = np.mean(np.array(y))
    sigmay = np.std(np.array(y))
    return vfin,sigmav,xfin,sigmax,yfin,sigmay

v,sv,x,sx,y,sy = mcmc(1000)

print("coordenada x:",x,"+/-",sx)
print("coordenada y:",y,"+/-",sy)
print("tiempo lanzamiento:","+/-",)
print("velocidad del sonido:",v,"+/-",sv)