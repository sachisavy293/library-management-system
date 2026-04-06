import json

library = {}
issued_books = {}

# -------- LOAD DATA FROM FILE --------
try:
    with open("library.txt", "r") as f:
        data = json.load(f)
        library = data.get("library", {})
        issued_books = data.get("issued_books", {})
except FileNotFoundError:
    print("No previous data found. Starting fresh.")
except json.JSONDecodeError:
    print("File corrupted. Starting fresh.")

# -------- MAIN PROGRAM --------
while True:
    print("\n1.Add 2.Search 3.Issue 4.Return 5.Display 6.Exit")
    
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input! Enter number only.")
        continue

    try:
        if ch == 1:
            name = input("Enter book name: ").strip().lower()
            qty = int(input("Enter quantity: "))
            library[name] = library.get(name, 0) + qty
            print("Book added successfully")

        elif ch == 2:
            name = input("Enter book name: ").strip().lower()
            print("Available:", library.get(name, 0))

        elif ch == 3:
            reg = input("Enter register number: ")
            name = input("Enter book name: ").strip().lower()

            if library.get(name, 0) > 0:
                library[name] -= 1
                issued_books.setdefault(reg, []).append(name)
                print("Book issued successfully")
            else:
                print("Book not available")

        elif ch == 4:
            reg = input("Enter register number: ")
            name = input("Enter book name: ").strip().lower()

            if reg in issued_books and name in issued_books[reg]:
                issued_books[reg].remove(name)
                library[name] += 1
                print("Book returned successfully")
            else:
                print("Invalid return")

        elif ch == 5:
            print("\n--- Library ---")
            for b, q in library.items():
                print(f"{b} : {q}")

            print("\n--- Issued Books ---")
            for r, books in issued_books.items():
                print(f"{r} : {books}")

        elif ch == 6:
            # -------- SAVE DATA TO FILE --------
            try:
                with open("library.txt", "w") as f:
                    json.dump({
                        "library": library,
                        "issued_books": issued_books
                    }, f)
                print("Data saved successfully!")
            except Exception as e:
                print("Error saving file:", e)

            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error occurred:", e)