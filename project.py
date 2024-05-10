from tkinter import *
from threading import Timer
from threading import *
from idlelib.tooltip import Hovertip
import atexit
import os.path
from random import randint
totalCitizens = 0
upgradeList = []
idBlockList = []
this = ""
scrapChange = 0
antTendingBoost = 1
millTendingBoost = 1
scrapMultiplier = 1
baseFood = 0
baseScrap = 0
baseWood = 0
enemyTroops = []
yourTroops = []
manPowerMultiplier = 1
stickCost = 65
frameOneContent = 0

names1 = ['Large','Thick','Unholy','Bending','Big','Titanic','Swollen','Pulsing','Long','Thin']
names2 = ['Sword','Knife','Potion','Scythe','Bag','Car']
names3 = ['Night','Day','Time']

troopRolls = {"Stick":4,"Rock":5}
troopRollsEnemy = {"Stick":4,"Rock":5}

mainScreen = Tk()
mainScreen.geometry("600x600")
mainScreen.resizable(False,False)

class Items():
    
    '''
    
    This function creates an item instance that the player owns. These are saved in the save file and carry over.
    
    '''
    
    itemFrame = Frame(mainScreen,background='skyblue')
    itemFrame.forget()
   
    canEquipLabel = Label(itemFrame,text="CAN EQUIP ONLY 3!",bg='red',fg='white')
    canEquipLabel.pack()
   
    def __init__(self,itemName, itemEffect, itemMultiplier) -> None:
        
        '''
        
        This creates the item in question. itemName is the name of the item as shown in the program. itemEffect is the effect of the item (basewood basescrap or baseFood)
        
        itemMultiplier is the amount of the itemEffect that is provided.
        
        itemButton is also created such that items can be equipped
        
        '''
        
        self.__equipped = False
        self.__itemName = itemName
        self.__itemEffect = itemEffect
        self.__itemMultiplier = itemMultiplier
        self.__itemButton = Button(Items.itemFrame,text=f"{self.__itemName}",command=self.buttonClicked,bg='gray')
        self.__itemButton.pack()
        self.__itemTip = Hovertip(self.__itemButton,text=f'PROVIDES: {self.__itemEffect} of {self.__itemMultiplier}')
       
    def buttonClicked(self) -> None:
        
        '''
        
        When clicked, it will check if the item in question is equipped. If it isn't and equipped items is less than 3, the item is equipped
        
        If the item is equipped, then the item will be unequipped and the equipped items number is decremented by 1

        
        '''
        
        global baseFood,baseWood,baseScrap
        if self.__equipped == False:
            if len(itemsEquipped) < 3:
                if self.__itemEffect == "Base Food":
                    baseFood += self.__itemMultiplier
                elif self.__itemEffect == "Base Wood":
                    baseWood += self.__itemMultiplier
                elif self.__itemEffect == "Base Scrap":
                    baseScrap += self.__itemMultiplier
                self.__itemButton.configure(bg='gold')
                itemsEquipped.append(self.__itemName)
                self.__equipped = True
        elif self.__equipped == True:
            if self.__itemEffect == "Base Food":
                    baseFood -= self.__itemMultiplier
            elif self.__itemEffect == "Base Wood":
                baseWood -= self.__itemMultiplier
            elif self.__itemEffect == "Base Scrap":
                baseScrap -= self.__itemMultiplier
           
            self.__itemButton.configure(bg='gray')
            itemsEquipped.remove(self.__itemName)
            self.__equipped = False
    def __str__(self) -> str:
        global this2
        this2 = f'{str(self.__itemName.replace(" ","."))}+|{self.__itemEffect.replace(" ",".")}-|{self.__itemMultiplier}'
        return f'{str(self.__itemName)} {self.__itemEffect} {self.__itemMultiplier}'

if os.path.isfile("saveFile.txt"):
    
    '''

    This portion of the program is ran at the beginning, and it retrieves the data from the save file. If a save file does not exist, then
    
    Default values are set such that the game is beginning


    '''
    with open("saveFile.txt",'r') as f:
        dataList = f.read().split()
       
        print(dataList[0])
        print(dataList[1])
        print(dataList[2])
        print(dataList)
        totalFood = float(dataList[0])
        totalWood = float(dataList[1])
        antTrapAmount = float(dataList[2])
        woodMillAmount = float(dataList[3])
        ownedAntTraps = float(dataList[2])
        ownedWoodMills = float(dataList[3])
        smallShackAmount = float(dataList[4])
        upgradeOneBought = dataList[5]
        boxAmount = float(dataList[7])
        totalScrap = float(dataList[9])
        manPower = float(dataList[11])
        stickWielders = int(dataList[13])
        boxBenefit = 100
        print(upgradeOneBought)
        itemList = []
       
        if boxAmount >= 1:
            boxNow = True
            boxPrice1 = 100 + (5*boxAmount)
            boxPrice2 = 10 + (0.5*boxAmount)
            maxWood = 2000 + (boxBenefit*boxAmount)
            maxFood = 2000 + (boxBenefit*boxAmount)
        else:
            boxNow = False
            boxPrice1 = 100
            boxPrice2 = 10
            maxWood = 2000
            maxFood = 2000
       
        if ownedAntTraps >= 1:
            antTrapNow = True
            antTrapPrice = 25 + (2*antTrapAmount)
        else:
            antTrapNow = False
            antTrapPrice = 25
           
        if ownedWoodMills >= 1:
            woodMillNow = True
            woodMillPrice = 125 + (7*woodMillAmount)
        else:
            woodMillNow = False
            woodMillPrice = 125
           
        if smallShackAmount >= 1:
            smallShackNow = True
            smallShackPrice1 = 200 + (75*smallShackAmount)
            smallShackPrice2 = 100 + (40*smallShackAmount)
            totalCitizens += smallShackAmount
        else:
            smallShackNow = False
            smallShackPrice1 = 200
            smallShackPrice2 = 100
            totalCitizens = 0
       
        if upgradeOneBought == "False":
            oneBought = False
        else:
            oneBought = True
            totalCitizens += 3
       
        amountToSubtract = 14
        stop = False
       
        items = 0
       
        while stop == False:
       
            if dataList[amountToSubtract] != "ITEMSTOP":
                items += 1
                print(dataList[amountToSubtract])
                print(dataList[amountToSubtract+1])
                print(dataList[amountToSubtract+2])
                itemList.append(Items(dataList[amountToSubtract].replace("."," ").replace("+",""),dataList[amountToSubtract+1].replace("."," ").replace("-",""),int(dataList[amountToSubtract+2])))
                amountToSubtract += 3
            else:
                stop = True
       
        blah = int((len(dataList) - amountToSubtract)/2)
        print(items)
        print(blah)
        print(amountToSubtract)
        print(blah)
        for x in range(0,blah):
            param1 = dataList[15+ (3*items) + (2*x)]
            param2 = dataList[16+ (3*items) + (2*x)]
           
            if param2 == "True":
                idBlockList.append(param1)
        print(idBlockList)
       
        totalCitizensBonus = 0
       
           
       
