def createList(title):
    newList = []
    task = input("Enter a task(Leave blank when finished): ")

    while task != "":
        newList.append(task)
        task = input("Enter a task(Leave blank when finished): ")

    newList.append(title)

    while True:
        match input("Would you like to view this your new list?(Y/N): ").upper():
            case "Y":
                displayList(newList)
                break
            case "N":
                break
            case _:
                print("ERROR")

    return newList

def displayList(list):
    print()
    print(f"--- {list[-1]} ---")
    for i in range(len(list)-1):

        print(f"{i+1}. {list[i]}")

def deleteList(lists):
    selection = selectList(lists)
    print("\n" + selection[-1] + " has been deleted.")
    lists.remove(selection)



def selectList(lists):
    print("\n--- Lists ---")

    for i in range(len(lists)):
        print(f"{i + 1}. {lists[i][-1]}")

    selection = int(input("\nEnter the number of the list you want to select: "))

    return lists[selection-1]

def main():
    print("Welcome to Checklist App! ")
    lists = []
    while True:
        print("\nMain Menu")
        print("1) Create List")
        print("2) View list")
        print("3) Edit list")
        print("4) Delete list")
        print("5) Exit")

        menuSelection = input("Enter an option(1/2/3/4/5): ")


        if menuSelection == "1":
            lists.append(createList(input("\nEnter a Title for your new List: ")))
        elif menuSelection == "2":
            if not lists:
                print("No lists to select")
            else:
                list = selectList(lists)
                displayList(list)
        elif menuSelection == "3":
            print("This is where you edit the list")
        elif menuSelection == "4":
            deleteList(lists)
        elif menuSelection == "5":
            break
        else:
            print("ERROR")

main()