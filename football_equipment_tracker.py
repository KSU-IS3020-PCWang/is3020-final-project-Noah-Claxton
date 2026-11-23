import csv

FILE_NAME = "equipment_inventory.csv"
FIELDS = ["equipment_id", "type", "size", "condition", "status", "assigned_to"]


def load_inventory():
    inventory = []
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["equipment_id"] != "":
                    inventory.append(row)
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
    except (OSError, KeyError):
        print("Could not read the inventory file. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory):
    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            for item in inventory:
                writer.writerow(item)
        print("Inventory saved.")
    except OSError:
        print("Error: The inventory could not be saved.")


def find_equipment(inventory, equipment_id):
    for item in inventory:
        if item["equipment_id"].lower() == equipment_id.lower():
            return item
    return None


def display_item(item):
    print("ID:", item["equipment_id"])
    print("Type:", item["type"])
    print("Size:", item["size"])
    print("Condition:", item["condition"])
    print("Status:", item["status"])
    print("Assigned to:", item["assigned_to"] if item["assigned_to"] != "" else "Nobody")
    print("------------------------------")


def add_equipment(inventory):
    equipment_id = input("Enter equipment ID: ").strip()
    if equipment_id == "":
        print("ID cannot be blank.")
        return
    if find_equipment(inventory, equipment_id) is not None:
        print("That equipment ID already exists.")
        return

    equipment_type = input("Enter equipment type: ").strip()
    size = input("Enter size (or N/A): ").strip()
    if equipment_type == "" or size == "":
        print("Type and size cannot be blank.")
        return

    print("Condition: 1. Good  2. Needs Repair  3. Replace")
    choice = input("Choose a condition: ").strip()
    if choice == "1":
        condition = "Good"
    elif choice == "2":
        condition = "Needs Repair"
    elif choice == "3":
        condition = "Replace"
    else:
        print("Invalid condition. Equipment was not added.")
        return

    item = {
        "equipment_id": equipment_id,
        "type": equipment_type,
        "size": size,
        "condition": condition,
        "status": "Available",
        "assigned_to": ""
    }
    inventory.append(item)
    save_inventory(inventory)
    print("Equipment added.")


def view_inventory(inventory):
    if len(inventory) == 0:
        print("There is no equipment in the inventory.")
        return
    for item in inventory:
        display_item(item)


def search_equipment(inventory):
    print("1. Search by ID")
    print("2. Search by equipment type")
    choice = input("Choose an option: ").strip()
    if choice != "1" and choice != "2":
        print("Invalid option.")
        return
    search_text = input("Enter search text: ").strip().lower()
    if search_text == "":
        print("Search cannot be blank.")
        return
    matches = 0
    for item in inventory:
        if choice == "1" and search_text == item["equipment_id"].lower():
            display_item(item)
            matches += 1
        elif choice == "2" and search_text in item["type"].lower():
            display_item(item)
            matches += 1
    if matches == 0:
        print("No matching equipment found.")


def assign_equipment(inventory):
    equipment_id = input("Enter equipment ID to assign: ").strip()
    item = find_equipment(inventory, equipment_id)
    if item is None:
        print("Equipment not found.")
        return
    if item["status"] != "Available":
        print("That item is already assigned.")
        return
    if item["condition"] != "Good":
        print("This item needs maintenance or replacement and cannot be assigned.")
        return
    player = input("Enter player's name or number: ").strip()
    if player == "":
        print("Player cannot be blank.")
        return
    item["assigned_to"] = player
    item["status"] = "Assigned"
    save_inventory(inventory)
    print("Equipment assigned to", player)


def return_equipment(inventory):
    equipment_id = input("Enter equipment ID to return: ").strip()
    item = find_equipment(inventory, equipment_id)
    if item is None:
        print("Equipment not found.")
        return
    if item["status"] != "Assigned":
        print("This equipment is not currently assigned.")
        return
    item["status"] = "Available"
    item["assigned_to"] = ""
    save_inventory(inventory)
    print("Equipment returned. Check its condition before assigning it again.")


def update_condition(inventory):
    equipment_id = input("Enter equipment ID: ").strip()
    item = find_equipment(inventory, equipment_id)
    if item is None:
        print("Equipment not found.")
        return
    print("1. Good")
    print("2. Needs Repair")
    print("3. Replace")
    choice = input("Choose the new condition: ").strip()
    if choice == "1":
        item["condition"] = "Good"
    elif choice == "2":
        item["condition"] = "Needs Repair"
    elif choice == "3":
        item["condition"] = "Replace"
    else:
        print("Invalid condition. No changes made.")
        return
    save_inventory(inventory)
    print("Condition updated.")
    if item["status"] == "Assigned" and item["condition"] != "Good":
        print("Warning: This item is assigned to", item["assigned_to"], "and needs attention.")


def inventory_summary(inventory):
    available = 0
    assigned = 0
    needs_repair = 0
    replace = 0
    types = {}
    for item in inventory:
        if item["status"] == "Available":
            available += 1
        elif item["status"] == "Assigned":
            assigned += 1
        if item["condition"] == "Needs Repair":
            needs_repair += 1
        elif item["condition"] == "Replace":
            replace += 1
        equipment_type = item["type"]
        if equipment_type in types:
            types[equipment_type] += 1
        else:
            types[equipment_type] = 1

    print("Total items:", len(inventory))
    print("Available:", available)
    print("Assigned:", assigned)
    print("Needs repair:", needs_repair)
    print("Replace:", replace)
    print("Items by type:")
    for equipment_type in types:
        print(" ", equipment_type + ":", types[equipment_type])


def maintenance_list(inventory):
    count = 0
    print("MAINTENANCE LIST")
    for item in inventory:
        if item["condition"] == "Needs Repair" or item["condition"] == "Replace":
            display_item(item)
            count += 1
    if count == 0:
        print("No items currently need repair or replacement.")
    else:
        print("Items needing attention:", count)


def player_lookup(inventory):
    player = input("Enter player name or number: ").strip().lower()
    if player == "":
        print("Player cannot be blank.")
        return
    count = 0
    print("GEAR ASSIGNED TO PLAYER")
    for item in inventory:
        if item["status"] == "Assigned" and item["assigned_to"].lower() == player:
            display_item(item)
            count += 1
    if count == 0:
        print("No assigned equipment found for that player.")
    else:
        print("Total assigned items:", count)


def end_of_season_report(inventory):
    count = 0
    print("END-OF-SEASON REPORT: ITEMS STILL CHECKED OUT")
    for item in inventory:
        if item["status"] == "Assigned":
            display_item(item)
            count += 1
    if count == 0:
        print("All equipment has been returned!")
    else:
        print("Total items still checked out:", count)


def main():
    inventory = load_inventory()
    while True:
        print("\n===== FOOTBALL EQUIPMENT INVENTORY TRACKER =====")
        print("1. Add equipment")
        print("2. View inventory")
        print("3. Search equipment")
        print("4. Assign equipment")
        print("5. Return equipment")
        print("6. Update equipment condition")
        print("7. Inventory summary")
        print("8. Maintenance list")
        print("9. Player lookup")
        print("10. End-of-season report")
        print("11. Save and exit")
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_equipment(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            search_equipment(inventory)
        elif choice == "4":
            assign_equipment(inventory)
        elif choice == "5":
            return_equipment(inventory)
        elif choice == "6":
            update_condition(inventory)
        elif choice == "7":
            inventory_summary(inventory)
        elif choice == "8":
            maintenance_list(inventory)
        elif choice == "9":
            player_lookup(inventory)
        elif choice == "10":
            end_of_season_report(inventory)
        elif choice == "11":
            save_inventory(inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 11.")


main()