else:
    maxWood = 2000
    maxFood = 2000
    boxAmount = 0
    boxPrice1 = 100
    boxPrice2 = 10
    antTrapAmount = 0
    totalFood = 50
    totalWood = 0
    ownedAntTraps = 0
    antTrapPrice = 25
    antTrapNow = False
    woodMillNow = False
    smallShackNow = False
    boxNow = False
    woodMillAmount = 0
    woodMillPrice = 125
    smallShackPrice1 = 200
    smallShackPrice2 = 100
    smallShackAmount = 0
    totalCitizens = 0
    totalCitizensBonus = 0
    oneBought = False
    totalScrap = 0
    boxBenefit = 100
    manPower = 0
    itemList = []
    stickWielders = 0
boon = False
onMills = 0
onAnts = 0
onScrap = 0
onMilitary = 0
antTrapProduction = 0.02
woodMillProduction = 0.05
smallShackInitial = False
antTrapInitial = False
woodMillInitial = False
storageBoxInitial = False
passiveFoodProduction = 0
ownedAntTraps = 0
foodDepreciation = 0.1
unusedCitizens = totalCitizens
woodChange = 0
foodChange = 0
upgradeList2 = []
itemsEquipped = []
this2 = ""


           
                   
                   
           
       

class Upgrades():
    
    '''

    This class creates an upgrade instance such that upgrades can be added easily and in one line


    '''
    
    upgradeFrame = Frame(mainScreen,background='skyblue')
    upgradeFrame.forget()
    upgradeFrame2 = Frame(mainScreen,background='skyblue')
    upgradeFrame2.forget()
    def __init__(self, upgradeName,upgradeCost,upgradeCostType,upgradeBenefit,toolTip,upgradeId,benefitType,upgradeModifier,finished,condition,amount,upgradeCost2=None,upgradeCostType2=None) -> None:
        
        '''

        This method is run when a new upgrade is created. upgradeName is the name of the upgrade, upgradeCost is the cost, upgradeCostType is the type of resources required
        
        upgradeBenefit is the type of reward the upgrade grants, tooltip is the tooltip created when the upgrade is hovered over, upgradeId is the id of the upgrade for saving purposes
        
        upgradeModifier is the amount of benefit the upgrade grants. Finished checks if the upgrade has been bought. Condition checks if the condition for the upgrade to appear has been met
        
        upgradeCost2 and upgradeCostType2 are optional and if present introduce another upgrade cost and type to the upgrade.
 


        '''
        
        global idBlockList, frameOneContent
        self.__condition = condition
        self.__amount = amount
        self.__upgradeId = upgradeId
        self.__upgradeModifier = upgradeModifier
        self.__benefitType = benefitType
        self.__upgradeName = upgradeName
        self.__frame = "idk"
       
        if frameOneContent < 11:
            frameOneContent += 1
            self.__frame = "one"
            self.__upgradeButton = Button(Upgrades.upgradeFrame,text=f'{upgradeName}',command=self.buttonClicked)
        else:
            self.__upgradeButton = Button(Upgrades.upgradeFrame2,text=f'{upgradeName}',command=self.buttonClicked)

        self.__upgradeTip = Hovertip(self.__upgradeButton,text=f'{toolTip}')
        self.__upgradeCost = upgradeCost
        self.__upgradeCost2 = upgradeCost2
        self.__upgradeCostType = upgradeCostType
        self.__upgradeCostType2 = upgradeCostType2
        self.__upgradeBenefit = upgradeBenefit
        self.__finished = finished
       
        if (str(self.__upgradeId) not in idBlockList) and self.__condition == False:
            self.__upgradeButton.pack()
        elif (str(self.__upgradeId) not in idBlockList) and self.__condition == True:
            pass
        else:
            print(self.__upgradeId)
            self.__finished = True
            self.__condition = False
            self.receiveBenefit()
   
   
   
    def buttonClicked(self) -> None:
        
        '''

        When the upgrade is clicked, this method will check if the upgradeCost of the upgradeCostType is met, and if it is the benefit will be granted


        '''
        
        global totalWood,totalFood,totalScrap, manPower, stickWielders
        print(totalWood)
        if (self.__upgradeCostType == "Wood") and (totalWood>=self.__upgradeCost):
            if (self.__upgradeCostType2 == "Food") and (totalFood >=self.__upgradeCost2):
                totalFood -= self.__upgradeCost2
                totalWood -= self.__upgradeCost
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
            elif (self.__upgradeCostType2 == "Scrap") and (totalScrap >= self.__upgradeCost2):
                totalWood -= self.__upgradeCost
                totalScrap -= self.__upgradeCost2
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
            elif (self.__upgradeCostType2 == None):
                totalWood -= self.__upgradeCost
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
        elif (self.__upgradeCostType == "Food") and (totalFood>=self.__upgradeCost):
            if (self.__upgradeCostType2 == "Wood") and (totalWood >= self.__upgradeCost2):
                totalWood -= self.__upgradeCost2
                totalFood -= self.__upgradeCost
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
            elif (self.__upgradeCostType2 == None):
                totalFood -= self.__upgradeCost
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
        elif (self.__upgradeCostType == "Scrap") and (totalScrap >= self.__upgradeCost):
            if (self.__upgradeCostType2 == "Food") and (totalFood >= self.__upgradeCost2):
                totalScrap -= self.__upgradeCost
                totalFood -= self.__upgradeCost2
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
            elif (self.__upgradeCostType2 == "Wood") and (totalWood >= self.__upgradeCost2):
                totalScrap -= self.__upgradeCost
                totalWood -= self.__upgradeCost2
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
            elif (self.__upgradeCostType2 == None):
                totalScrap -= self.__upgradeCost
                self.receiveBenefit()
                self.__upgradeButton.pack_forget()
        elif (self.__upgradeCostType == "Man Power") and (manPower >= self.__upgradeCost):
            manPower -= self.__upgradeCost
            self.receiveBenefit()
            self.__upgradeButton.pack_forget()
        elif (self.__upgradeCostType == "Stick Wielders") and (stickWielders >= self.__upgradeCost):
            stickWielders -= self.__upgradeCost
            stickWielder.configure(text=f'Stick Wielder ({stickWielders})')
            self.receiveBenefit()
            self.__upgradeButton.pack_forget()
           
    def receiveBenefit(self) -> None:
        
        '''

        This method is run when the upgrade button is clicked and the upgradeCost is met. This provides the user with the benefit the upgrade Provides
        
        Also removes the resources which are required for the upgrade in question.


        '''
        
        global boon, stickCost, woodMillProduction, frameOneContent, stickWielderTip, troopRolls, manPowerMultiplier, totalCitizensBonus, totalCitizens, antTrapProduction, scrapMultiplier,unusedCitizens,maxFood,maxWood,boxAmount,boxBenefit,idBlockList,antTendingBoost, millTendingBoost
        if self.__benefitType == "More Citizens":
            totalCitizens += self.__upgradeModifier
            unusedCitizens += self.__upgradeModifier
        elif self.__benefitType == "Box Storage":
            old = boxBenefit
            boxBenefit = boxBenefit * self.__upgradeModifier
            differential = boxBenefit - old
            maxFood += (boxAmount*differential)
            maxWood += (boxAmount*differential)  
            upgradeList.append(Upgrades(f"Larger Coffers {round((self.__upgradeId+10)/10,1)}",round(self.__upgradeCost +175,2),"Scrap",1,f"Costs: {round(self.__upgradeCost +175,2)} scrap\nProvides: 1.1 times multiplier to ALL Boxes",self.__upgradeId+10,"Box Storage",1.1,False,False,0))
        elif self.__benefitType == "Ant Tending":
            antTendingBoost = antTendingBoost + self.__upgradeModifier
           
            upgradeList.append(Upgrades(f"Better Ant Tending {round((self.__upgradeId+1000)/1000,1)}",round(self.__upgradeCost +5,2),"Scrap",1,f"Costs: {round(self.__upgradeCost+5,2)} scrap and {self.__upgradeCost2+10} food\nProvides: General Increase in Ant tending efficiency",self.__upgradeId + 1000,"Ant Tending",0.015,False,False,0,self.__upgradeCost2 +10,"Food"))
        elif self.__benefitType == "Mill Tending":
            millTendingBoost = millTendingBoost + self.__upgradeModifier
           
            upgradeList.append(Upgrades(f"Better Mill Managing {round((self.__upgradeId+100000)/100000,1)}",round(self.__upgradeCost+5,2),"Scrap",1,f"Costs: {round(self.__upgradeCost+5,2)} scrap and {self.__upgradeCost2+10} wood\nProvides: General Increase in Mill Managing efficiency",self.__upgradeId + 100000,"Mill Tending",0.015,False,False,0,self.__upgradeCost2 +10,"Wood"))

        elif self.__benefitType == "Scrap":
            scrapMultiplier *= self.__upgradeModifier
       
       
        elif self.__benefitType == "Ant Farm":
            antTrapProduction *= self.__upgradeModifier
       
        elif self.__benefitType == "Wood Mill":
            woodMillProduction *= self.__upgradeModifier
       
        elif self.__benefitType == "Bonus Citizens":
            boon = True
            b = totalCitizens // 5 * self.__upgradeModifier
            totalCitizensBonus = b
           
            unusedCitizens = totalCitizensBonus + totalCitizens
        elif self.__benefitType == "Manpower":
            manPowerMultiplier *= self.__upgradeModifier
        elif self.__benefitType == "Stick Roll":
            troopRolls["Stick"] += 1
            stickWielderTip = Hovertip(stickWielder, f'Weakest unit in an army - But a necessary one\nCosts: {stickCost} Manpower\nPower: Rolls a D{troopRolls["Stick"]}')
        elif self.__benefitType == "Stick Price":
            stickCost -= self.__upgradeModifier
            stickWielderTip = Hovertip(stickWielder, f'Weakest unit in an army - But a necessary one\nCosts: {stickCost} Manpower\nPower: Rolls a D{troopRolls["Stick"]}')

           
           
        self.__finished = True
       
        if self.__frame == "one":
            frameOneContent -= 1
   
    def checkCondition(self) -> None:
        
        '''

        This is run when the upgrades tab is open, and checks if an upgrade has a condition. If it does and the condition is met, the upgrade appears.
        
        If not, then it stays hidden.
        

        '''
        
        global upgradeList, totalScrap
       
        print(self.__condition)
        print(self.__amount)
       
        if self.__condition == True:
            if self.__amount == 500:
                if totalScrap >= 500:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 1000:
                if totalScrap >= 1000:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 50:
                if totalScrap >= 50:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 35:
                if antTrapAmount >= 35:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 10:
                if smallShackAmount >= 10:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 25:
                if woodMillAmount >= 25:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 8:
                if antTrapAmount >= 8:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 200:
                if manPower >= 200:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 499:
                if manPower >= 499:
                    self.__condition = False
                    self.__upgradeButton.pack()
            elif self.__amount == 1:
                if stickWielders >= 1:
                    self.__condition = False
                    self.__upgradeButton.pack()
           
   
   
    def __str__(self) -> str:
        
        '''

        This is used to save the upgrades which are bought and is called when the save button is pressed

        '''
        
        global this
        this = f'{str(self.__finished)} {self.__upgradeId}'
        return f'{str(self.__finished)} {self.__upgradeId}'
       

