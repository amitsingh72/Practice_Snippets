#by amit 
#Least cost method 
import numpy as np

'''

cost array = [[19, 30, 50, 10],
     [70, 30, 40, 60],
     [40, 8, 70, 20]]
supply = [7, 9, 18]
demand = [5, 8, 7, 14]
'''

print("******** LEAST COST METHOD ********")
print("\n")

#step1

#input of demand array  
demand_array = []
m = int(input("Size of Demand array:"))
for i in range(m):
    demand_array.append(float(input("Enter the Elements into Demand Array(1 Dim):")))
    
#demand_array = np.array(demand_array) # converting list to demand array
print("Demand Array: {}".format(demand_array))



#input of supply array
supply_array = []
n = int(input("Size of supply array:"))
for i in range(n):
    supply_array.append(float(input("Enter the Elements into Supply Array(1 Dim):"))) # coverting list to supply array
    
#supply_array = np.array(supply_array)
#print(supply_array)

print("supply_array: {}".format(supply_array))



#input of 2 dimensional cost array
lst = [ ] 
n = int(input("Enter number of rows/sublists inside main array : ")) 
#    noofcolumns = int(input("Enter the number of columns"))
for i in range(0, n): 
    ele = [int(input("Enter values into {} Sublist:".format(i))),int(input("Enter values into {} Sublist:".format(i))),int(input("Enter values into {} Sublist:".format(i))), int(input("Enter values into {} Sublist:".format(i)))] 
    lst.append(ele) 
      
    
    
cost_array = lst
#cost_array =lst

print("cost_array: {}".format(cost_array))

 


#this function checkswhether array is valid or not
def ValidArray(arr):
    for i in arr:
        if (i != 0):
            return True
    return False


#this function gives us row and column index of minimum element
def Index(cost_array, n, m):
    min = 9999
    min_i = 0
    min_j = 0
    for i in range(0, n):
        for j in range(0, m):
            if (min > cost_array[i][j]):
                min = cost_array[i][j]
                min_i = i
                min_j = j

    return min_i, min_j



#initialization of variables
y = 0
min_i = 0
min_j = 0
cost = 0

while ValidArray(supply_array) and ValidArray(demand_array): #checking whether arrays are valid are not
    
    min_i, min_j = Index(cost_array, n, m) #mini,minj are index of minimum elemnt chosen for each iteration
    #print(min_i)
    #print(min_j)
    if supply_array[min_i] < demand_array[min_j]:
        cost = cost + (cost_array[min_i][min_j] * supply_array[min_i])

        demand_array[min_j] = demand_array[min_j] - supply_array[min_i]
        supply_array[min_i] = 0
        for j in range(0, m):
            cost_array[min_i][j] = 99999
    else:
        cost = cost + (cost_array[min_i][min_j] * demand_array[min_j])

        supply_array[min_i] = supply_array[min_i] - demand_array[min_j]
        demand_array[min_j] = 0
        for i in range(0, n):
            cost_array[i][min_j] = 99999


print('Total Transportation cost: ', cost)


#step1
m =3 #no of rows
  
n = 4 #no of columnbs 

alloc = 6  #no of allocated cells
 
u1,u2,u3 = 0
v1,v2 ,v3,v4 =0


if m+n-1 == alloc:
    v1= 0 
