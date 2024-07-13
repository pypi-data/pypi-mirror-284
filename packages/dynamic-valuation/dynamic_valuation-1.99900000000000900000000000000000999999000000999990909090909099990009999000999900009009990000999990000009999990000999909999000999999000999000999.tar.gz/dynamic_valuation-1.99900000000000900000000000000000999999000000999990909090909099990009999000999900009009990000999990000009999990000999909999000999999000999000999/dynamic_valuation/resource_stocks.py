class Fishery:
    """
 def __init__(self,
                 s_min=1,
                 s_max=int(3.59e8),
                 freq=1,
                 δ=.02,
                 q=3.17e-4,
                 α=.544,
                 γ=.7882,
                 y=.157,
                 m=2.7,
                 c=153,
                 K=int(3.59e8),
                 z=1,
                 n=99,
                 r=.3847,
                 policy_bound=3.5e9):
                


        self.δ=δ
        self.β=np.exp(-δ/freq)
        self.freq=freq
        self.q=q
        self.α=α
        self.γ=γ
        self.y=y
        self.m=m
        self.c=c
        self.K=K
        self.s_min=s_min
        self.s_max=s_max
        self.z=z
        self.n=n
        self.r=r
        self.ds=(self.s_max-self.s_min)/(self.n-2)
        self.policy_bound=policy_bound
        self.eq=root(lambda s: self.sdot(s,self.x(s)),bracket=[self.s_min,self.s_max],method='brentq').root
        self.veq=(self.W(self.eq,self.x(self.eq)))/((self.freq)*(1-self.β))
        self.s_grid=np.append(np.append(np.arange(self.s_min, self.eq, self.ds),np.arange(self.eq,self.s_max,self.ds)),self.s_max)

    def x(self,s):

      return (self.y*s**self.γ)

    def f(self,s):
      return self.r*s*(1-s/self.K)
#this is per period growth
    def h(self,s,x):
      return ((self.q*s**self.z)*(x)**self.α)
#this is per period harvest as a function of the per period effort
    def sdot(self,s,x):
      return self.f(s)-self.h(s,x)
    def W(self,s,x):
      return (self.m*self.h(s,x)-self.c*x)





    This is a class that has all the parameters of the main fishery valuation in Fenichel & Abbott 2024
    to see the basic parameters: Fishy__

  c: the cost of a unit of a effort
  ds: the mesh size of the s_grid
  eq: the equilibrium of the fishery
  f: the growth rate of the fish stock as a function of the the fish stock
  freq: 1 is yearly, 12 is monthly, 365 is daily. 
  h: amount of fish harvest
  m: price of a unit of fish
  n: number of points in the s_grid
  policy_bound: this is the maximum that the policy function can take. In this case the maximum
  rate of fishing effort
  q:
 'r',
 's_grid',
 's_max',
 's_min',
 'sdot',
 'veq',
  x: fishing effort
 'y',
 'z',
 'α',
 'β',
 'γ',
 'δ'

    """
    def __init__(self,
                 s_min=1,
                 s_max=int(3.59e8),
                 freq=1,
                 δ=.02,
                 q=3.17e-4,
                 α=.544,
                 γ=.7882,
                 y=.157,
                 m=2.7,
                 c=153,
                 K=int(3.59e8),
                 z=1,
                 n=99,
                 r=.3847,
                 policy_bound=3.5e9):
                


        self.δ=δ
        self.β=np.exp(-δ/freq)
        self.freq=freq
        self.q=q
        self.α=α
        self.γ=γ
        self.y=y
        self.m=m
        self.c=c
        self.K=K
        self.s_min=s_min
        self.s_max=s_max
        self.z=z
        self.n=n
        self.r=r
        self.ds=(self.s_max-self.s_min)/(self.n-2)
        self.policy_bound=policy_bound
        self.eq=root(lambda s: self.sdot(s,self.x(s)),bracket=[self.s_min,self.s_max],method='brentq').root
        self.veq=(self.W(self.eq,self.x(self.eq)))/((self.freq)*(1-self.β))
        self.s_grid=np.append(np.append(np.arange(self.s_min, self.eq, self.ds),np.arange(self.eq,self.s_max,self.ds)),self.s_max)

    def x(self,s):

      return (self.y*s**self.γ)

    def f(self,s):
      return self.r*s*(1-s/self.K)
#this is per period growth
    def h(self,s,x):
      return ((self.q*s**self.z)*(x)**self.α)
#this is per period harvest as a function of the per period effort
    def sdot(self,s,x):
      return self.f(s)-self.h(s,x)
    def W(self,s,x):
      return (self.m*self.h(s,x)-self.c*x)



#####
