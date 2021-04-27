class Spot:
    def __init__(self, thing):
        self.thing = thing # specific thing to store
        self.after = None # will change with instance

class LinkedList:
    def __init__(self):
        self.head = None

    def pushOn(self, new_thing):
        new_spot = Spot(new_thing)
        new_spot.after = self.head # because new thing will be at beginning of list b4 the head
        self.head = new_spot # puts the new thing in the head position

    def insertAfter(self, prev_spot, new_thing):
        if prev_spot is None: #ie, does not exist (?)
            print('Given previous spot must NOT be empty') # don't understand this
            return
        # if spot is not empty create a spot instance
        new_spot = Spot(new_thing)

        # update previous spot's old pointer to point to my new spot
        new_spot.after = prev_spot.after

        prev_spot.after = new_spot

    # This will append to the end of the linked list
    def append(self, new_thing):
        # create a new spot with a new thing
        new_spot = Spot(new_thing)

        # check if linked list empty
        # if empty, make this new spot the head spot
        if self.head is None:
            self.head = new_spot

        # but if list not empty, traverse to the end and add new thing there
        end = self.head
        # while end.after is not none continue to loop until a none thing found for next pointer
        while end.after: # same as 'is not None'
            end = end.after

        # change current last spot thing to point at new spot
        end.after = new_spot

    def traverse(self):
        temp = self.head
        # while tem is not none keep looping through links until none thing found
        while temp: # 'is not None'
            print(temp.thing)
            temp = temp.after

weekdays_links = LinkedList()

# insert new day into LL

weekdays_links.pushOn('Mon')
weekdays_links.append('Tues')
weekdays_links.insertAfter(weekdays_links.head.after, 'Wed')
weekdays_links.traverse()


    