def hideBuildings() -> None:
    
    '''
    Simply hides all the building labels/buttons in the buildings tab

    '''
    
    global antTrap,woodMill
    antTrap.place(x=10000)
    woodMill.place(y=10000)
    smallShack.place(x=10000)
    storageBox.place(x=10000)

def showBuildings() -> None:
    
    '''
    Simply shows all the building labels/buttons in the buildings tab

    '''
    
    global antTrap,woodMill,smallShack,storageBox
   
    hideCitizens()
    hideUpgrades()
    hideItems()
    hideTactics()
   
    if antTrapInitial == True:
        antTrap.place(x=10,y=160)
    if woodMillInitial == True:
        woodMill.place(x=110,y=160)
    if smallShackInitial == True:
        smallShack.place(x=230,y=160)
    if storageBoxInitial == True:  
        storageBox.place(x=360,y=160)
   
def showCitizens() -> None:
    '''
    Simply shows all the citizen labels/buttons in the citizens tab

    '''
    global boon, unusedCitizens, onMills, onAnts, onScrap, totalCitizensBonus, onMilitary
   
    if boon == True:
        b = totalCitizens // 5 * 2
        totalCitizensBonus = b
       
        unusedCitizens = totalCitizensBonus + totalCitizens - onMills - onAnts - onScrap - onMilitary
       
       
        print(onMilitary)
        print(b)
        print(totalCitizensBonus)
        print(unusedCitizens)
       
       
    hideBuildings()
    hideUpgrades()
    hideItems()
    hideTactics()
    unusedLabel.place(x=10,y=140)
    assignOne.place(x=140,y=140)
    assignTen.place(x=180,y=140)
    assignHundred.place(x=220,y=140)
    manageMills.place(x=10,y=180)
    tendAntTraps.place(x=10,y=210)
    collectScrap.place(x=10,y=240)
    harvestMen.place(x=10,y=270)
    plusOne.place(x=145,y=180)
    minusOne.place(x=160,y=180)
    plusTwo.place(x=140,y=210)
    minusTwo.place(x=155,y=210)
    plusThree.place(x=150,y=240)
    minusThree.place(x=165,y=240)
    plusFour.place(x=150,y=270)
    minusFour.place(x=165,y=270)
   


