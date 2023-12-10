# Function to perform a descending bubble sort on the given list
def triee(tab):
    # Iterate through each element in the list
    for b in range(len(tab)):
        # Compare the current element with the elements after it
        for i in range(b + 1, len(tab)):
            # Check if the current element is less than the one after it
            if tab[b] < tab[i]:
                # Swap the elements if the condition is true
                temp = tab[b]
                tab[b] = tab[i]
                tab[i] = temp
    # Return the sorted list
    return tab

# Function to display the elements of a list
def Afficher(tab):
    print(tab)

# Example list
tab = [8, 6, 14, 25, 0, -1, -100, 15]

# Call the triee function to sort the list
tab1 = triee(tab)

# Call the Afficher function to display the sorted list
Afficher(tab1)
