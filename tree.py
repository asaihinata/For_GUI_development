from glob import glob
from pathlib import Path, PosixPath, WindowsPath
from pathspec import PathSpec

TypePath = Path | WindowsPath | PosixPath


class Treetxt:
    def __init__(self, path, save, skip=None, gitignore=None):
        self.folder = 0
        self.file = 0
        if isinstance(path, TypePath):
            path = self._pathlist(path)
        if isinstance(save, TypePath):
            save = self._pathlist(save)
        if isinstance(skip, str):
            self.skiplist = [skip]
        elif isinstance(skip, list | tuple | TypePath):
            self.skiplist = self._pathlist(skip)
        else:
            self.skiplist = None

        self.root_path = Path(path)
        self.gitignore_spec = self._load_gitignore(gitignore)

        self.txt = ""
        self.tree(path=path, root=str(Path(path).parent))
        self.txt = f"{self.txt}ファイル数:{self.file}\nフォルダ数:{self.folder}"
        with open(save, "w", encoding="utf-8") as f:
            f.write(self.txt)

    def _load_gitignore(self, gitignore):
        if gitignore is None:
            gitignore_path = self.root_path / ".gitignore"
        else:
            gitignore_path = Path(gitignore)

        if not gitignore_path.is_file():
            return None

        with open(gitignore_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        return PathSpec.from_lines("gitwildmatch", lines)

    def _is_gitignored(self, p: str) -> bool:
        if self.gitignore_spec is None:
            return False

        try:
            rel = Path(p).resolve().relative_to(self.root_path.resolve())
        except ValueError:
            return False

        rel_str = rel.as_posix()
        if Path(p).is_dir():
            return self.gitignore_spec.match_file(rel_str + "/")
        return self.gitignore_spec.match_file(rel_str)

    def _pathlist(self, path):
        def types(path):
            if isinstance(path, TypePath):
                return True
            else:
                return False

        if types(path):
            return str(path)
        elif isinstance(path, str):
            return path
        elif isinstance(path, list | tuple):
            return [str(i) if types(i) else i for i in path]

    def tree(
        self, path="", layer=0, is_last=False, indent_current=" ", root="", skip=None
    ):
        def replaces(path: str):
            return Path(path).name

        if skip is not None:
            effective_skip = skip
        else:
            effective_skip = self.skiplist
        current = replaces(path.split("/")[::-1][0])
        if layer == 0:
            self.txt += f"{current}\n"
        else:
            self.txt += f"{indent_current}{'└── ' if is_last else '├── '}{current}\n"
        paths = [
            p
            for p in sorted(glob(path + "/*"))
            if Path(p).is_dir() or Path(p).is_file()
        ]
        ps = [
            p
            for p in sorted(glob(path + "/.*"))
            if Path(p).is_dir() or Path(p).is_file()
        ]
        if ps != []:
            for i in ps:
                paths.append(i)
        filtered_paths = [
            p
            for p in paths
            if (effective_skip is None or Path(p).name not in effective_skip)
            and not self._is_gitignored(p)
        ]
        for i, p in enumerate(filtered_paths):
            lens = i == len(filtered_paths) - 1
            indent_lower = indent_current
            if layer != 0:
                if is_last:
                    indent_lower += "    "
                else:
                    indent_lower += "│   "
            if Path(p).is_dir():
                self.folder = self.folder + 1
                self.tree(
                    p,
                    layer=layer + 1,
                    is_last=lens,
                    indent_current=indent_lower,
                    root=root,
                    skip=effective_skip,
                )
            else:
                self.file = self.file + 1
                self.txt += f"{indent_lower}{'└── ' if lens else '├── '}{replaces(p.split('/')[::-1][0])}\n"

if __name__=="__main__":
    from skip import skiplist
    paths = Path(__file__).parent
    Treetxt(path=paths, save=paths / "tree.txt", skip=skiplist)
