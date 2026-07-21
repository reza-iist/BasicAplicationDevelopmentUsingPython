import csv
import os

filename = "fruits_inventory.csv"

def add_fruits():
    number = int(input("How many fruits do you want to add? "))

    # File নতুন বা empty হলে header প্রয়োজন
    new_file = not os.path.exists(filename) or os.path.getsize(filename) == 0

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if new_file:
                writer.writerow([
                    "Fruit Name",
                    "Unit Price (TK)",
                    "Quantity",
                    "Total Price (TK)"
                ])

            for i in range(number):
                print(f"\nFruit {i + 1}")

                name = input("Fruit name: ")
                price = float(input("Unit price: "))
                quantity = int(input("Quantity: "))
                total = price * quantity

                writer.writerow([name, price, quantity, total])

        print("\nFruit data added successfully.")

    except PermissionError:
        print("\nPlease close the CSV file from Excel and try again.")


def show_fruits():
    print("\n--- Fruit Inventory ---")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                print(", ".join(row))

    except FileNotFoundError:
        print("No fruit data found.")


def main():
    while True:
        print("\n======================")
        print(" Fruit Inventory Menu")
        print("======================")
        print("1. Add fruits")
        print("2. Show fruits")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_fruits()
        elif choice == "2":
            show_fruits()
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Invalid option. Choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