def hideCitizens() -> None:
    '''
    Simply hides all the citizen labels/buttons in the citizens tab

    '''
    unusedLabel.place(x=10000)
    plusOne.place(x=15000)
    minusOne.place(x=15000)
    manageMills.place(x=15001)
    tendAntTraps.place(x=15001)
    collectScrap.place(x=15000)
    harvestMen.place(x=15000)
    plusTwo.place(x=15000)
    minusTwo.place(x=15000)
    plusThree.place(x=15000)
    minusThree.place(x=15000)
    plusFour.place(x=15000)
    minusFour.place(x=15000)
    assignOne.place(x=15000)
    assignTen.place(x=15000)
    assignHundred.place(x=15000)

def showUpgrades() -> None:
    '''
    Simply shows all the upgrade labels/buttons in the upgrades tab

    '''
    hideBuildings()
    hideCitizens()
    hideItems()
    hideTactics()
   
   
   
    for x in upgradeList2:
        Upgrades.checkCondition(x)
   
    Upgrades.upgradeFrame.place(x=10,y=155)
    Upgrades.upgradeFrame2.place(x=225,y=155)

def showTactics() -> None:
    '''
    Simply shows all the tactic labels/buttons in the tactics tab

    '''
    hideBuildings()
    hideUpgrades()
    hideCitizens()
    hideItems()
    troopsLabel.place(x=10,y=150)
    stickWielder.place(x=10,y=180)
    battlesLabel.place(x=10,y=210)
    forestHill.place(x=10,y=240)
    battleResults.place(x=10,y=280)
   
def hideTactics() -> None:
    '''
    Simply hides all the tactic labels/buttons in the tactics tab

    '''
    troopsLabel.place(x=15000)
    stickWielder.place(x=15000)
    battlesLabel.place(x=15000)
    forestHill.place(x=15000)
    battleResults.place(x=15000)

def showItems() -> None:
    '''
    Simply shows all the item labels/buttons in the items tab

    '''
    hideBuildings()
    hideCitizens()
    hideUpgrades()
    hideTactics()
    Items.itemFrame.place(x=10,y=155)
   
def hideItems() -> None:
    '''
    Simply hides all the item labels/buttons in the items tab

    '''
    Items.itemFrame.place(x=15000)

def hideUpgrades() -> None:
    '''
    Simply hides all the upgrade labels/buttons in the upgrades tab

    '''
    Upgrades.upgradeFrame.place(x=15000)
    Upgrades.upgradeFrame2.place(x=15000)

def updateLabels() -> None:
    '''
    This is run every second, and updates all the labels such that the user can see accurate change in data
    '''
    global woodChange,foodChange,maxWood,maxFood,scrapChange, unusedCitizens
    woodLabel.configure(text=f'Total Wood: {totalWood:.2f}/{maxWood:.0f} ({woodChange}/s)')
    foodLabel.configure(text=f'Total Food: {totalFood:.2f}/{maxFood:.0f} ({foodChange}/s)')
    antTrap.configure(text=f'Ant Trap ({antTrapAmount})')
    woodMill.configure(text=f'Wood Mill ({woodMillAmount})')
    citizensLabel.configure(text=f'Total Citizens: {totalCitizens + totalCitizensBonus}')
    smallShack.configure(text=f'Small Shack ({smallShackAmount})')
    manageMills.configure(text=f'Manage Wood Mills: ({onMills})')
    tendAntTraps.configure(text=f'Tend Ant Traps: ({onAnts})')
    harvestMen.configure(text=f'Raise the military: ({onMilitary})')
    unusedLabel.configure(text=f'Unused Citizens: ({unusedCitizens})')
    collectScrap.configure(text=f'Collect Scrap: ({onScrap})')
    scrapLabel.configure(text=f'Total Scrap: {totalScrap:.2f} ({scrapChange*5:.2f}/s)')
    storageBox.configure(text=f'Storage Box ({boxAmount})')
    manPowerLabel.configure(text=f'Total Manpower: {manPower:.2f}')
   

def collectWood() -> None:
    '''
    This is run when the collect twigs button is pressed, and increments wood by 1

    '''
    global totalWood
   
    totalWood += 1
   
    updateLabels()
   
def collectBerries() -> None:
    '''
    This is run when the collect berries button is pressed, and increments food by 1

    '''
    global totalFood
   
    totalFood += 1
   
    updateLabels()

