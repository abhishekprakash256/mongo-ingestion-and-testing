
# 📦 **Data Ingestion and Testing**

## ✨ Description

This repository provides tools for **data insertion, deletion, update, and retrieval** operations on a MongoDB database.
It is designed for use during **deployment workflows**, supporting both development and production environments.

---

## ⚙️ **Requirements**

* **Python 3.x**
* **Mongo-helper-kit** git+https://github.com/abhishekprakash256/mongo-helper-kit.git
* **MongoDB** (Docker container recommended)

---

## 🚀 **Setup and Commands**

### 1️⃣ Run MongoDB using Docker:

```bash
docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest
```

### 2️⃣ Install dependencies:

```bash
pip install mongo-helper-kit
```

---

## 🔑 **Important Points**

* **Docker must be running** for MongoDB-based data ingestion.
* The **`mongo-helper-kit`** Python package is required for database operations.
* You can use:

  * `localhost`
  * or the container host name `mongo`
    depending on your network setup.

* You can **customize**:

  * Database name
  * Collection name
  * File path
    for development vs. production.

---

# 📄 **Database Operations Module**

This module (`data_crud.py`) provides utility functions to interact with a MongoDB database using the **`mongo_helper_kit`** library.
It is designed to help you **create, insert, view, delete, and query data** in a MongoDB database during development or testing.

---

### 🔧 **Main Function**

---


## 🏗 **Project Structure (Optional, if you want to add)**

```
/project-root
│
├── requirements.txt     # Python dependencies
├── config.py             # Configuration (database, paths)
├── data_crud.py         # data crud pperations
└── README.md            # Project documentation
```

## `perform_database_operations()`

### 🛠 Description

This function performs various database operations, including:

✅ **Create** database and collection
✅ **Insert** data from a JSON file
✅ **Delete** the entire database (⚠ caution!)
✅ **Show** all data
✅ **Query** specific article data

Operations can be **enabled or disabled** by **uncommenting** specific lines inside the function.

---

### ⚙ **Function Signature**

```python
def perform_database_operations():
    """
    Perform various database operations:
    - Create database and collection (optional)
    - Insert data
    - Delete database (CAUTION!)
    - Show all data
    - Get article data (example)
    """
```

---

### 📦 **How It Works**

1️⃣ **Initialize Helper**
Uses `initialize_helper(MONGO_HOST_NAME)` to set up the MongoDB connection.

2️⃣ **Load JSON Data**
Loads JSON data from the file path specified in `config.py`.

3️⃣ **Run Operations**
Depending on which lines you uncomment, it can:

* Create a database/collection
* Insert data
* Delete the entire database
* Show all data
* Query specific documents

---

### 🏗 **Setup Requirements**

✅ MongoDB running (local or in Docker)
✅ Python environment with:

* `mongo_helper_kit`
* `json`

✅ Configuration in `config.py`:

* `DB_NAME`: Name of the database
* `COLLECTION_NAME`: Name of the collection
* `MONGO_HOST_NAME`: MongoDB host (e.g., `localhost`)
* `FILE_PATH`: Path to JSON file with data

---

### 🚀 **How to Run**

```bash
# Start MongoDB (if using Docker)
docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest

# Run the script
python data_crud.py
```

---

### ⚠ **Important Notes**

* Be careful when running `db_helper.delete_db()` — it deletes the **entire database**.
* To avoid running all operations at once, only uncomment the sections you need.

---


## 💡 **Future Improvements (Optional Section)**

* Add automated tests for CRUD operations.
* Include CI/CD pipeline integration.
* Add support for multiple database connections.


