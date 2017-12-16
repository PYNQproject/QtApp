import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
import loader_ui
import urllib.request

class MainScreen(QtWidgets.QMainWindow,  loader_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        geometry= QDesktopWidget().screenGeometry()
        self.pushButton.move(geometry.width()/2-self.pushButton.frameGeometry().width()/2,
                            0.1 * geometry.height()+ 1.8*self.pushButton.frameGeometry().height())
        self.lineEdit.move(geometry.width() / 2 - self.lineEdit.frameGeometry().width() / 2,
                           0.1 * geometry.height() )

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                  QtCore.QDir.currentPath())
        if fileName:
            image = QtGui.QImage(fileName)
            if image.isNull():
                QDialog.QMessageBox.information(self, "Image Viewer",
                                                "Cannot load %s." % fileName)
                return
        self.show_image(fileName)

    @QtCore.pyqtSlot()

    def on_pushButton_clicked(self):

        name = 'slika'
        url = self.lineEdit.text()
        full_name = str(name) + ".jpg"
        urllib.request.urlretrieve(url, full_name)
        self.show_image("slika.jpg")



    def show_image(self, name):
        label = QLabel(self)
        pixmap = QtGui.QPixmap(name)

        geometry = QDesktopWidget().screenGeometry()
        h = min(geometry.height() * 0.5, pixmap.height())
        pixmap2 = pixmap.scaledToHeight(h)
        w = min(geometry.width() * 0.5, pixmap2.width())
        label.setPixmap(pixmap2)
        label.resize(w, h)

        label.move(geometry.width() / 2 - w / 2, geometry.height() * 0.3)
        label.show()

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainScreen=MainScreen()
    mainScreen.show()
    mainScreen.showMaximized()
    sys.exit(app.exec_())