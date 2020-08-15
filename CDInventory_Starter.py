#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# Sbakker, 8/10/2020, created file
# Sbakker, 8/11/2020, edited file - added functionality of loading data
# Sbakker, 8/13/2020, edited file - added functionality to delete data
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            Row1 = row.strip().split(',')
            dicRow = {'ID': int(Row1[0]), 'Title': Row1[1],'Artist': Row1[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print(lstTbl)
        
        pass
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = [intID, strTitle, strArtist]
        lstTbl.append(lstRow)
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row, sep = ', ')
    
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print("enter ID of the entry you want to delete")
        deleteditem = input()
        deleteditem = int(deleteditem)
        with open(strFileName, "r") as f: 
            data = f.readlines() 
        objFile = open (strFileName, 'w')
        for line in data:
            if line.strip("\n") != 'deleteditem':
                objFile.close()
                
            pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

