import abc
import dataclasses

class IFileComponent(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str: ...

    @abc.abstractmethod
    def get_size(self) -> int: ...

    @abc.abstractmethod
    def is_composite(self) -> bool: ...


@dataclasses.dataclass
class FileLeaf(IFileComponent):
    name: str
    size: int

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def is_composite(self) -> bool:
        return False


class DirectoryComposite(IFileComponent):
    def __init__(self, name: str) -> None:
        self._name = name
        self._children: list[IFileComponent] = []

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def add(self, file_component: IFileComponent) -> None:
        self._children.append(file_component)

    def remove(self, file_component: IFileComponent) -> None:
        self._children.remove(file_component)

    def get_children(self) -> list[IFileComponent]:
        return self._children

    def is_composite(self) -> bool:
        return True


def traverse(file_component: IFileComponent) -> None:
    if not file_component.is_composite():
        print(f'{file_component.get_name()} - {file_component.get_size()} bytes')

    else:
        print(f'{file_component.get_name()} - {file_component.get_size()} bytes')
    
        for child in file_component.get_children():
            traverse(child)

if __name__ == '__main__':
    root = DirectoryComposite('root')
    documents = DirectoryComposite('Documents')
    downloads = DirectoryComposite('Downloads')
    music = DirectoryComposite('Music')
    pictures = DirectoryComposite('Pictures')
    videos = DirectoryComposite('Videos')

    root.add(documents)
    root.add(downloads)
    root.add(music)
    root.add(pictures)
    root.add(videos)

    resume = FileLeaf('resume.pdf', 1000)
    documents.add(resume)

    song1 = FileLeaf('song1.mp3', 5000)
    song2 = FileLeaf('song2.mp3', 7000)
    music.add(song1)
    music.add(song2)

    traverse(root)
