"""
mkdir -> /a should create director a. /a/b should only create b if /a exists. If a and b don't exist it needs to error out
write_file -> If intermittent directories are absent then throw error
readfile -> This is the usual one.

Trie
---
Node(
    Directories: Dict = {dir_path: Node, ...}
    Files: Dict = {file_name: Content, ...}
)
"""


class Node:
    def __init__(self):
        self.directories: dict[str, Node] = {}
        self.files = {}


class FileSystem:
    def __init__(self):
        self.root = Node()

    def make_dir(self, dir_path: str):
        """
        :param dir_path: /a/b
        :return:
        """
        paths = self._split_path(dir_path)
        node: Node = self._get_node(paths[:-1])
        node.directories[paths[-1]] = Node()

    def write_file(self, file_path: str, content: object):
        """
        :param file_path: /a/b/c.py
        :param content: {a: 1, b: 2}
        :return:
        """
        paths = self._split_path(file_path)
        file_name = paths[-1]
        dir_paths = paths[:-1]
        node = self._get_node(dir_paths)
        node.files[file_name] = content

    def read_file(self, file_path: str):
        paths = self._split_path(file_path)
        file_name = paths[-1]
        dir_paths = paths[:-1]
        node = self._get_node(dir_paths)
        return node.files[file_name]

    def _split_path(self, dir_path):
        return [v for v in dir_path.split('/') if len(v)]

    def _get_node(self, paths) -> Node:
        node = self.root
        for i in range(len(paths)):
            if paths[i] in node.directories:
                node = node.directories[paths[i]]
            else:
                raise ValueError(f"directory path {'/'.join(paths)} not exists!")
        return node


class TestFS:
    def __init__(self):
        pass

    def test_make_dir(self):
        fs = FileSystem()
        fs.make_dir("/a")
        if 'a' not in fs.root.directories:
            raise Exception("test make dir failed")

        try:
            fs.make_dir('/a/b/c')
        except Exception as e:
            print(e)

    def test_read_write_file(self):
        fs = FileSystem()
        fs.make_dir("/a")

        obj = {'a': 1, 'b': 2}
        file_path = '/a/test.py'
        fs.write_file(file_path, obj)
        got = fs.read_file(file_path)

        assert obj == got


if __name__ == '__main__':
    tfs = TestFS()
    tfs.test_make_dir()
    tfs.test_read_write_file()

# With file creation

# class Trie:
#     def __init__(self):
#         self.root = Node()
#
#     def ls(self, path: str):
#         full_paths = self._split_path(path)
#         dir_paths, last_item = full_paths[:-1], full_paths[-1]
#         node = self.root
#         for p in dir_paths:
#             node = node.directories[p]
#         if last_item in node.directories:
#             node = node.directories[last_item]
#             return self._get_dir_items(node)
#         else:
#             return [last_item]
#
#     def make_dir(self, path: str):
#         paths = self._split_path(path)
#         node: Node = self.root
#         for p in paths:
#             if p not in node.directories:
#                 node.directories[p] = Node()
#             node = node.directories[p]
#
#     def add_content_to_file(self, file_path: str, content: str):
#         full_paths = self._split_path(file_path)
#         dir_paths, file_name = full_paths[:-1], full_paths[-1]
#         node: Node = self.root
#         for p in dir_paths:
#             if p not in node.directories:
#                 node.directories[p] = Node()
#             node = node.directories[p]
#         if file_name not in node.files:
#             node.files[file_name] = ""
#         node.files[file_name] += content
#
#     def read_content_from_file(self, file_path: str):
#         full_paths = self._split_path(file_path)
#         dir_paths, file_name = full_paths[:-1], full_paths[-1]
#         node: Node = self.root
#         for p in dir_paths:
#             node = node.directories[p]
#         return node.files[file_name]
#
#     def _split_path(self, path):
#         return [x for x in path.split('/') if len(x)]
#
#     def _get_dir_items(self, node: Node):
#         items = list(node.directories.keys()) + list(node.files.keys())
#         items.sort()
#         return items
#
#     def _get_file_node(self, file_path):
#         pass
#
#
# a = "/a/b/c"
#
# print(a.split('/'))
