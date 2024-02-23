import mysql.connector
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banking_system"
)
# Create a cursor object to interact with the database
cursor = conn.cursor()
# Create Tables if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        account_number VARCHAR(15) NOT NULL UNIQUE,
        account_holder VARCHAR(255) NOT NULL,
        balance DECIMAL(10, 2) NOT NULL DEFAULT 0.0
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT,
        amount DECIMAL(10, 2) NOT NULL,
        transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
        transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts(account_id)
    )
""")
# Function to create a new account
def create_account(account_number, account_holder):
    query = "INSERT INTO accounts (account_number, account_holder) VALUES (%s, %s)"
    values = (account_number, account_holder)
    cursor.execute(query, values)
    conn.commit()
    print("Account created successfully!")
# Function to read all accounts
def read_accounts():
    query = "SELECT * FROM accounts"
    cursor.execute(query)
    accounts = cursor.fetchall()

    if not accounts:
        print("No accounts found.")
    else:
        for account in accounts:
            print(account)

# Function to update account balance
def update_balance(account_id, amount, transaction_type):
    query = "UPDATE accounts SET balance = balance + %s WHERE account_id = %s"
    values = (amount if transaction_type == 'deposit' else -amount, account_id)
    cursor.execute(query, values)

# Function to perform a transaction
def perform_transaction(account_id, amount, transaction_type):
    update_balance(account_id, amount, transaction_type)

    query = "INSERT INTO transactions (account_id, amount, transaction_type) VALUES (%s, %s, %s)"
    values = (account_id, amount, transaction_type)
    cursor.execute(query, values)
    conn.commit()
    print("Transaction completed successfully!")

# Example Usage
create_account("123342323","Th. John")
read_accounts()

perform_transaction(2, 1050.0, 'deposit')
perform_transaction(2, 50000.0, 'withdrawal')

read_accounts()

# Close the cursor and connection
cursor.close()
conn.close()