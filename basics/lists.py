squares = [1, 4, 9, 16, 25]
print squares
print squares[0]  # indexing returns the item
print squares[-1]
print squares[-3:]  # slicing returns a new list
print squares[:]

squares2 = squares + [36, 49, 64, 81, 100]
print squares2

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print cubes
cubes[3] = 64  # replace the wrong value
print cubes
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print cubes

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print letters
letters[2:5] = ['C', 'D', 'E']
print letters
# now remove them
letters[2:5] = []
print letters
print len(letters)


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x
print x[0]
print x[0][1]