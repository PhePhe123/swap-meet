from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
    
    def add(self, item): #this method will add item to the list of self.inventory
        self.inventory.append(item)
        return item
    
    def remove(self, item): #this method will remove the item is present in self.inventory
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id = None): #this method is going to return the item is the id is present in self.inventory
        for item in self.inventory:
            if item.id == id:
                return item 
            # else:
        return None
        
    def swap_items(self, other_vendor,my_item, their_item):
        if self.get_by_id(my_item.id) == None or other_vendor.get_by_id(their_item.id) == None:
            return False #get_by_id is None if the item is not in the inventory
        self.add(their_item) #adding their item to my inventory
        other_vendor.add(my_item) #adding my item in their inventory
        self.remove(my_item) #removing my item from my inventory
        other_vendor.remove(their_item) #removing their item from their inventory
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        self.add(other_vendor.inventory[0])
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        matched_category = [item for item in self.inventory if Item.get_category(item) == category]
        return matched_category 
        #refactored into list comprehension    
        # for item in self.inventory:
        #     if Item.get_category(item) == category:
        #         matched_category.append(item)
        
    
    def get_best_by_category(self, category):
        #refactored into max()
        # matched_category = self.get_by_category(category)
        # if len(matched_category) == 0:
        #     return None
        # highest_condition = 0 
        # for object in matched_category:
        #     if object.condition > highest_condition:
        #         highest_condition = object.condition
        #         highest_valued_object = object
        # return highest_valued_object
        if len(self.get_by_category(category)) == 0:
            return None
        return max(self.get_by_category(category), key = lambda object: object.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if len(other_vendor.get_by_category(my_priority)) == 0 or len((self.get_by_category(their_priority))) == 0 :
            return False
        else:
            self.add(other_vendor.get_best_by_category(my_priority))
            other_vendor.remove(other_vendor.get_best_by_category(my_priority))
            other_vendor.add(self.get_best_by_category(their_priority))
            self.remove(self.get_best_by_category(their_priority))
            return True
        # item_wanted_by_vendor = other_vendor.get_best_by_category(my_priority)
        # item_wanted_by_other_vendor = self.get_best_by_category(their_priority)
        # if item_wanted_by_vendor == None or item_wanted_by_other_vendor == None:
        #     return False
        # return self.swap_items(other_vendor, item_wanted_by_other_vendor, item_wanted_by_vendor)
        

