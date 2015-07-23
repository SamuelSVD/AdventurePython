class EnvironmentComponent:
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

    DEFAULT = 0
    # initiate environment component of environmentType. Other data changes respectively, unless stated otherwise
    def __init__(self, x, y, environmentType, isSolid = DEFAULT, effect = DEFAULT, orientations = DEFAULT):
        self.x = x
        self.y = y
        self.environmentType = environmentType
        self.solid = isSolid
        self.effect = effect
        self.orientation = orientation

        if environmentType == DIRT:
            
    # set location along x
    def setX(self, x):
        self.x = x

    # get location along x
    def getX(self):
        return self.x

    # set location along y
    def setY(self, y):
        self.y = y
    
    # get location along y
    def getY(self):
        return self.y
    
    # get the type of environment
    def getType(self):
        return self.environmentType

    # set block type to environmentType. This will change block's other 
    def setType(self, environmentType):
        self.__init__(self.x, self.y, environmentType)
    
    # return if the component is solid (has collision)
    def isSolid(self):
        return self.solid

    # set whether component is solid or not
    def setSolid(self, solid):
        self.solid = solid
    
    # return the component's effect.
    def getEffect(self):
        return self.effect

    # set component effect to
    def setEffect(self, effect):
        self.effect = effect
    
    # return the component's orientation.
    def getOrientation(self):
        return orientation

    # sets the component's orientation to 'orientation'
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
            grid.append(s)

    # set size along x
    def setX(self,x):
        self.x = x

    # get size along x
    def getX(self):
        return self.x

    # set size along y
    def setY(self,y):
        self.y = y
    
    # get size along y
    def getY(self):
        return self.y
    
    # set the environment component at x,y to 'component'
    def setComponent(self, x, y, component):
        self.grid[x][y] = component

    # get the environment component at x,y
    def getComponent(self, x, y):
        return self.grid[x][y]

    # get the whole environment.
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
    ARMS = 4
    SHOES = 5
    WEAPON = 6
    POTION = 7
    
    # initiate item with itemNumber num. All other data is changed respective to item number
    def __init__(self, num):
        self.itemNumber = num 
        self.name = 'Item'
        self.itemType = ITEM

        self.effect = 'none'
        # represents  the effect it would have if used.
        # self.effect = Attack([0,0,0,0,0,0])
        
        self.equipRequitements = [0,0,0,0,0] # [lvl,STR,INT,WIS,LUCK]
        self.description = 'This is a description'

    # return item number
    def getItemNumber(self):
        return self.itemNumber
    
    # returns if item is of type POTION
    def isUsable(self):
        return self.type == self.POTION
    
    # returns of item is of type HELM->SHOES
    def isEquipable(self):
        return self.type < ITEM and self.type > POTION
    
    # returns the item's name
    def getName(self):
        return self.name

    # set the item's name to 'name'
    def setName(self, name):
        self.name = name
    
    # returns the type of item it is
    def getItemType(self):
        return self.itemType

    # set the item's name to 'name'
    def setItemType(self, itemType):
        self.itemType = itemType
    
    # returns the effects this item causes.
    def getItemEffect(self):
        return self.effect
    
    # set the item's name to 'name'
    def setItemEffect(self, effect):
        self.effect = effect
    
    # returns the requirements to equip item
    def getRequirements(self):
        return self.equipRequirements

    # set the item's name to 'name'
    def setName(self, equipRequirements):
        self.equipRequirements = equipRequirements


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


