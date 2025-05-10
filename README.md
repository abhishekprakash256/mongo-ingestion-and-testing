
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

## 🏗 **Project Structure (Optional, if you want to add)**

```
/project-root
│
├── requirements.txt     # Python dependencies
├── config.py             # Configuration (database, paths)
├── data_crud.py         # data crud pperations
└── README.md            # Project documentation
```

---

## 💡 **Future Improvements (Optional Section)**

* Add automated tests for CRUD operations.
* Include CI/CD pipeline integration.
* Add support for multiple database connections.


