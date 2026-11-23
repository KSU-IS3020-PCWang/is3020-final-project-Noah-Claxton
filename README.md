# IS 3020 Final Project

## Student and Project Information

- Student name: Noah Claxton
- GitHub username: Noah-Claxton
- Project title: Football Equipment Inventory Tracker
- Application purpose: Track Inventory and Player Equipment

## How to Run the Application

The application is a command-line Python program. Python 3.8 or newer is recommended; it uses only Python's built-in csv module and requires no additional packages. The program has not been tested on every Python version.

Required file: football_equipment_tracker.py. The program reads and writes equipment_inventory.csv in its current working directory. The CSV file is not required for the first run: if it is missing, the program starts with an empty inventory and creates the file when the inventory is saved.
1. Open PyCharm and open the project containing football_equipment_tracker.py.
2. Confirm a Python 3 interpreter is selected under Settings/Preferences > Project > Python Interpreter (the wording may vary by PyCharm version).
3. Make sure the Run configuration's Working directory is your project folder, so the CSV file is stored there.
4. Right-click football_equipment_tracker.py and choose Run 'football_equipment_tracker', or open the file and click the green Run triangle.
5. Use the Run console to enter a menu number from 1 through 11, and follow the prompts.
6. Select 11. Save and exit to save and close the program.
7. To confirm records persist, restart the program and choose 2. View inventory.

## Major Features

Add equipment: Enter a unique item ID, type, size, and condition; duplicate IDs are rejected.
View inventory: Display all items, including assignment and condition information.
Search equipment: Find items by exact ID or a partial equipment-type match.
Assign equipment: Assign an available item in good condition to a player name or number; reject assignments of items already assigned or needing attention.
Return equipment: Mark an assigned item as available and clear its player field.
Update condition: Mark gear as Good, Needs Repair, or Replace; warn when assigned gear needs attention.
Inventory summary: Count total, available, assigned, repair, and replacement items, plus totals by equipment type.
Maintenance list (required): Display all items marked Needs Repair or Replace.
Player lookup: List all equipment currently assigned to one player name or number.
End-of-season report: List all items still assigned and count the total not yet returned.
Save and exit: Write the inventory to disk and close the application.

## Python Concepts Used

Functions: Each task is separated into functions such as add_equipment(), assign_equipment(), maintenance_list(), and end_of_season_report().
Collections: A list holds equipment records in memory; each record is a dictionary with named fields. A separate dictionary counts items by type for the summary.
Conditionals: if, elif, and else handle menu selections, validate input, reject duplicate IDs, and enforce assignment rules.
Loops: A while True loop shows the menu until the user exits. for loops search, display, count, load, and save records.
File persistence: Python's built-in csv module uses csv.DictReader to load saved items and csv.DictWriter to save changes. The program saves after updates and when exiting.
Exception handling: try/except handles missing files (FileNotFoundError) and some reading or writing issues (OSError and KeyError). Invalid menu choices and blank fields are handled with conditional checks rather than exceptions.

## Data Files

equipment_inventory.csv is the only persistent data file used. Each row is one individual piece of equipment, with these six columns:
Field	Purpose
equipment_id	Unique identifier, such as H001
type	Equipment category, such as Helmet
size	Size, such as Large or N/A
condition	Good, Needs Repair, or Replace
status	Available or Assigned
assigned_to	Player name or number; blank if not assigned


No JSON files or database are used. The CSV is created in the Run configuration's working directory, usually the PyCharm project folder.

## Testing Summary

| Scenario | Observed outcome |
|---|---|
| Start with no CSV file | Printed a first-run message and displayed the menu |
| Add two items | Created CSV rows for both items |
| Add a duplicate ID | Rejected the duplicate |
| Assign an item needing repair | Rejected the assignment |
| Assign a good item twice | First assignment worked; second was rejected |
| Look up a player | Listed the player's assigned item |
| Display maintenance list | Listed an item marked Needs Repair |
| Run end-of-season report | Listed an outstanding item before its return |
| Return an item and rerun report | Reported that all gear had been returned |
| Exit and restart | Loaded saved inventory from the CSV |
| Enter blank ID or invalid search option | Printed an error message instead of exiting unexpectedly |

## AI Use

AI assisted with brainstorming the application scope, revising the initial proposal, testing the initial Python application, adding the maintenance list, player lookup, and end-of-season report, and preparing documentation and basic tests. See AI_USAGE.md for the detailed disclosure. 

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
