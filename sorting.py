# student = ["Hina","Ayesha","Rabia","Alishba","Bushra","Laiba","Dia"]
# # above one is list so sort function is giving he result ,but if we change the list
# # into tupple it will not work so there we will use the sorted funtion
# # student.sort()
#
# student.sort(reverse=True)
# for i in student:
#     print(i)

# student = ("Hina","Ayesha","Rabia","Alishba","Bushra","Laiba","Dia")
# # sorted_student = sorted(student)
# sorted_student = sorted(student , reverse=True)
# for i in sorted_student:
#     print(i)




# level 2

# student = [("Hina","C",60),
#            ("Ayesha","B",33),
#            ("Rabia","F",55),
#            ("Alishba","A",98),
#            ("Bushra","D",45),
#            ("Laiba","A",78),
#            ("Dia","C",56)]
#
# # grades = lambda grade:grade[1]
# ages = lambda age:age[2]
# # student.sort(key=grades)
# student.sort(key=ages,reverse=True)
# for i in student:
#     print(i)


# now we have tuples of tuple now wwe cannot use sort method anymore


student = (("Hina","C",60),
           ("Ayesha","B",33),
           ("Rabia","F",55),
           ("Alishba","A",98),
           ("Bushra","D",45),
           ("Laiba","A",78),
           ("Dia","C",56))

ages = lambda age:age[2]
sorted_student = sorted(student,key=ages)

for i in sorted_student:
    print(i)
    