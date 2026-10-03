# 🏋️ Gym Membership Manager (Python)

A simple command-line application to manage gym members. You can add new members, view all of them, and search by ID, first name, or membership status.

## ✨ Features

- Add a new member (first name, last name, membership ID, status)
- Display all registered members
- Search for members by:
  - Membership ID
  - First name
  - Membership status (active / inactive)
- Clean terminal menu that works on Windows, macOS, and Linux

## 🛠️ Requirements

- Python 3.6 or higher

No external libraries are needed. The project only uses the built-in `os` and `time` modules.

## 🚀 How to Run

1. Clone this repository or download the files:
```bash
   git clone https://github.com/YOUR-USERNAME/gym-membership-manager.git
```
2. Go to the project folder:
```bash
   cd gym-membership-manager
```
3. Run the program:
```bash
   python gym_manager.py
```

## 🕹️ How to Use

When the program starts, you will see this menu:

```
Welcome to Gym Membership Management!

Choose an action:

1. Add new member
2. Display all members
3. Search for a member
4. Exit
```

Type the number of the action you want and press Enter.

## 📸 Example

```
First name: Ahmed
Last name: Benali
ID: 101
Status: active
```

> **Note:** Data is stored in memory only, so it is lost when you close the program.

## 📚 What I Learned

- Creating classes and objects (OOP) in Python
- Using the `__init__` method and instance methods
- Working with lists of objects
- Building a menu with `while` loops and conditions
- Writing reusable functions
- Clearing the terminal with `os.system`

## 🔮 Future Improvements

- Save members to a file (JSON or CSV) so data is not lost
- Add options to edit and delete members
- Prevent duplicate membership IDs
- Add membership start and end dates

## 👤 Author

**Mehdi**
GitHub: [@ghezzaz-mehdi-dev](https://github.com/ghezzaz-mehdi-dev)
