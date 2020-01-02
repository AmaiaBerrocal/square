square = []
n = 6

for j in range(0,n):
    string = ""
    for i in range(0,n):
        if j == 0 or j == n - 1:
            string += "*"
        else:
            if i == 0 or i == n - 1:
                string += "*"
            else:
                string += " "
    string += "\n"      
    square.append(string)

for item in square:
    print(item)

