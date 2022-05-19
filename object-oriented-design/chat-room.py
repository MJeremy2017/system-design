from collections import defaultdict
from abc import ABC, abstractmethod
from typing import List, Dict
import uuid


class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

    def __hash__(self):
        return hash((self.user_id, self.name))

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __str__(self):
        return f"user_id: {self.user_id}|name: {self.name}"


class RelationshipDict:
    def __init__(self):
        self._s = defaultdict(set)

    def add_friend(self, user: User, friend: User):
        key = self._hash_user(user)
        self._s[key].add(friend)

    def remove_friend(self, user: User, friend: User):
        key = self._hash_user(user)
        if user in self._s:
            self._s[key].remove(friend)

    def _hash_user(self, user):
        return user.user_id + '-' + user.name

    def __str__(self):
        return str(self._s)


class FriendServer:
    def __init__(self):
        self.relationships: RelationshipDict = RelationshipDict()

    def add_friend(self, user: User, friend: User):
        self.relationships.add_friend(user, friend)

    def remove_friend(self, user: User, friend: User):
        self.remove_friend(user, friend)


class ChatRoom:
    def __init__(self, chat_id: str, users: List[User]):
        self.chat_id = chat_id
        self.users = users

    def display_message(self, user: User, content: str):
        print(user.user_id, "says:", content)


class ChatServer(ABC):
    def __init__(self):
        self.chat_id_room: Dict[str, ChatRoom] = {}

    @abstractmethod
    def send_message(self, user: User, chat_id: str, content: str):
        ...

    def get_chat_ids(self):
        return set(self.chat_id_room.keys())

    def _generate_chat_id(self):
        return str(uuid.uuid4())


class PrivateChatServer(ChatServer):
    def __init__(self):
        self.room_type = 'private'
        super().__init__()

    def send_message(self, user: User, chat_id: str, content: str):
        chat_room = self.chat_id_room[chat_id]
        chat_room.display_message(user, content)

    def create_private_chat_room(self, user: User) -> ChatRoom:
        chat_id = self._generate_chat_id()
        room = ChatRoom(chat_id, [user])
        self.chat_id_room[chat_id] = room
        return room


class GroupChatServer(ChatServer):
    def __init__(self):
        self.room_type = 'group'
        super().__init__()

    def send_message(self, user: User, chat_id: str, content: str):
        chat_room = self.chat_id_room[chat_id]
        chat_room.display_message(user, content)

    def create_group_chat_room(self, user: User) -> ChatRoom:
        chat_id = self._generate_chat_id()
        room = ChatRoom(chat_id, [user])
        self.chat_id_room[chat_id] = room
        return room


class ChatServer:
    def __init__(self, friend_server: FriendServer = None, private_chat_server: PrivateChatServer = None,
                 group_chat_server: GroupChatServer = None):
        self.friend_server = friend_server
        self.private_chat_server = private_chat_server
        self.group_chat_server = group_chat_server

    def send_message(self, user_from: User, content: str, chat_id: str):
        private_chat_ids = self.private_chat_server.get_chat_ids()
        group_chat_ids = self.group_chat_server.get_chat_ids()
        if chat_id in private_chat_ids:
            self._send_private_chat(user_from, content, chat_id)
        if chat_id in group_chat_ids:
            self._send_group_chat(user_from, content, chat_id)
        raise Exception("chat_id not exists")

    def _send_private_chat(self, user_from, content, chat_id):
        self.private_chat_server.send_message(user_from, chat_id, content)

    def _send_group_chat(self, user_from: User, content: str, chat_id: str):
        self.group_chat_server.send_message(user_from, chat_id, content)


if __name__ == '__main__':
    pc = PrivateChatServer()
    pc.create_private_chat_room(User("123", "MM"))
    cs = ChatServer(private_chat_server=pc)

