scores = [3,7,2,9,4,1,8,5,6]
input("List: " + str(scores) + "n = 9 Linear search-checls left to right. Press Enter")
target=int(input("Enter a number to search for: "))
input("Searching for " + str(target) + ". Press Enter to run ")
steps=0
for score in scores:
    steps+=1
    if score == target:
        break
print(" target =", target, " found at position", steps, " checks =", steps)

input("Compare with best and worse case. Press Enter")
mid= len(scores) // 2