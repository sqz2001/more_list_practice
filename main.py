"""The practice problem on p46 says to think of 5 places in the world you'd like to visit,
 and to make a list with the 5 places.
I would like to visit:
1) Japan
2) Faroe Islands
3) Scotland
4) Switzerland
5) Canada
"""
list = ["Japan", "Faroe Islands", "Scotland", "Switzerland", "Canada"]

"""Now the practice problem says to print the list"""
print(list)

"""now put the list in alphabetical order without modifying the actual list. then show the list is still in its original
order by printing it"""
print(sorted(list))
print(list)

"""now print the list in reverse alphabetical order without changing the original list"""
#giving the sorted list its own variable and reversing it to preserve the original
a = sorted(list)
a.reverse()
print(a)

#printing original list to check that it is unaffected
print(list)




