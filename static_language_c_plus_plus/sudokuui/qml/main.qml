import QtQuick
import QtQuick.Dialogs
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: window

    width: 640
    height: 600
    visible: true
    title: "Sudoku"

    signal parseSignal(msg: string)

    MessageDialog {
        id: messageDialog
        buttons: MessageDialog.Ok
        visible: false
    }

    TableView {
        id: tableView
        anchors.fill: parent
        model: sudoku_table_model

        delegate: Rectangle {
            implicitWidth: 50
            implicitHeight: 50
            border.width: 1
            border.color: "light gray"

            Text {
                anchors.centerIn: parent

                horizontalAlignment: Text.AlignHCenter
                width: 30

                text: display
                wrapMode: Text.Wrap
            }
        }
    }

    Button {
        id: parseButton
        text: "Parse"

        anchors {
            bottom: hintButton.top
        }

        onClicked: {
            window.parseSignal(parse_string.text)
            messageDialog.text = sudoku_table_model.message
            messageDialog.visible = true
        }
    }
    TextField {
        id: parse_string
        placeholderText: "Input string"
        text: "017903600000080000900000507072010430000402070064370250701000065000030000005601720"

        anchors {
            left: parseButton.right
            right: parent.right
            top: parseButton.top
            bottom: parseButton.bottom
        }
    }

    Button {
        id: hintButton

        anchors.bottom: parent.bottom

        text: "Hint"
        onClicked: {
            sudoku_table_model.show_hint = !sudoku_table_model.show_hint;
            messageDialog.text = sudoku_table_model.message
            messageDialog.visible = true
        }
    }

}