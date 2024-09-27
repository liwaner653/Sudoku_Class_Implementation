# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.7.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x07R\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Di\
alogs\x0d\x0aimport Qt\
Quick.Window\x0d\x0aim\
port QtQuick.Con\
trols\x0d\x0aimport Qt\
Quick.Layouts\x0d\x0a\x0d\
\x0aWindow {\x0d\x0a    i\
d: window\x0d\x0a\x0d\x0a   \
 width: 640\x0d\x0a   \
 height: 600\x0d\x0a  \
  visible: true\x0d\
\x0a    title: \x22Sud\
oku\x22\x0d\x0a\x0d\x0a    sign\
al parseSignal(m\
sg: string)\x0d\x0a\x0d\x0a \
   MessageDialog\
 {\x0d\x0a        id: \
messageDialog\x0d\x0a \
       buttons: \
MessageDialog.Ok\
\x0d\x0a        visibl\
e: false\x0d\x0a    }\x0d\
\x0a\x0d\x0a    TableView\
 {\x0d\x0a        id: \
tableView\x0d\x0a     \
   anchors.fill:\
 parent\x0d\x0a       \
 model: sudoku_t\
able_model\x0d\x0a\x0d\x0a  \
      delegate: \
Rectangle {\x0d\x0a   \
         implici\
tWidth: 50\x0d\x0a    \
        implicit\
Height: 50\x0d\x0a    \
        border.w\
idth: 1\x0d\x0a\x0d\x0a     \
       Text {\x0d\x0a \
               a\
nchors.centerIn:\
 parent\x0d\x0a\x0d\x0a     \
           horiz\
ontalAlignment: \
Text.AlignHCente\
r\x0d\x0a             \
   width: 30\x0d\x0a\x0d\x0a\
                \
text: display\x0d\x0a \
               w\
rapMode: Text.Wr\
ap\x0d\x0a            \
}\x0d\x0a        }\x0d\x0a  \
  }\x0d\x0a\x0d\x0a    Butto\
n {\x0d\x0a        id:\
 parseButton\x0d\x0a  \
      text: \x22Par\
se\x22\x0d\x0a\x0d\x0a        a\
nchors {\x0d\x0a      \
      bottom: hi\
ntButton.top\x0d\x0a  \
      }\x0d\x0a\x0d\x0a     \
   onClicked: {\x0d\
\x0a            win\
dow.parseSignal(\
parse_string.tex\
t)\x0d\x0a            \
messageDialog.te\
xt = sudoku_tabl\
e_model.message\x0d\
\x0a            mes\
sageDialog.visib\
le = true\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a   \
 TextField {\x0d\x0a  \
      id: parse_\
string\x0d\x0a        \
placeholderText:\
 \x22Input string\x22\x0d\
\x0a        text: \x22\
0179036000000800\
0090000050707201\
0430000402070064\
3702507010000650\
0003000000560172\
0\x22\x0d\x0a\x0d\x0a        an\
chors {\x0d\x0a       \
     left: parse\
Button.right\x0d\x0a  \
          right:\
 parent.right\x0d\x0a \
           top: \
parseButton.top\x0d\
\x0a            bot\
tom: parseButton\
.bottom\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a\x0d\x0a   \
 Button {\x0d\x0a     \
   id: hintButto\
n\x0d\x0a\x0d\x0a        anc\
hors.bottom: par\
ent.bottom\x0d\x0a\x0d\x0a  \
      text: \x22Hin\
t\x22\x0d\x0a        onCl\
icked: {\x0d\x0a      \
      sudoku_tab\
le_model.show_hi\
nt = !sudoku_tab\
le_model.show_hi\
nt;\x0d\x0a           \
 messageDialog.t\
ext = sudoku_tab\
le_model.message\
\x0d\x0a            me\
ssageDialog.visi\
ble = true\x0d\x0a    \
    }\x0d\x0a    }\x0d\x0a\x0d\x0a\
}\
"

qt_resource_name = b"\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x921@m\x8b\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
