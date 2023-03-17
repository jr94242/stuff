import numpy as np
import urllib.request

w1 = 0.3
w2 = 0.2
w3 = 0.5

kanto = [73, 67, 42]
johto = [91, 88, 64]
hoenn = [87, 134, 58]

weights = [w1, w2, w3]

def crop_yield(region, weights):
    global result
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result
    print(f"{region} - {result} tons per hectare")

#crop_yield(kanto, weights)


# this can also be done through numpy

# first, the lists have to be converted to numpy arrays
kanto = np.array([73, 67, 42])
weights = np.array([w1, w2, w3])

#print(np.dot(kanto, weights))  # same output as the crop_yield function

# numpy is like a 100-times faster than normal python operations as it has a C compiler - therefore its use-case

climate_data = np.array([
    [73, 67, 42],
    [91, 88, 64],
    [87, 134, 58]
])  # --> this is a matrix, with numpy arrays you can have any number of dimensional data - 1D, 2D, 3D, etc...

# np.matmul // climate_data @ weights ---> both mean matrix multiplication and can be executed and results will be the same

# this is the syntax to download a file via the urllib package --> timed out so I downloaded it from the course's .ipynb's
#urllib.request.urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 'climate.txt')


climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

#print(climate_data.shape())  # this method in jupyter returns the shape of the data, aka in this case would be (10000, 3) 
# meaning 10 000 rows with 3 columns

yields = climate_data @ weights  # matrix multiplication

# what does that reshape function do? ---> basically rearange the array, instead of 10 000 records in a sigle array, what 
# (10000, 1) tells it to do is "take the array and reshape it so that it has 1 column and 10 000 rows, so that we can later concatenate 
# it to the rest of the dataset that is in those dimensions" 
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

#np.savetxt('climate_results.txt', climate_results, fmt='%.2f', header='temperature, rainfall, humidity, yield_crops', comments='')

# with arrays you can do many things, for example scalar operations
# arr3 + 3 --> will add 3 to each element in the array, same with arr3 / 0.5

# it also supports broadcasting, aka inter-array operations with arrays with different structures

arr2 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,1,2,3]
])

arr3 = np.array([4,5,6,7])

arr4 = arr2 + arr3  # this makes the operation, because they are compatible, aka, they both have 4 elements in the sub-array 

# broadcasting only works if one of the arrays can be replicated to take the shape of the other array

#print(arr4)

# array indexing and slicing can be done the following way
#print(arr2[1, 1]) # corresponds to 6

# it also supports ranges

# there are different functions to create arrays 

arr5 = np.arange(10, 90, 3).reshape(3,3,3)

#print(arr5)

# there are some exercises (100 numpy exercises) and the assigment about the 5 functions, each with its use-case from 3 examples, 1 error 
# you can do that after the course in case you are having some trouble with numpy, should help you get your hands dirty








































































































































































































































