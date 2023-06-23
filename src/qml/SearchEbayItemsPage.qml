import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15

Rectangle {
	id: root

	property QtObject model : null

	gradient: Gradient {
		GradientStop { position: 0.0; color: "#eeeeee" }
		GradientStop { position: 1.0; color: "#dddddd" }
	}

	RowLayout {
		id: mainLayout

		anchors.fill: parent
		anchors.margins: 2

		ListView {
			model: root.model ? root.model.itemsModel : null

			Layout.preferredWidth: root.width / 2
			Layout.fillHeight: true

			delegate: EbayItemDelegate {
				required property string idRole
				required property string categoryRole
				required property string titleRole
				required property url iconUrlRole
				required property string priceRole
				required property string currencyRole

				width: 450
				height: 150

				itemId: idRole
				itemCategory: categoryRole
				itemName: titleRole
				itemIconUrl: iconUrlRole
				itemPrice: priceRole
				itemCurrency: currencyRole
			}
		}

		ColumnLayout {
			Label {
				Layout.preferredHeight: 20
				text: "Type your request (e.g. Car)"
			}

			Rectangle {
				Layout.preferredHeight: 20
				Layout.fillWidth: true

				color: "white"

				TextInput {
					id: inputText

					anchors.fill: parent
					selectByMouse: true
					focus: true
					text: "Car"
				}
			}

			Button {
				Layout.preferredHeight: 20

				text: "Search"

				onClicked: {
					root.model.searchItems(inputText.text);
				}
			}

			Item {
				id: placeholder
				Layout.fillHeight: true
			}
		}
	}
}
