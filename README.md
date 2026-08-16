# 💳 In-Memory Expense Tracking & Financial Aggregation Pipeline

---

Welcome to my Python expense tracking and analytics project! This repository contains a modular, lightweight data pipeline built entirely in pure **Python 3**.

As a self-taught aspiring data engineer operating under the moniker **Yanolitics**, I designed this project to demonstrate how transactional expenditures can be systematically validated, stored, dynamically aggregated, and formatted into clean financial reports using core software and data engineering principles.

---

## 🗺️ High-Level Architecture

The pipeline follows a simple, step-by-step workflow: **Check incoming expenses → Save valid entries → Calculate category totals → Print formatted financial reports.**

---

## 🛠️ Pipeline Breakdown

### 1. Checking New Expenses (Validation)

* **What it does:** Receives new expense entries with an amount, category, and description.
* **Safety check:** Ensures the expense amount is greater than $0.00. If someone tries to enter $0 or a negative number, the system catches it immediately and displays a clear error message instead of saving bad data.

### 2. Saving Approved Entries (Storage)

* **What it does:** Acts as a temporary digital ledger (database) to store all validated expenses.
* **How it's stored:** Organizes each expense into a simple record holding three clear fields: amount, category, and description.

### 3. Calculating Totals & Filtering (Analytics)

* **Overall total:** Adds up every saved expense in one quick calculation to show total spending.
* **Category totals:** Calculates total spending for specific categories (like "Food" or "Transport").
* **Smart matching:** Ignores letter casing so searching for "food", "Food", or "FOOD" always returns the correct total.

### 4. Displaying Clean Reports (Formatting)

* **Dollar formatting:** Automatically formats numbers into standard currency values (like `$50.00` instead of `50.0`).
* **Numbered lists:** Automatically numbers each stored expense (1, 2, 3...) when printing the final report to the screen.

### 5. Automated Testing (Test Runner)

* **Sample run:** Runs through a batch of sample expenses to test both good inputs and invalid entries.
* **Doesn't crash on errors:** If a bad test item fails validation, the system logs the error and safely moves on to the next test without crashing the program.

---

## ⚡ Tech Stack & Core Concepts Demonstrated

* **Language:** Python 3
* **Core Paradigms:** Functional Decomposition, Modular Architecture, Explicit Exception Raising (`raise ValueError`), and Localized Error Interception (`try...except`).
* **Data Engineering & Financial Concepts:** Ingestion Pipeline Design, Numeric Bound Enforcement, Case-Insensitive Data Aggregation, Memory-Efficient Generator Expressions, Financial Decimal Formatting, and Resilient Batch Execution.
* **Data Structures:** Dictionaries, List Collections, Tuples, and Generator Expressions.

---

## 👨‍💻 About the Developer

I’m Timothy, a former banking documentation analyst who spent three years managing rigid data compliance and structure. I chose to pivot into the tech sector because I love building systems, wrestling with technical tools, and mastering business intelligence.

I am entirely self-taught through dedicated, project-driven bootcamps and courses. While I am still navigating the earlier stages of my engineering career, I bring an incredibly high tolerance for debugging, a rigorous eye for detail inherited from banking, and a promise to write clean code that minimizes the risk of breaking database production environments.