def checking() -> None:
    '''
    This checks if a building is unlocked, and if it is the button for said building appears

    '''
    global boon, unusedCitizens, onMilitary, totalCitizensBonus, scrapMultiplier, millTendingBoost, antTendingBoost,totalScrap, onScrap, maxFood, maxWood, boxNow, woodChange, scrapChange, foodChange, totalCitizens, totalFood, onMills,smallShackNow, onAnts, foodDepreciation, smallShackInitial, antTrapProduction, woodMillProduction, woodMillNow, totalWood,antTrapInitial, antTrapAmount, antTrapNow, woodMillInitial, woodMillAmount,storageBoxInitial

    if ((totalWood >= 50) and antTrapInitial == False) or antTrapNow == True:
        antTrap.place(x=10,y=160)
        antTrapInitial = True
        antTrapNow = False
    if ((antTrapAmount >= 7) and woodMillInitial == False) or woodMillNow == True:
        woodMill.place(x=110,y=160)
        woodMillInitial = True
        woodMillNow = False
    if ((woodMillAmount >= 5) and smallShackInitial == False) or smallShackNow == True:
        smallShack.place(x=230,y=160)
        smallShackInitial = True
        smallShackNow = False
    if ((totalFood >= 500) and storageBoxInitial == False) or boxNow == True:
        storageBox.place(x=360,y=160)
        storageBoxInitial = True
        boxNow = False
    if boon == True:
        b = totalCitizens // 5 * 2
        totalCitizensBonus = b
       
        unusedCitizens = totalCitizensBonus + totalCitizens - onMills - onAnts - onScrap - onMilitary
    updateLabels()
    mainScreen.update()
    t4 = Timer(0.1,checking)
    t4.start()

def feedThePeople() -> None:
    '''
    This is run once every 0.2 seconds, and changes all variables based on the per second basis of every resource

    '''
    global scrapMultiplier, manPowerMultiplier, baseFood, baseWood, baseScrap, onMilitary, manPower, millTendingBoost, totalCitizensBonus, antTendingBoost,totalScrap, onScrap, maxFood, maxWood, boxNow, woodChange, scrapChange, foodChange, zens, totalFood, onMills,smallShackNow, onAnts, foodDepreciation, smallShackInitial, antTrapProduction, woodMillProduction, woodMillNow, totalWood,antTrapInitial, antTrapAmount, antTrapNow, woodMillInitial, woodMillAmount,storageBoxInitial
   
    foodDepreciation = baseFood/5 + (antTrapAmount * antTrapProduction) - 0.1 - ((totalCitizens + totalCitizensBonus) * 0.1) + (onAnts * 0.15) * antTendingBoost
    woodIncrease = baseWood/5 + (woodMillAmount *woodMillProduction) + onMills/5 * millTendingBoost
   
   
   
    totalFood += foodDepreciation
    totalFood = round(totalFood,3)
    totalWood += round(woodIncrease,2)
   
    woodChange = round(woodIncrease *5,2)
    foodChange = round(foodDepreciation *5,2)
   
    scrapChange = onScrap * 0.02
   
    totalScrap += scrapChange
   
    manPower += onMilitary * 0.04
   
    if totalFood >= maxFood:
        totalFood = maxFood
    if totalWood >= maxWood:
        totalWood = maxWood
   
   
    if ((totalWood >= 50) and antTrapInitial == False) or antTrapNow == True:
        antTrap.place(x=0,y=160)
        antTrapInitial = True
        antTrapNow = False
    if ((antTrapAmount >= 7) and woodMillInitial == False) or woodMillNow == True:
        woodMill.place(x=90,y=160)
        woodMillInitial = True
        woodMillNow = False
    if ((woodMillAmount >= 5) and smallShackInitial == False) or smallShackNow == True:
        smallShack.place(x=190,y=160)
        smallShackInitial = True
        smallShackNow = False
    if ((totalFood >= 500) and storageBoxInitial == False) or boxNow == True:
        storageBox.place(x=300,y=160)
        storageBoxInitial = True
        boxNow = False

    t2 = Timer(0.2,feedThePeople)
    t2.start()

def buyAntTrap() -> None:
    '''
    This checks if the price for ant traps is met. If it is, totalWood is decresaed by the price, and an ant trap is added, as well as its benefits

    '''
    global ownedAntTraps, totalWood, antTrapPrice, passiveFoodProduction,antTrapAmount
   
    if totalWood >= antTrapPrice:
        totalWood -= antTrapPrice
        passiveFoodProduction += 0.02
        antTrapPrice = antTrapPrice +2
        antTrapAmount += 1
       
        updateLabels()
        antTrapTip = Hovertip(antTrap,f"Guess you have to start somewhere \nCosts: {antTrapPrice:.2f} wood \nProvides: {antTrapProduction*5} Food Per second")
def buyWoodMill() -> None:
    '''
    Checks if the price for wood mills is met. If it is, totalWood is decreased by the price, and a wood mill is added, as well as its benefits

    '''
    global woodMillAmount, totalWood, woodMillPrice
   
    if totalWood >= woodMillPrice:
        totalWood -= woodMillPrice
        woodMillPrice = woodMillPrice + 7
        woodMillAmount += 1
   
    updateLabels()
    woodMillTip = Hovertip(woodMill,f'Automatically Harvests Wood\nCosts: {woodMillPrice:.2f} wood \nProvides: 0.25 Wood Per Second')
def buySmallShack() -> None:
    '''
    Checks if the price for small shacks is met. If it is, totalWood and totalFood is decreased by the prices, and a small shack is added, as well as a citizen

    '''
    global smallShackAmount, totalWood, totalCitizens, smallShackPrice1, smallShackPrice2, totalFood, unusedCitizens
   
    if (totalWood >= smallShackPrice1) and (totalFood >= smallShackPrice2):
        totalWood -= smallShackPrice1
        totalFood -= smallShackPrice2
       
        smallShackPrice1 = smallShackPrice1 + 75
        smallShackPrice2 = smallShackPrice2 + 40
       
        totalCitizens += 1
        unusedCitizens += 1
        smallShackAmount += 1
    smallShackTip = Hovertip(smallShack,f'A shitty house for your citizens\nCosts: {smallShackPrice1:.2f} wood and {smallShackPrice2:.2f} berries\nProvides: 1 citizen\n (NOTE: Citizens consume 0.5 food per second)')

