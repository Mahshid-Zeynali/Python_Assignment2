number = int(input("Please enter the number of students in the class : "))
sum = 0
scores = []
for i in range(number) :
    print("Enter the student programming lesson grade ", i+1 , ":" , end =" ")
    scores.append(int(input()))
    sum += scores[i]
    if(i==0) :
        max = min = scores[i]
    if(scores[i] > max) :
        max = scores[i]
    if(scores[i] < min) :
        min = scores[i]

print("Average class scores :", sum/number)
print("Maximum class score :", max)  
print("Minimum class score :", min) 