class EnvironmentComponent:
    DEFAULT = 0
    # Environment Types
    DIRT = 0
    GRASS = 1
    SAND = 2
    WATER = 50
    # Orientations
    FRONT = 0
    LEFT = 1
    TOP = 2
    RIGHT = 3
    # initiate environment component of environmentType. Other data changes respectively, unless stated otherwise
    def __init__(self, x, y, environmentType, isSolid = DEFAULT, effect = DEFAULT, orientation = DEFAULT):
        self.x = x
        self.y = y
        self.environmentType = environmentType
        self.solid = isSolid
        self.effect = effect
        self.orientation = orientation
    def setX(self, x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self, y):
        self.y = y
    def getY(self):
        return self.y
    def getType(self):
        return self.environmentType
    def setType(self, environmentType):
        self.__init__(self.x, self.y, environmentType)
    def isSolid(self):
        return self.solid
    def setSolid(self, solid):
        self.solid = solid
    def getEffect(self):
        return self.effect
    def setEffect(self, effect):
        self.effect = effect
    def getOrientation(self):
        return orientation
    def setOrientation(self, orientation):
        self.orientation = orientation


class Environment:
    # initiate environment x * y all empty.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []
        for a in range(x):
            s = []
            for b in range(y):
                s.append('')
            self.grid.append(s)

    def setX(self,x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y
    def setComponent(self, x, y, component):
        self.grid[x][y] = component
    def getComponent(self, x, y):
        return self.grid[x][y]
    def getComponents(self):
        return self.grid
    # change the whole environment to this new one's grid
    def setComponents(environment):
        self.grid = environment.getComponents()
        self.x = environment.getX()
        self.y = environment.getY()


class Item:
    # Basic item types
    ITEM = 0
    HELM = 1
    CHEST = 2
    LEGS = 3
    HANDS = 4
    SHOES = 5
    WEAPON = 6
    PROJECTILE = 7
    POTION = 8
    # initiate item with itemNumber num. All other data is changed respective to item number
    def __init__(self,itemNumber,itemType,name,description,effect,requirements):
        self.itemNumber = itemNumber
        self.itemType = itemType
        self.name = name
        self.description = description
        self.effect = effect
        self.requirements = requirements
    def getItemNumber(self):
        return self.itemNumber
    def setItemNumber(self,itemNumber):
        self.itemNumber = itemNumber	
    def getItemType(self):
        return self.itemType
    def setItemType(self,itemType):
        self.itemType = itemType	
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name	
    def getDescription(self):
        return self.description
    def setDescription(self,description):
        self.description = description	
    def getEffect(self):
        return self.effect
    def setEffect(self,effect):
        self.effect = effect	
    def getRequirements(self):
        return self.requirements
    def setRequirements(self,requirements):
        self.requirements = requirements



class Inventory:
    # Initialize an inventory of size 'size'. 
    def __init__(self,size):
        self.size = size
        self.numItems = 0
        self.inventory = ['']*size
    # Sets the slot num in inventory with item.
    def setSlot(self, num, item):
        self.inventory[num] = item
    # Gets the item in the slot 'num'
    def getSlot(self, num):
        return self.inventory[num]
    # Sets the number of items to num. SHOULD NOT BE USED OUTSIDE OF CLASS
    def setNumItems(self, num):
        self.numItems = num
    # Gets the number of items in the inventory
    def getNumItems(self):
        return self.numItems
    # Adds item to list if list is not full. Returns true if full.
    def addItem(self, item):
        if self.numItems == self.size: return True
        for i in range(len(self.inventory)):
            if not self.inventory[i]:
                self.inventory[i] = item
                self.numItems +=1
                return
    # Removes the item in slot 'num' from the inventory
    def removeItem(self, num):
        if self.inventory[num]:
            self.inventory[num] = ''
            self.numItems -=1
    # Removes and returns the item in slot 'num' in inventory
    def takeItem(self, num):
        tempSlot = self.getSlot(num)
        self.removeItem(num)
        return tempSlot
    # Takes an item and replaces it with item in slot 'num' in inventory and returns the
    # item previously there.
    def switchItem(self, num, item):
        tempItem = self.inventory[num]
        self.inventory[num] = item
        return tempItem

class Stats:
    def __init__(self, level, HP, MP, defence, accuracy, damageRange, speed, strength, intelligence, wisdom, luck):
        self.level = level
        self.HP = HP
        self.MP = MP
        self.defence = defence
        self.accuracy = accuracy
        self.damageRange = damageRange
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.luck = luck
    def getLevel(self):
        return self.level
    def setLevel(self, level):
        self.level = level
    def getHP(self):
        return self.HP
    def setHP(self,HP):
    	self.HP = HP
    def getMP(self):
        return self.MP
    def setMP(self,MP):
        self.MP = MP
    def getDefence(self):
        return self.defence
    def setDefence(self,defence):
        self.defence = defence
    def getAccuracy(self):
        return self.accuracy
    def setAccuracy(self,accuracy):
        self.accuracy = accuracy
    def getDamageRange(self):
        return self.damageRange
    def setDamageRange(self,damageRange):
        self.damageRange = damageRange
    def getSpeed(self):
        return self.speed
    def setSpeed(self,speed):
        self.speed = speed
    def getStrength(self):
        return self.strength
    def setStrength(self,strength):
        self.strength = strength
    def getIntelligence(self):
        return self.intelligence
    def setIntelligence(self,intelligence):
        self.intelligence = intelligence
    def getWisdom(self):
        return self.wisdom
    def setWisdom(self,wisdom):
        self.wisdom = wisdom
    def getLuck(self):
        return self.luck
    def setLuck(self,luck):
        self.luck = luck
    # Checks if current Stats' STR, INT, WIS, LUCK are greater or equal to
    # stat's.
    def isGreaterEqual(self, stat):
        if self.strength < stat.getStrength() or self.intelligence < stat.getIntelligence() or self.wisdom < stat.getWisdom() or self.luck < stat.getLuck():
            return False
        return True

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self,y):
        self.y = y
