# UniStock

Inventory control system developed in Python for the Software Engineering practical assignment.

UniStock is a terminal-based application created to manage inventory operations, allowing item registration, stock updates, and movement tracking.

## Features

* Item registration
* Stock entry
* Stock withdrawal
* Movement history
* Input validation
* Item search by code
* Inventory quantity control

## Technologies

* Python 3
* Dictionaries and lists for in-memory storage
* Terminal interface (CLI)

## Project Structure

```plaintext
unistock/
│
├── README.md
├── src/
│   ├── main.py
│   ├── stock.py
│
├── docs/
│   ├── requirements.docx
│   └── kanban.png
│
├── screenshots/
│   └── execucao_terminal.png
│
├── tests/
├── requirements.txt
├── .gitignore
└── LICENSE
```

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Access the project folder:

```bash
cd unistock
```

3. Run the application:

```bash
python src/main.py
```

## System Flow

1. Register an item
2. Perform stock entry
3. Perform stock withdrawal
4. Track movement history

## Business Rules

* Item code must be unique
* Item code cannot be zero
* Item name must contain at least 2 characters
* Stock quantity cannot become negative
* Dates must follow the format DD/MM/YYYY
* All stock movements are stored in history

## Future Improvements

* Data persistence using JSON
* Graphical interface
* User authentication
* Dashboard and reports

## Author

Developed as an academic project for Software Engineering.