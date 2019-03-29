#Оценить распределение выборочного среднего случайной величины при разных объёмах выборок;
#При трёх и более значениях n сгенерировать 1000 выборок объёма n;

def beta_to_normal_approx(n,mu,sigma):
    values = np.array([rv_beta.rvs(n) for x in range(1000)])
    mean_vals = values.mean(axis = 1)
    
    #Постройть гистограммы распределений их выборочных средних;
    plt.hist(mean_vals, density=True, alpha=0.4, label='Hist Mean n - %s' % n)
    
    #Наносим нормальное распределение
    norm_rv = norm(mu,sigma)
    x = np.linspace(0,1,100)
    pdf = norm_rv.pdf(x)
    plt.plot(x,pdf,label='Samples Beta PDF = %s' % str(n))
    plt.legend()

#Параметр среднего для нормального распределения
mu = rv_beta.mean()

#Список значений n
list_nSamples = [2,4,8,31]

for nSamples in list_nSamples:
    #Параметр сигма для нормального распределения
    sigma = sqrt(rv_beta.var()/nSamples)
    beta_to_normal_approx(nSamples,mu,sigma)
    
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
