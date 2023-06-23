import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15

Page {
	id: root

	width: 1000
	height: 800

	TabBar {
		id: bar

		width: parent.width
		height: 20

		TabButton {
			text: qsTr("Search items")
		}
		TabButton {
			text: qsTr("TODO")
		}
		TabButton {
			text: qsTr("TODO")
		}
	}

	StackLayout {
		anchors {
			top: bar.bottom
			bottom: parent.bottom
			left: parent.left
			right: parent.right
		}

		currentIndex: bar.currentIndex
		clip: true

		SearchEbayItemsPage {
			model: coreModel
		}
		Item {
			id: discoverTab
		}
		Item {
			id: activityTab
		}
	}
}
