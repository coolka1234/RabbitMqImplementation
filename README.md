# Event-Driven System with RabbitMQ

This project implements an **event-driven system** using **RabbitMQ** as the message broker. It follows **Clean Architecture** principles and utilizes **publishers and consumers** to handle different event types asynchronously.

## 📌 Features

- **3 Publishers** for `type1` events (fixed interval of 3s)
- **1 Publisher** for `type2` (random interval)
- **1 Publisher** for `type3` (random interval)
- **2 Consumers** for `type1` events
- **1 Consumer** for `type2` events
- **1 Consumer** for `type3` events (which triggers a `type4` event)
- **1 Consumer** for `type4` events
- **Logging** for all operations

---


## Getting Started

### Install Dependencies

Make sure you have Python **3.8+** installed. Then install the required packages:

```sh
pip install -r requirements.txt
```

### Start RabbitMQ

Ensure RabbitMQ is installed and running:

```sh
rabbitmq-server
```

### Run the System

Start all publishers and consumers using the `main.py` script:

```sh
python app/main.py
```

---

## 🛠 Configuration

### 🔹 Environment Variables

Modify `config.py` to set up RabbitMQ connection details:

```python
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
```



### **3. RabbitMQ Not Running**

📌 Fix: Start RabbitMQ manually:

```sh
rabbitmq-server
```

---

## 📌 Future Improvements

- Dockerize
