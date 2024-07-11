"""
Copyright (c) 2024 Leonov Artur (depish.eskry@yandex.ru)

Permission is hereby granted to use, copy, modify, and distribute this code in any form, provided that the above copyright notice and this permission notice appear in all copies.

DISCLAIMER:
This source code is provided "as is", without any warranty of any kind, express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the code is with you.



Copyright (c) 2024 Леонов Артур (depish.eskry@yandex.ru)

Разрешается использовать, копировать, изменять и распространять этот код в любом виде, при условии сохранения данного уведомления.

ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ:
Этот исходный код предоставляется "как есть" без каких-либо гарантий, явных или подразумеваемых, включая, но не ограничиваясь, подразумеваемыми гарантиями товарной пригодности и пригодности для конкретной цели. Вся ответственность за использование данного кода лежит на вас.
"""


from exechain.base import BaseTool
from exechain.internal import _get_path, JnString

import shutil
from pathlib import Path
import os
from jinja2 import Template


class Copy(BaseTool):
    def __init__(self, src, dst) -> None:
        super().__init__()
        self.src: JnString = JnString(src)
        self.dst: JnString = JnString(dst)


    def _invoke(self, vars: dict = {}):
        src = self.src.precessed_string(vars)
        dst = self.dst.precessed_string(vars)
        
        _src = _get_path(src)

        if not _src.exists():
            raise FileNotFoundError(f"not found {src}")
        
        print(f"copy [src: {src} dst: {dst}]")
        if _src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy(src, dst)

        return True


class Makedirs(BaseTool):
    def __init__(self, dir) -> None:
        super().__init__()
        self.dir: JnString = JnString(dir)


    def _invoke(self, vars: dict = {}):
        dir = _get_path(self.dir.precessed_string(vars))
        dir.mkdir(parents=True, exist_ok=True)
        return True


class Touch(BaseTool):
    def __init__(self, file) -> None:
        super().__init__()
        self.file: JnString = JnString(file)


    def _invoke(self, vars: dict = {}):
        file = _get_path(self.file.precessed_string(vars))
        file.touch(exist_ok=True)
        return True


class WriteFile(BaseTool):
    def __init__(self, file, content, mode="w") -> None:
        super().__init__()
        self.file: JnString = JnString(file)
        self.content: JnString = JnString(content)
        self.mode: JnString = JnString(mode)
    
    
    def _invoke(self, vars: dict = {}):
        file = self.file.precessed_string(vars)
        content = self.content.precessed_string(vars)
        mode = self.mode.precessed_string(vars)
        
        print(f"write [file: {file}]")
        with open(file, mode) as f:
            f.write(content)
            
        return True


class Remove(BaseTool):
    def __init__(self, file_or_dir) -> None:
        super().__init__()
        self.file_of_dir: JnString = JnString(file_or_dir)


    def _invoke(self, vars: dict = {}):
        path = _get_path(self.file_of_dir.precessed_string(vars))
        
        print(f"remove [{path}]")
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                os.remove(path)
        return True
        
    def __str__(self) -> str:
        return f"remove {self.file_of_dir}"


class Chmod(BaseTool):
    def __init__(self, path: Path, mode) -> None:
        super().__init__()
        self.target: JnString = JnString(path)
        self.mode: JnString = JnString(mode)
    

    def _invoke(self, vars: dict = {}):
        target = _get_path(self.target.precessed_string(vars))
        mode = self.mode.precessed_string(vars)
        
        print(f"chmod  [{target} mode: {mode}]")
        target.chmod(mode)
        return True
        
    