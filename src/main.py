import sys
from pathlib import Path

from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QIcon

from Models import CoreModel 

if __name__ == '__main__':
    currentDir = Path(__file__).parent

    app = QGuiApplication(sys.argv)
    app.setApplicationDisplayName("eBay client")

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    coreModel = CoreModel()
    view.rootContext().setContextProperty("coreModel", coreModel)
    view.setSource(QUrl.fromLocalFile(currentDir / "qml/MainWindow.qml".__str__()))

    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()

    app.exec()
    del view