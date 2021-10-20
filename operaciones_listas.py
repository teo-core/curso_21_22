a = [8,2,3,5,1,6,9,9]
b = ['a','b','c']

total = min(a)
print('Total: ',total)

a.append(9)
a.append(8)
print(a)

a.pop()
print(a)

#sort
a.sort(reverse=True)
print(a)

# extend
a.extend(b)
print(a)

#count
print('cuenta de 9',a.count(9))

#index
print('indice de c', a.index('c'))

#insert
a.insert(5,'nuevo')
print(a)

#remove
a.remove('nuevo')
print(a)


#clear
a.clear()
print(a)