def buyStorageBox() -> None:
    '''
    Checks if the price for a storage box is met. If it is, totalFood and totalScrap is decreased by the prices, and a storage box is added, and max resources increased

    '''
    global totalFood,boxPrice1,boxPrice2,totalScrap,maxFood,maxWood,boxAmount,boxBenefit
   
    if (totalFood >= boxPrice1) and (totalScrap >= boxPrice2):
        boxAmount += 1
        totalFood -= boxPrice1
        totalScrap -= boxPrice2
       
        boxPrice1 = boxPrice1 + 5
        boxPrice2 = boxPrice2 + 0.5
        print(boxBenefit)
        maxFood += boxBenefit
        maxWood += boxBenefit
    storageBoxTip = Hovertip(storageBox,f'Small box to store various items\nCosts: {boxPrice1:.2f} berries and {boxPrice2:.2f} scraps\nProvides: 100 Wood and Berry Space')

       
   
    
def finished() -> None:
    '''
    This is run when the save button is pressed, and data is appended to the file

    '''
    global totalFood, manPower, itemList, totalWood, antTrapAmount, woodMillAmount,smallShackAmount,oneBought, upgradeList,this,boxAmount, this2
   
    with open('saveFile.txt','w') as f:
   
       f.write(f'{totalFood} {totalWood} {antTrapAmount} {woodMillAmount} {smallShackAmount} {oneBought} 0 {boxAmount} 0 {totalScrap} 0 {manPower} 0 {stickWielders}')
    with open('saveFile.txt','a') as f:
        for x in itemList:
            print(x)
           
            print(this2)
            print(f' {this2.split("|")[0]} {this2.split("|")[1]} {this2.split("|")[2]}')
           
            f.write(f' {this2.split("|")[0]} {this2.split("|")[1]} {this2.split("|")[2]}')
        f.write(" ITEMSTOP")
           
        for x in upgradeList:
            print(x)
            f.write(f' {this.split()[1]} {this.split()[0]}')
        for x in upgradeList2:
            print(x)
            f.write(f' {this.split()[1]} {this.split()[0]}')
               
       
def deleteSave() -> None:
    '''
    This is run when the delete save button is pressed, and clears the save file such that a new game is started.

    '''
    with open('saveFile.txt','w') as f:
        f.write(f'50 0 0 0 0 False 0 0 0 0 0 0 0 0 ITEMSTOP')
       
def add(job) -> None:
    '''
    This is run when one of the plus buttons is pressed, and adds the corresponding amount of citizens to the job
    
    Also checks if there are enough available citizens

    '''
    global onMills,unusedCitizens,onAnts,onScrap,onMilitary
   
    print(assignNum.get())
    if (job == "mill") and unusedCitizens >= assignNum.get():
        onMills += assignNum.get()
        unusedCitizens -= assignNum.get()
    elif (job == "ants") and unusedCitizens >= assignNum.get():
        onAnts += assignNum.get()
        unusedCitizens -= assignNum.get()
    elif (job == "scrap") and unusedCitizens >= assignNum.get():
        onScrap += assignNum.get()
        unusedCitizens -= assignNum.get()
    elif (job == "men") and unusedCitizens >= assignNum.get():
        onMilitary += assignNum.get()
        unusedCitizens -= assignNum.get()
   

def minus(job) -> None:
    '''
    This is run when one of the minus buttons is pressed, and removes the corresponding amount of citizens to the job
    
    Also checks if there are enough people on the job to remove

    '''
    global onMills,unusedCitizens, onAnts,onScrap, onMilitary,assignNum
   
   
    if (job == "mill") and onMills >= assignNum.get():
        onMills -= assignNum.get()
        unusedCitizens += assignNum.get()
    elif (job == "ants") and onAnts >= assignNum.get():
        onAnts -= assignNum.get()
        unusedCitizens += assignNum.get()
    elif (job == "scrap") and onScrap >= assignNum.get():
        onScrap -= assignNum.get()
        unusedCitizens += assignNum.get()
    elif (job == "men") and onMilitary >= assignNum.get():
        onMilitary -= assignNum.get()
        unusedCitizens += assignNum.get()

def buyStick() -> None:
    '''
    Run when the stickWielder button is pressed, and checks if manPower is greater than stickCost. If it is, remove manPower equal to the cost,
    
    and add a stickWielder

    '''
    global manPower, stickWielders, stickCost
   
    if manPower >= stickCost:
        manPower -= stickCost
        stickWielders += 1
        stickWielder.configure(text=f'Stick Wielder ({stickWielders})')

def battle(troopList) -> bool:
    '''
    Conducts a battle based on the amount of troops you have and the enemy. If the battle succeeds, loot is provided.

    '''
    global yourTroops,enemyTroops,troopRolls, stickWielders,stickWielder
   
    enemyTroops = []
    yourTroops = []
    defeat = False
    victory = False
   
   
    for x in range(0,stickWielders):
        yourTroops.append("Stick")
    for x in troopList:
        enemyTroops.append(x)
       
    if len(yourTroops) != 0:
       
        while (defeat != True) and (victory != True):
            enemyRoll = troopRollsEnemy[enemyTroops[0]]
            yourRoll = troopRolls[yourTroops[0]]
           
            print(f'{enemyRoll} {enemyTroops[0]}')
            print(f'{yourRoll} {yourTroops[0]}')
           
            rolled = randint(0,yourRoll)
            enemyRolled = randint(0,enemyRoll)
           
            print(rolled)
            print(enemyRolled)
           
            if rolled > enemyRolled:
                print(f'Killed {enemyTroops[0]}')
                enemyTroops.remove(enemyTroops[0])
            elif rolled == enemyRolled:
                pass
            else:
                print(f'Troop {yourTroops[0]} was killed')
                if yourTroops[0] == "Stick":
                    stickWielders -= 1
                yourTroops.remove(yourTroops[0])
           
            print(enemyTroops)
           
            if len(enemyTroops) == 0:
                victory = True
            elif len(yourTroops) == 0:
                defeat = True
       
        if victory == True:
            return True
        elif defeat == True:
            return False
       
   
   
       
       

