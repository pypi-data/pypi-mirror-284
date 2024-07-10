from stcube.core import *
from stcube._pyqt_pack import *

class Module(Functional):
    key = 'm|mod'
    doc = """
    Modules management.
        - Module is made from some .c/cpp .h/hpp files.
        - Import module will copy file and write the main.h
    .new: Create a new module from current project directory.
    .exp: Open the module directory in the explorer.
    """
    doc_zh = """
    模块管理模块, 展示当前的模块列表.
        - 模块是由一些.c/cpp .h/hpp文件创建的。
        - 导入模块会复制文件并写入main.h
    .new: 从当前项目目录创建新模块。
    .exp: 在资源管理器中打开模块目录。
    """
    sys = Functional.sys + ['mods']
