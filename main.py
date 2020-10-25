import math

def main(n):
    out = [[1]] # Initalise the first element in the list
    lastLn = out[0] # Last line is a variable used to keep track of the last line that we created since we need it to make the next line

    for i in range(0, n): # Loop the number of lines we want to make
        indx = 0
        tmp = [1] # This is the line that we are constructing ALL lines start with a 1
        for x in lastLn: # Loop over the last line

            try: # We try to add the numbers if it fails it will be because we are at the end of the list
                tmp.append(x + lastLn[indx + 1]) # We append the current number in the last line plus the number after that
            except IndexError: # If we get an index error from the line above we are at the end of the list
                tmp.append(1) # And since we got the error we append 1 to tmp
            indx += 1 # Increase the indx counter by 1

        out.append(tmp) # Appennd that row
        lastLn = tmp # Update last line

    maxNum = len(str(max(out[-1]))) # Get the length of the largest number in out for calculating the distance between each element in the output
    maxDist = maxNum + 1 # Add at least one space between each element

    if maxDist % 2 == 1: # If the max distance is odd we make it even
        maxDist += 1 # Here we add one to max dist to make it an even number

    printLines = ["".join([f"{x:<{maxDist}}" for x in y]) for y in out] # Genarate all the strings we need to print

    indx = n # Keep track of the amount of lines left
    for i in printLines: # Loop over the strings we need to print
        print(f"{' ' * round(indx * maxDist / 2)}{i}") # Print the amount of space to the side needed to make it a triange and the number itself
        indx -= 1 # Decreace indx by one

if __name__ == '__main__':
    n = input("n: ")
    main(int(n))