def battleForestHill() -> None:
    '''
    Run when the battle of forest hill button is pressed, and calculates the battle results using the battle method.
    
    If battle returns true, loot is provided, and if False no loot is provided.

    '''
    global manPower, stickWielders,totalScrap,totalWood,totalFood
   
    if battle(["Rock","Rock","Rock","Rock","Rock","Stick"]) == True:
        reward = randint(0,100)
        rewardName = ""
        rewardNumber = 0
        if reward < 25:
            rewardNumber = randint(50,100)
            totalScrap += rewardNumber
            rewardName = "Scrap"
        elif reward < 50:
            rewardNumber = randint(1000,2000)
            totalFood += rewardNumber
            rewardName = "Food"
        elif reward < 90:
            rewardNumber = randint(3000,4000)
            totalWood += rewardNumber
            rewardName = "Wood"
        else:
            rewardNumber = 1
            rewardName = f'{names1[randint(0,len(names1)-1)]} {names2[randint(0,len(names2)-1)]} of {names3[randint(0,len(names3)-1)]}'
           
            typeItem = randint(0,100)
           
            if typeItem < 33:
                itemList.append(Items(f'{rewardName}',"Base Wood",randint(5,12)))
            elif typeItem < 88:
                itemList.append(Items(f'{rewardName}',"Base Food",randint(5,10)))
            else:
                itemList.append(Items(f'{rewardName}',"Base Scrap",randint(1,2)))
       
        battleResults.configure(text=f'Victory! Reward: {rewardNumber} {rewardName}')
    else:
        battleResults.configure(text=f'You lost! Get stronger!')
   
    stickWielder.configure(text=f'Stick Wielder ({stickWielders})')
   
#RESOURCES

woodLabel = Label(mainScreen,text=f'Total Wood: {totalWood}',bg='maroon',fg='white')
woodLabel.place(x=10,y=6)

foodLabel = Label(mainScreen,text=f'Total Food: {totalFood}',bg='blue',fg='white')
foodLabel.place(x=10,y=30)

scrapLabel = Label(mainScreen,text=f'Total Scrap: {totalScrap}',bg='gray',fg='white')
scrapLabel.place(x=10,y=550)

manPowerLabel = Label(mainScreen,text=f'Total Manpower: {manPower}',bg='green',fg='white')
manPowerLabel.place(x=10,y=576)



citizensLabel = Label(mainScreen,text=f'Total Citizens: {totalCitizens + totalCitizensBonus}',bg='honeydew',fg='black')
citizensLabel.place(x=10,y=60)

collectTwigsButton = Button(mainScreen,text=f'Collect Twigs', command=collectWood)
collectTwigsButton.place(x=260,y=6)

collectBerriesButton = Button(mainScreen,text=f'Collect Berries', command=collectBerries)
collectBerriesButton.place(x=260,y=35)

blockLabel = Label(mainScreen,text="-------------------------------------------")
blockLabel.place(x=10,y=85)

#BUILDINGS

buildingsLabel = Button(mainScreen,text="Buildings:",command=showBuildings)
buildingsLabel.place(x=10,y=110)

citizensLabel2 = Button(mainScreen,text="Citizens:",command=showCitizens)
citizensLabel2.place(x=100,y=110)



woodMill = Button(mainScreen,text=f'Wood Mills (0)', command=buyWoodMill,bg='maroon',fg='white')
woodMill.forget()
woodMillTip = Hovertip(woodMill,f'Automatically Harvests Wood\nCosts: {woodMillPrice:.2f} wood \nProvides: 0.25 Wood Per Second')

smallShack = Button(mainScreen,text=f'Small Shack (0)',command=buySmallShack,bg='honeydew',fg='black')
smallShack.forget()
smallShackTip = Hovertip(smallShack,f'A shitty house for your citizens\nCosts: {smallShackPrice1:.2f} wood and {smallShackPrice2:.2f} berries\nProvides: 1 citizen\n (NOTE: Citizens consume 0.5 food per second)')

storageBox = Button(mainScreen,text=f'Storage Box (0)',command=buyStorageBox,bg='red',fg='white')
storageBox.forget()
storageBoxTip = Hovertip(storageBox,f'Small box to store various items\nCosts: {boxPrice1:.2f} berries and {boxPrice2:.2f} scraps\nProvides: 100 Wood and Berry Space')

#CITIZENS

assignNum = IntVar()

assignOne = Radiobutton(mainScreen,text="1",variable=assignNum,value=1)
assignOne.forget()

assignOne.invoke()

assignTen = Radiobutton(mainScreen,text="10",variable=assignNum,value=10)
assignTen.forget()

assignHundred = Radiobutton(mainScreen,text="100",variable=assignNum,value=100)
assignHundred.forget()

unusedLabel = Label(mainScreen,text=f'Unused Citizens: ({unusedCitizens})',bg='honeydew',fg='black')
unusedLabel.forget()

manageMills = Label(mainScreen,text=f'Manage Wood Mills: ({onMills})',bg='maroon',fg='white',height=1)
manageMills.forget()
mangeMillsTip = Hovertip(manageMills,f'NOTE: Suffers from Diminishing Marginal Returns\n((((TrapAmount)^1.4) * AntWorkers)^0.5)/10')

tendAntTraps = Label(mainScreen,text=f'Tend Ant Traps: ({onAnts})',bg='blue',fg='white')
tendAntTraps.forget()
tendAntTrapsTip = Hovertip(tendAntTraps,f'NOTE: Suffers from Diminishing Marginal Returns\n((((MillAmount)^1.7) * MillWorkers)^0.5)/7')

collectScrap = Label(mainScreen,text=f'Collect Scrap: ({onScrap})',bg='gray',fg='white')
collectScrap.forget()
collectScrapTip = Hovertip(collectScrap,f'Search around abandoned shacks for useful scrap')

harvestMen = Label(mainScreen,text=f'Raise the Military: ({onMilitary})',bg='green',fg='white')
harvestMen.forget()
harvestMenTip = Hovertip(harvestMen, f'Look around for men to fight for your cause')

plusOne = Button(mainScreen,text=f'+',bg='green',fg='white',height=1,command=lambda: add("mill"))
plusOne.forget()

minusOne = Button(mainScreen,text=f'-',bg='red',fg='white',height=1,command=lambda: minus("mill"))
minusOne.forget()
                           
plusTwo = Button(mainScreen,text=f'+',bg='green',fg='white',height=1,command=lambda: add("ants"))
plusTwo.forget()

minusTwo = Button(mainScreen,text=f'-',bg='red',fg='white',height=1,command=lambda: minus("ants"))
minusTwo.forget()

plusThree = Button(mainScreen,text=f'+',bg='green',fg='white',height=1,command=lambda: add("scrap"))
plusThree.forget()

