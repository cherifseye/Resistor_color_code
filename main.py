import sys 
from PyQt5.QtWidgets import QApplication
import UI
def main():
    app = QApplication(sys.argv)
    ex = UI.codesColor()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()