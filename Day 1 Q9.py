time=int(input("enter the number of time slots= "))
entry=[int(input("enter the number of quests entering at time slot{}:".format(i+1))) for i in range(time)]
exit=[int(input("enter the number of quests entering at time slot{}:".format(i+1))) for i in range(time)]


count=0
quests= []
for i in range(len(entry)):
       count=count+entry[i]-exit[i]
       quests.append(count)

print("the maximum number of quests present at any time: ",max(quests))
