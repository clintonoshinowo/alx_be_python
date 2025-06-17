def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the shopping list manager application.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop continuously until the user chooses to exit
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ").strip() # Get user's choice and remove whitespace

        if choice == '1':
            # --- Add Item functionality ---
            item = input("Enter the item to add: ").strip()
            # Ensure the item is not empty before adding
            if item:
                shopping_list.append(item) # Add the item to the list
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # --- Remove Item functionality ---
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is empty. Nothing to remove.")
                continue # Skip to the next loop iteration
            
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list: # Check if the item exists in the list
                shopping_list.remove(item) # Remove the first occurrence of the item
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            # --- View List functionality ---
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                # Iterate through the list and print each item with a number
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                print("--------------------------")
        elif choice == '4':
            # --- Exit functionality ---
            print("Goodbye! Your shopping list session has ended.")
            break # Exit the while loop
        else:
            # --- Handle invalid menu choices ---
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
