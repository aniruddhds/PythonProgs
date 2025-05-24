"""
items will include the following:
    arrow
    gold coin
    rope
    torch
    dagger
"""
def displayInventory(inventory):
    item_total = 0
    for item, quan in inventory.items():
        print(quan, end=' ')
        print(item)
        item_total += quan
    print("Total number of items: " + str(item_total))

def inventoryUpdater(origInv,lootInv):
    for origItem,origQuan in origInv.items():
        for lootItem,lootQuan in lootInv.items():
            if origItem == lootItem:
                origInv[origItem] = origQuan + lootQuan

# print("The available items are: ")
# print("Arrow","Gold Coin","Rope","Torch","Dagger",sep='\t')

# items=['rope','torch','dagger','gold coin','arrow']

yourStuff={'rope':1, 'torch':4, 'dagger':3,'gold coin':500}
print("Your inventory: ")
displayInventory(yourStuff)

loot={'rope':3, 'torch':5,'dagger':2,'gold coin': 567}
print("Your loot: ")
displayInventory(loot)

inventoryUpdater(yourStuff,loot)
print("Your updated inventory with the loot: ")
displayInventory(yourStuff)