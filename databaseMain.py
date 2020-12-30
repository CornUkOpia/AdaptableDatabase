from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLabel, QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
import sys

class customerProfile(QWidget):
    def __init__(self,customerId):
        QWidget.__init__(self)
        self.setWindowTitle("Customer Profile")
        label = QLabel(self)
        label.setText("CUSTOMER PROFILE")
        label.setFont(QFont("Arial",11))
        verticalBox = QVBoxLayout()
        verticalBox.addWidget(label)
        horizontalBox = QHBoxLayout()

        self.returnToStore = QPushButton("Return to Store")
        self.returnToStore.clicked.connect(lambda: self.toMain())
        
        self.editProfile = QPushButton("Edit Profile")
        self.editProfile.clicked.connect(lambda: self.toMain())
        
        self.orderHistory = QPushButton("View Order History")
        self.orderHistory.clicked.connect(lambda: self.toOrderHistory(customerId))
        
        horizontalBox.addWidget(self.returnToStore)
        horizontalBox.addWidget(self.editProfile)
        horizontalBox.addWidget(self.orderHistory)

        verticalBox.addLayout(horizontalBox)

    def toOrderHistory(self,customerId):
        self.w = orderHistory(customerId)
        self.w.show()
        self.hide()

class editProfile(QWidget):
    def __init__(self,customerId):
        QWidget.__init__(self)
        self.setWindowTitle("Edit Profile")
        label = QLabel(self)
        label.setText("EDIT PROFILE")
        label.setFont(QFont("Arial",11))
        verticalBox = QVBoxLayout()
        verticalBox.addWidget(label)
        horizontalBox = QHBoxLayout()

        self.returnToProfile = QPushButton("Return to Profile")
        self.returnToProfile.clicked.connect(lambda: self.toProfile(customerId))
        
        self.editProfile = QPushButton("Edit Profile")
        self.editProfile.clicked.connect(lambda: self.toMain())
        
    
        
        horizontalBox.addWidget(self.returnToProfile)
        horizontalBox.addWidget(self.editProfile)


        verticalBox.addLayout(horizontalBox)

    def toProfile(self,customerId):
        self.w = customerProfile(customerId)
        self.w.show()
        self.hide()

class orderHistory(QWidget):
    def __init__(self,customerId):
        QWidget.__init__(self)
        self.setWindowTitle("Order History")
        label = QLabel(self)
        label.setText("ORDER HISTORY")
        label.setFont(QFont("Arial",11))
        verticalBox = QVBoxLayout()
        verticalBox.addWidget(label)
        horizontalBox = QHBoxLayout()

        self.returnToStore = QPushButton("Return to Store")
        self.returnToStore.clicked.connect(lambda: self.toMain())

        self.returnToProfile = QPushButton("Return to Profile")
        self.returnToProfile.clicked.connect(lambda: self.toProfile(customerId))
        horizontalBox.addWidget(self.returnToProfile)

        horizontalBox.addWidget(self.returnToStore)
        verticalBox.addLayout(horizontalBox)

    def toProfile(self,customerId):
        self.w = customerProfile(customerId)
        self.w.show()
        self.hide()

class orderPage(QWidget):
    def __init__(self,customerId, orderNumber):
        QWidget.__init__(self)
        self.setWindowTitle("Order Page")
        label = QLabel(self)
        label.setText("ORDER #" + str(orderNumber))
        label.setFont(QFont("Arial",11))
        verticalBox = QVBoxLayout()
        verticalBox.addWidget(label)
        horizontalBox = QHBoxLayout()

        self.returnToStore = QPushButton("Return to Store")
        self.returnToStore.clicked.connect(lambda: self.toMain())

        self.returnToProfile = QPushButton("Return to Profile")
        self.returnToProfile.clicked.connect(lambda: self.toProfile(customerId))
        horizontalBox.addWidget(self.returnToProfile)

        horizontalBox.addWidget(self.returnToStore)
        verticalBox.addLayout(horizontalBox)

    def toProfile(self,customerId):
        self.w = customerProfile(customerId)
        self.w.show()
        self.hide()






def createTable(tableName, tableParameters):
    createTable = QSqlQuery()
    createTableQueryString = """CREATE TABLE """ + str(tableName) + """("""+ str(tableParameters) +""")"""
    createTable.exec(createTableQueryString)

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName("adaptableDatabaseMain")

app = QApplication(sys.argv)

if not connection.open():
    QMessageBox.critical("Unable to open connection", "Can't connect lol")
    sys.exit(1)

print(connection.tables())
win = QLabel("Connection Successful")
win.setWindowTitle("Database Name")
win.resize(200,100)
win.show()
sys.exit(app.exec_())
