import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Layout তৈরি করছি
        self.layout = QVBoxLayout()

        # প্রথম টেক্সট বক্স
        self.num1 = QLineEdit(self)
        self.num1.setPlaceholderText("Enter first number")
        self.layout.addWidget(self.num1)

        # দ্বিতীয় টেক্সট বক্স
        self.num2 = QLineEdit(self)
        self.num2.setPlaceholderText("Enter second number")
        self.layout.addWidget(self.num2)

        # যোগ করার বোতাম
        self.button = QPushButton("Add", self)
        self.button.clicked.connect(self.add_numbers)
        self.layout.addWidget(self.button)

        # রেজাল্ট দেখানোর জন্য লেবেল
        self.result = QLabel("Result will be shown here", self)
        self.layout.addWidget(self.result)

        # Layout সেট করা হচ্ছে
        self.setLayout(self.layout)

        # উইন্ডোর টাইটেল এবং সাইজ
        self.setWindowTitle("PyQt5 Simple Calculator")
        self.setGeometry(200, 200, 300, 200)

    def add_numbers(self):
        try:
            # ইনপুট থেকে সংখ্যা নেওয়া হচ্ছে
            num1 = float(self.num1.text())
            num2 = float(self.num2.text())

            # সংখ্যা যোগ করে রেজাল্ট লেবেলে দেখানো হচ্ছে
            result = num1 + num2
            self.result.setText(f"Result: {result}")
        except ValueError:
            self.result.setText("Please enter valid numbers!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
