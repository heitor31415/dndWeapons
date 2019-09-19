import numpy as np
import matplotlib.pyplot as plt
import dice


class item:
    
    maxCA=30
    
    def __init__(self, name='Sword', damage='1d6', bonus=0):
        self.name=name
        self.damage=damage+'+'+str(bonus)
        self.bonus=bonus
        
        self.minDamage=dice.roll_min(self.damage)
        self.maxDamage=dice.roll_max(self.damage)
        self.averageDamage=np.zeros(self.maxCA)
        
    def AverageDamage(self, armorClass):
        iterations=10000
        damageRoll=np.random.randint(self.minDamage,self.maxDamage,iterations)
        attackRoll=np.random.randint(0,20,iterations)+self.bonus-armorClass-1
        hitArray=attackRoll.clip(min=0, max=1)*damageRoll
        
        return hitArray.mean()
                
        
    def plotDamage(self):
        for i in range(self.maxCA):
            self.averageDamage[i]=self.AverageDamage(i)
            
        plt.plot(self.averageDamage)
        
        
            
        