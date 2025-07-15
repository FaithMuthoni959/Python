class CIRCULARARRAYQUEUE:#FIFO
    #define max no. of elements
    DEFAULT_CAPACITY=10

    def __init__(self):
    # create 10 empty slots in a list/array
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY
        self._size = 0 # keep track of how many elements are in the list
        self._front=0 #first element

    def __len__(self):# returns size of an attribute
        return self._size

    def is_empty(self):
        return self._size == 0  # returns true if array is empty

    def first(self):#used to peek
        if self.is_empty():
            raise Empty('Queue is empty')
        #the front element is at position self._front in array
        return self._data[self._front]

    def dequeue(self):
        #remove and return first element
        #we move front  pointer to the next position using modulo arithmetic to wrap around when we reach the end of the array
        if self.is_empty():
            raise Empty('Queue is empty')#raise an error

        item_to_dequeue=self._data[self._front] #store element at the front in an attribute

        self._data[self._front] = None#garbage collection - helps with memory allocation and deallocation enusring efficient memory use
        # % operator helps wrap around where if we are on last position and add one we go back to the first
        self._front = (self._front + 1) % len(self._data)
        self._size-=1#reduce queue size by one
        return item_to_dequeue
    def enqueue(self,element):#add an element to the rear of the queue
        #uses modulo arithmetic to calculate back of queue
        # check if queue size is full and if full increase size of queue
        if self._size == len(self._data):
            self._resize(2*len(self._data))#double capacity
            #calculate back of queue

        back_of_queue = (self._front + self._size) % len(self._data)
        #place element at new position at back of queue
        self._data[back_of_queue] = element
        #increase size of queue by one
        self._size+=1

    #if queue is full  and we need to enqueue
    def _resize(self,new_capacity):
        #we need to create a linear arrangement to increase easily
        #create a bigger array
        old_data = self._data#hold existing data
        self._data = [None] * new_capacity #resizing by new factor
        #copy elements back in queue
        current_index = self._front
        for item in range (self._size):
            #copy to new array
            self._data[item] = old_data[current_index]
            #move to next element and wrap around
            current_index = (current_index + 1) % len(old_data)

        self._front = 0#reset front position to 0
class Empty(Exception):
    #class with custom exception message
    def _init_(self,message="Queue is empty"):
        self.message=message
        super().__init__(self.message)


if __name__ == '__main__':
    queue=CIRCULARARRAYQUEUE()
    print("Queus using circular arrays")
    print(f"The initial queue size is : {len(queue)}")
    print(f"Is queue empty?{queue.is_empty()}")
    #enqueue the queue
    print("\n Enqueueing our queue")
    elements_to_enqueue = ['Alice','Bob','William','Dorothy','Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added{person}.Queue size is now:{len(queue)}")
    # show the front eleemnt without removing
    print(f"\n Person at the front of the line : {queue.first()}")

    #remove some elements then return.
    print("\n Serving people from the front of the queue:")
    for i in range(3):
        served_person=queue.dequeue()
        print(f"Served:{served_person}. Queue size is now: {len(queue)}")

    #induce an overflow to demo circular nature
    print("\n Adding more people to induce a wrap around")
    more_people = ['Frank','Linda','Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    #show what is left in queue
    print(f"\n Person at front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    #demonstrate the wrap around
    print(f"\n Internal details:")
    print(f"\n Front index: {queue._front}")
    print(f"\n Array contents: {queue._data}")