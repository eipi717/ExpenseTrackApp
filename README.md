# Expense Track App

[![License](https://img.shields.io/github/license/dec0dOS/amazing-github-template.svg?style=flat-square)](LICENSE)
[![made by Nicholas Ho](https://img.shields.io/badge/Created%20by-NicholasHo-red.svg?style=flat-square)](https://www.linkedin.com/in/nicholaschho/)
[![Demo](https://img.shields.io/badge/Demo%20site-blue)](http://192.18.148.63)

A simple expense tracking app that helps you manage your finances by tracking transactions, calculating tips, and splitting bills.

## Features

## Lightweight Performance

- This app runs efficiently on a **1 GB VM**, consuming minimal resources.

### **Resource Usage**

#### **System Resource Consumption**
- **Memory Used:** ~261MB  
- **CPU Usage:** **0.2% (idle)**  
    ![System Performance](/performances/system-performance.png)

#### **Docker Image Size**
- **Container Size:** **580MB**  
![Docker Image](/performances/docker-image-size.png)

### Tip Calculator
- Calculates tip percentages (10%, 12%, 15%, 18%) based on the bill amount.
- Provides a quick and easy way to determine the total amount including tips.
- Allows navigation back to the dashboard.


### Expense Tracker
- Records transactions as either **income** or **expense**.
- Displays transaction history with **description, amount, and date**.
- Helps users track spending habits over time.

### Bill Splitting
- Supports **equal bill splitting** and **item-based splitting**.
- Allows adding multiple participants for bill division.
- Calculates each person's share, including tip options.

### User Authentication (Login/Logout)
- Secure login system with **username and password** stored in SQLite3.
- Logout functionality to ensure session security.

## Technologies Used
| Technology | Description           |
|--|-----------------------|
| Flask | Backend API & Routing |
| SQLite3 | Database for storing users and transactions |
| HTML, CSS, JavaScript | Frontend for UI |
| Docker | Containerized Deployment |

## Project Structure
```
.
├── Dockerfile                # Containerization setup
├── README.md                 # Project documentation
├── app.py                    # Flask backend application
├── expense-track.db           # SQLite3 database file
├── requirements.txt           # Dependencies list
├── static                     # Static files (CSS, JS)
│   ├── css
│   │   └── style.css          # Stylesheet for UI
│   └── js
│       └── script.js          # JavaScript for UI interactions
└── templates                  # HTML templates for UI
    ├── dashboard.html         # Dashboard page
    ├── expense_tracker.html   # Expense tracking page
    ├── home.html              # Landing page
    ├── login.html             # User authentication page
    ├── split_bill.html        # Bill splitting page
    └── tips_calculator.html   # Tip calculator page
```

## Database Schema
### User table
```sqlite
CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
password_hash TEXT NOT NULL
);
```

### Expense table
```sqlite
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

## Future Improvements
- Keep the app lightweight 
- Add user registration  
- Implement data visualization for spending analysis  
- Export transaction history to CSV

## Contact
For any issues, please do not hesitate to contact me at:
- Email - `nicholasriven717@gmail.com`
- LinkedIn - [Click the Link](https://www.linkedin.com/in/nicholaschho/)

## License
This project is licensed under the **MIT License**.