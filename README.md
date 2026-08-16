# 💳 In-Memory Expense Tracking & Financial Aggregation Pipeline

---

Welcome to my Python expense tracking and analytics project! This repository contains a modular, lightweight data pipeline built entirely in pure **Python 3**.

As a self-taught aspiring data engineer operating under the moniker **Yanolitics**, I designed this project to demonstrate how transactional expenditures can be systematically validated, stored, dynamically aggregated, and formatted into clean financial reports using core software and data engineering principles.

---

## 🗺️ High-Level Architecture

The pipeline follows a modular ETL and analytics lifecycle (**Ingestion & Validation → In-Memory Storage → Case-Insensitive Aggregation → Visual Financial Output**) to ensure numeric accuracy and reporting integrity.

---

## 🛠️ Pipeline Breakdown

### 1. Ingestion & Validation Layer

* **Purpose:** Accepts incoming transaction payloads (`amount`, `category`, `description`).
* **Numeric Boundary Enforcement:** Evaluates transaction value to ensure it meets strict positive bounds (`amount > 0.0`).
* **Exception Handling:** Explicitly raises a `ValueError` with detailed error messaging if non-positive or malformed amounts are submitted.

### 2. Persistence Layer (Storage Simulation)

* **Purpose:** Acts as the primary ledger for all validated expense entries.
* **Object Type:** In-memory list collection (`expenses`).
* **Data Model:** Array of Dictionaries (JSON-like schema: `{"amount": float, "category": str, "description": str}`).

### 3. Aggregation & Analytics Layer

* **Purpose:** Computes global financial metrics and filtered category rollups.
* **Global Total Summation:** Uses a Pythonic generator expression within `sum()` for memory-efficient iteration over all recorded expense objects.
* **Case-Insensitive Category Filtering:** Applies string normalization (`.lower()`) on both stored categories and query inputs, ensuring accurate financial rollups regardless of user casing variations (e.g., matching `"food"` with `"Food"`).

### 4. Display & Reporting Layer

* **Purpose:** Formats raw ledger data into clean, readable financial logs.
* **Currency Standardization:** Formats floating-point values into standard currency representations (`$XX.XX`).
* **Sequential Line-Item Indexing:** Leverages `enumerate(..., start=1)` for clean 1-based terminal logging without manual counter variables.

### 5. Resilient Test Runner

* **Purpose:** Executes automated test scenarios to verify both successful state changes and error handling.
* **Fault-Tolerant Execution:** Encloses individual test operations inside localized `try...except` blocks within an iteration loop, allowing the test suite to log validation failures without terminating the entire pipeline execution.
* **Module Execution Guard:** Uses the standard `if __name__ == "__main__":` entry point to ensure safe module imports and standalone execution.

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
