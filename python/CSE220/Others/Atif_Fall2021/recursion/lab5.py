class FinalQ:
    def print(self,array,idx):
        if idx<len(array):
            p=self.calcProfit(array[idx])
            print('{}. Investment: {}; Profit: {}'.format(idx+1,array[idx],p))
            self.print(array,idx+1)
    def calcProfit(self,investment):
        if investment<=25000:
            return 0.0
        n=investment-100000
        n=n/100
        n=(n+n+n+n+n+n+n+n)
        return n+3375.0
array = [25000,100000,250000,350000]
f=FinalQ()
f.print(array,0)