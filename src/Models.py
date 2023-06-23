from PySide6.QtCore import Qt, QObject, Slot, Property
from PySide6.QtCore import QAbstractListModel, QModelIndex, QByteArray

import EbayApiWrapper

class EbayItem:
    def __init__(self, data):
        self.id = data.itemId
        self.category = data.primaryCategory.categoryName
        self.title = data.title
        self.iconUrl = data.galleryURL
        self.price = data.sellingStatus.currentPrice.value
        self.currency = data.sellingStatus.currentPrice._currencyId

class EbayItemsModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    CategoryRole = Qt.UserRole + 2
    TitleRole = Qt.UserRole + 3
    IconUrlRole = Qt.UserRole + 4
    PriceRole = Qt.UserRole + 5
    CurrencyRole = Qt.UserRole + 6

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.db)

    def roleNames(self):
        default = super().roleNames()
        default[self.IdRole] = QByteArray(b"idRole")
        default[self.CategoryRole] = QByteArray(b"categoryRole")
        default[self.TitleRole] = QByteArray(b"titleRole")
        default[self.IconUrlRole] = QByteArray(b"iconUrlRole")
        default[self.PriceRole] = QByteArray(b"priceRole")
        default[self.CurrencyRole] = QByteArray(b"currencyRole")
        return default

    def data(self, index, role: int):
        if not self.db:
            return None

        if not index.isValid():
            return None

        item = self.db[index.row()]
        if role == self.IdRole:
            ret = item.id
        elif role == self.CategoryRole:
            ret = item.category
        elif role == self.TitleRole:
            ret = item.title
        elif role == self.IconUrlRole:
            ret = item.iconUrl
        elif role == self.PriceRole:
            ret = item.price
        elif role == self.CurrencyRole:
            ret = item.currency
        else:
            ret = None
        return ret

    def resetModel(self, data):
        self.beginResetModel()
        self.db.clear()
        for itemData in data.item:
            self.db.append(EbayItem(itemData))
        self.endResetModel()


class CoreModel(QObject):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__itemsModel = EbayItemsModel()

    @Slot(str)
    def searchItems(self, text):
        result = EbayApiWrapper.searchItems(text)
        self.__itemsModel.resetModel(result)

    @Property(QObject)
    def itemsModel(self):
        return self.__itemsModel
