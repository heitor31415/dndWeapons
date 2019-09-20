import numpy as np
import matplotlib.pyplot as plt
import dice

class dndChar:
    def __init__(self, attackBonus='0', accuracyBonus='+2', critRoll=20, critDies=1):
        self.atkBonus=attackBonus
        self.acBonus=accuracyBonus
        self.critRoll=critRoll
        self.critDies=critDies

class item:
    
    maxCA=30
    critAlwaysHit=True
    
    def __init__(self, name='Sword', damage='1d6', magicBonus=0, char=dndChar()):
        self.name=name
        self.damage=damage +'+0'
        self.magicBonus=magicBonus
        self.char=char
        
        self.minDamage=dice.roll_min(self.damage)
        self.maxDamage=dice.roll_max(self.damage)
        self.averageDamage=np.zeros(self.maxCA)
        self.plot=None
        
    def AverageDamage(self, armorClass):
        iterations=10000
        damageRoll=np.random.randint(self.minDamage,self.maxDamage+1,iterations)
        attackRoll=np.random.randint(1,21,iterations)
        crits= (attackRoll>=self.char.critRoll)*self.char.critDies
        
        
        attackRoll+=self.magicBonus+dice.roll(self.char.acBonus)-armorClass-1
        hitArray=attackRoll.clip(min=0, max=1)*(damageRoll+dice.roll(self.char.atkBonus))
        
        if self.critAlwaysHit==True:
            hitArray+=damageRoll*crits
        
        return hitArray.mean()
                
        
    def PlotDamage(self, figNum=None):
        for i in range(self.maxCA):
            self.averageDamage[i]=self.AverageDamage(i)
        
        self.plot=plt.plot(self.averageDamage, label=str(self.name))
        plt.xlabel('Enemy CA')
        plt.ylabel('Average Damage')
        
    def CompareDmg(*args):
        plt.figure()
        for i in range(len(args)):
            args[i].PlotDamage()
        plt.legend()
        plt.show()
        
            
