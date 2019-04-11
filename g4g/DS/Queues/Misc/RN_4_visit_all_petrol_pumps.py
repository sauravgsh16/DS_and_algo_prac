''' Find the first circular tour that visits all petrol pumps '''

''' Need to return starting point from where circular tour can be made '''


# METHOD 1

class PetrolPump(object):

    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


def print_tour(arr):

    n = len(arr)

    start = 0
    end = 1

    curPetrol = arr[start].petrol - arr[start].distance
    print 'curPetrol start', curPetrol
    while end != start or curPetrol < 0:
        while curPetrol < 0 and start != end:

            curPetrol -= arr[start].petrol - arr[start].distance
            print 'curPetrol here', curPetrol
            start = (start + 1) % n

            if start == 0:
                return -1
        
        curPetrol += arr[end].petrol - arr[end].distance
        print 'curPetrol add', curPetrol
        end = (end + 1) % n
    
    return start

def method_1():
    arr = [PetrolPump(6,4), PetrolPump(3,6), PetrolPump(7,3)]
    start = print_tour(arr)
    if start == -1:
        print 'No solution'
    else:
        print start

#########################################################################

# METHOD 2
'''
Start from P1. and store last = last +=fuel-distance Array
before starting last=0
Point  last = last + fuel-distance (before refueling)
P1     -3 ( 0 + 5 - 8 )
P2     -4 ( -3 + 3 - 4 )
P3      1 ( -4 + 12 - 7)
P4     -2 ( 1 + 1 - 4 )
P5      0 ( -2 + 7 - 5 )
Now as at last we can reach with 0 value.
We can travel this cities with 'X' location/city/petrol.
X will be next station of smallest last value. ie : P3 here.
(start from p3, You have 12 lit fuel next station P4 at 7 distance remaining fuel at P4 is 5, 
from there take 1 unit of fuel now you have 6. next station P5 at distance 4 , 
remaining fuel at P5 is 2, get 7 units fuel from P5 and go to P1... You can complete cycle
'''

def find_position(arr):
    start = 0
    last = 1
    min_fuel = 1
    min_pos = 0
    n = len(arr)
    while start < n:
        last += arr[start].petrol - arr[start].distance
        start += 1
        if last < min_fuel:
            min_fuel = last
            min_pos = start % n
    return min_pos

arr = [PetrolPump(6,4), PetrolPump(3,6), PetrolPump(7,3)]
print find_position(arr)
