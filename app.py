from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASS",
    database="bank_db"
)

db.autocommit = False  # important for transactions

@app.route('/')
def home():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM accounts")
    data = cursor.fetchall()
    return render_template('index.html', data=data)


@app.route('/transfer', methods=['POST'])
def transfer():
    sender = request.form['sender'].strip()
    receiver = request.form['receiver'].strip()
    amount = int(request.form['amount'])

    cursor = db.cursor()

    try:
        db.rollback()
        db.start_transaction()

        # 🔒 Lock sender row
        cursor.execute("SELECT balance FROM accounts WHERE name=%s FOR UPDATE", (sender,))
        sender_data = cursor.fetchone()

        if not sender_data:
            db.rollback()
            return "❌ Sender not found"

        # 💰 Check balance
        if sender_data[0] < amount:
            db.rollback()
            return "❌ Insufficient balance"

        # 🔒 Lock receiver row
        cursor.execute("SELECT balance FROM accounts WHERE name=%s FOR UPDATE", (receiver,))
        receiver_data = cursor.fetchone()

        if not receiver_data:
            db.rollback()
            return "❌ Receiver not found"

        # 💸 Perform transfer
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE name=%s",
            (amount, sender)
        )

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE name=%s",
            (amount, receiver)
        )

        db.commit()
        return "✅ Transaction Successful"

    except Exception as e:
        db.rollback()
        return f"❌ Error: {str(e)}"


app.run(debug=True)
