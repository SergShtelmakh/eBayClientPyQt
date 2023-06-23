import QtQuick 2.12
import QtQuick.Layouts 1.15

Rectangle {
	id: root

	property string itemId
	property string itemCategory
	property string itemName
	property alias itemIconUrl: icon.source
	property string itemPrice
	property string itemCurrency

	QtObject {
		id: internal
		readonly property size iconSize: Qt.size(150, 150)
	}

	gradient: Gradient {
		GradientStop { position: 0.0; color: "#eeeeee" }
		GradientStop { position: 1.0; color: "#dddddd" }
	}

	RowLayout {
		anchors.fill: parent
		anchors.margins: 2

		Image {
			id: icon

			Layout.preferredWidth: internal.iconSize.width
			Layout.preferredHeight: internal.iconSize.height
			fillMode: Image.PreserveAspectFit
			clip: true
		}

		Text {
			id: description

			Layout.preferredHeight: 100
			Layout.preferredWidth: 220
			wrapMode: Text.WordWrap
			textFormat: Text.RichText
			text: "<b>#" + itemId + "</b><br>
			<b>" + itemCategory + "</b><br>
			<i>" + itemName + "</i>
			<br>" + itemPrice + " " + itemCurrency
		}
	}
}
