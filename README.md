# Content

- 作业描述
- 成果展示

# 作业：实现Sudoku类

按照自己喜好，分别用两种语言，一种静态类型（C++、Java、……），一种动态类型（Python、JavaScript、……），按设计实现Sundoku模块（业务代码、测试代码、文档）。

## 要求
### 业务功能

Input：017903600000080000900000507072010430000402070064370250701000065000030000005601720 

更多测例，可从 https://www.sudokuwiki.org/ 获取

解析字符串输入，得到Sudoku实例

推理棋盘，得到各单元格候选值

场景下其它合理功能

### 代码质量

OO基础技术：实现的Sudoku类应当符合所用语言OOP的技术惯例，包括必要的基础技术方法，包括并不限于：对象创建、初始化、克隆、串行化、外表化、比较（序）

正确性：必要的测试代码和测试用例

可理解性：恰当的命名、合理的模块（函数）划分、必要的注释

# 成果展示

## SudokuTerminal.exe
流程：
1. 输入字符串 -> 解析输入的字符串。
2. 若解析失败，给出反馈提示。返回1
3. 若解析成功，显示九宫格矩阵数据
4. 序列化解析之后的九宫格矩阵至字符串，与输入字符串作比较，检查解析结果是否与输入字符串一致
<video src="[videos/sudoku_terminal_exe.mp4](https://github.com/liwaner653/Sudoku_Class_Implementation/blob/main/videos/sudoku_terminal_exe.mp4)"></video>

## SudokuUi.exe
使用Qt框架可视化九宫格，带解析按钮、输入框和提示按钮
<video src="videos/sudoku_ui_exe.mp4"></video>
