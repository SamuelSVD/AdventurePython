from classes import *
def nullStats():
    return Stats(0,0,0,0,0,[0,0],0,0,0,0,0)
def printItem(item):
    print item.getName(), item.getItemType()
    print item.getDescription()
# (itemNumber,itemType,name,description,effect,equipRequirements)
null = nullStats()
i_0 = Item(0,Item.WEAPON,'Wooden Sword','A simple wooden sword. It appears to be a toy.',null,Stats(1,0,0,0,0,[0,0],0,5,5,5,5))
i_1 = Item(1,Item.HELM,'Leather Cap',"A simple leather hat. It's a little tight around your head",Stats(1,0,0,1,0,[0,0],0,0,0,0,0),Stats(1,0,0,0,0,[0,0],0,5,5,5,5))
i_2 = Item(2,Item.CHEST,'White T-Shirt',"A white T-Shirt.",Stats(1,0,0,1,0,[0,0],0,0,0,0,0),Stats(1,0,0,0,0,[0,0],0,5,5,5,5))
i_3 = Item(3,Item.LEGS,'Jeans',"Some blue jeans you've had for a long time.",Stats(1,0,0,1,0,[0,0],0,0,0,0,0),Stats(1,0,0,0,0,[0,0],0,5,5,5,5))
i_4 = Item(4,Item.HANDS,'Gloves',"Well.. I guess they are comfortable.",Stats(1,0,0,1,0,[0,0],0,0,0,0,0),Stats(1,0,0,0,0,[0,0],0,5,5,5,5))
i_5 = Item(5,Item.SHOES,'Brown Boots',"Some old boots you found in your closet.",Stats(1,0,0,1,0,[0,0],0,0,0,0,0),Stats(1,0,0,0,0,[0,0],0,5,5,5,5))


#### DO NOT CREATE THIS MODULE YET ####