minusThree = Button(mainScreen,text=f'-',bg='red',fg='white',height=1,command=lambda: minus("scrap"))
minusThree.forget()

plusFour = Button(mainScreen,text=f'+',bg='green',fg='white',height=1,command=lambda: add("men"))
plusFour.forget()

minusFour = Button(mainScreen,text=f'-',bg='red',fg='white',height=1,command=lambda: minus("men"))
minusFour.forget()


#UPGRADES

upgradesButton = Button(mainScreen, text="Upgrades",command=showUpgrades)
upgradesButton.place(x=180,y=110)


#SAVING

antTrap = Button(mainScreen,text=f'Ant Trap (0)',command=buyAntTrap,bg='blue',fg='white')
antTrap.forget()
antTrapTip = Hovertip(antTrap,f"Guess you have to start somewhere \nCosts: {antTrapPrice:.2f} wood \nProvides: {antTrapProduction*5} Food Per second")

saveButton = Button(mainScreen, text=f'SAVE', command=finished)
saveButton.place(x=10,y=500)

deleteSaveButton = Button(mainScreen, text=f'Delete Save', command=deleteSave)
deleteSaveButton.place(x=60,y=500)

#TACTICS

tacticsButton = Button(mainScreen,text="Tactics",command=showTactics)
tacticsButton.place(x=270,y=110)

troopsLabel = Label(mainScreen,text="Troops")
troopsLabel.forget()

stickWielder = Button(mainScreen,text=f"Stick Wielder ({stickWielders})",command=buyStick)
stickWielder.forget()
stickWielderTip = Hovertip(stickWielder,f'Weakest unit in an army - But a necessary one\nCosts: 65 Manpower\nPower: Rolls a D4')

battlesLabel = Label(mainScreen,text="Battles")
battlesLabel.forget()

forestHill = Button(mainScreen,text="Forest Hill",command=battleForestHill)
forestHill.forget()
forestHillTip = Hovertip(forestHill,f'The First chokepoint that our army must take!\n\nEnemies:\n\nRock Throwers: 5 (Rolls D5)\nStick Wielders: 1 (Rolls D4)')

battleResults = Label(mainScreen,text="",bg='black',fg='red')
battleResults.forget()

#ITEMS

itemsButton = Button(mainScreen,text="Items",command=showItems)
itemsButton.place(x=360,y=110)

upgradeList2.append(Upgrades("Better Rolls",500,"Man Power",1,"Costs: 500 Manpower\nEffect: Stick Wielders Roll a D5 instead of a D4",11,"Stick Roll",1,False,True,499,3000))

upgradeList.append(Upgrades("Citizen Pack",1000,"Wood",1,"Costs: 1000 wood and 1000 food\nProvides: 3 citizens\nThis one is a freebie ~ use it wisely :)",0,"More Citizens",3,False, False,0,1000, "Food"))
upgradeList.append(Upgrades("Citizen Pack 2",2000,"Wood",1,"Costs: 2000 wood and 2000 food\nProvides: 5 citizens\nThis one is a freebie ~ use it wisely :)",1,"More Citizens",5,False, False,0,2000, "Food"))
upgradeList.append(Upgrades("Larger Coffers",250,"Scrap",1,"Costs: 250 scrap\nProvides: 1.1 times multiplier to ALL Boxes",10,"Box Storage",1.1,False,False,0))
upgradeList.append(Upgrades("Better Ant Tending",10,"Scrap",1,"Costs: 10 scrap and 100 food\nProvides: General Increase in Ant tending efficiency",1000,"Ant Tending",0.015,False,False,0,100,"Food"))
upgradeList.append(Upgrades("Better Mill Managing",10,"Scrap",1,"Costs: 10 scrap and 100 wood\nProvides: General Increase in Mill Managing efficiency",100000,"Mill Tending",0.015,False,False,0,100,"Wood"))
upgradeList2.append(Upgrades("Intelligent Scrap Collecting",600,"Scrap",1,"Costs: 600 scrap\nProvides: DOUBLE scrap collection",2,"Scrap",2,False,True,500))
upgradeList2.append(Upgrades("Desperate Scrap Collecting",1200,"Scrap",1,"Costs: 1200 scrap\nProvides: DOUBLE scrap collection",3,"Scrap",2,False,True,1000))
upgradeList2.append(Upgrades("More Expansive Scrap Collecting",150,"Scrap",1,"Costs: 150 scrap\nProvides: DOUBLE scrap collection",4,"Scrap",2,False,True,50))
upgradeList2.append(Upgrades("Larger Ant Traps",2000,"Food",1,"Costs: 2000 Food and 2000 Wood\nProvides: DOUBLING of all ant farm production (IS NOT AFFECTED BY NOR DOES IT AFFECT WORKERS)",5,"Ant Farm",2,False,True,35,2000,"Wood"))
upgradeList2.append(Upgrades("House Fitting Plan",4000,"Food",1,"Costs: 4000 Food and 4000 Wood\nProvides: 2 citizens for every 5 obtained through other means",6,"Bonus Citizens",2,False,True,10,4000,"Wood"))
upgradeList2.append(Upgrades("Larger Wood Mills",3000,"Wood",1,"Costs: 3000 wood and 100 Scrap\nProvides: DOUBLING of all wood mill production (IS NOT AFFECTED BY NOR DOES IT AFFECT WORKERS)",7,"Wood Mill",2,False,True,25,100,"Scrap"))
upgradeList2.append(Upgrades("Mobile Scrap Collecting",2000,"Food",1,"Costs: 2000 Food\nProvides: Multiplies all Scrap Production by 1.5",8,"Scrap",1.5,False,True,8))
upgradeList2.append(Upgrades("Higher Enlistment",1000,"Food",1,"Costs: 1000 Food and 1000 Wood\nProvides: Increase to manpower collection",9,"Manpower",1.5,False,True,200,1000,"Wood"))
upgradeList2.append(Upgrades("Sacrifice For the Greater Good",20,"Stick Wielders",1,"Costs: 20 Stick Wielders\nProvides: Decrease of Stick Wielder cost by 5 manpower",12,"Stick Price",5,False,True,1,))


t = Timer(0.2, feedThePeople)
t.start()

t3 = Timer(0.1,checking)
t3.start()

mainScreen.mainloop()

atexit.register(finished)
