from dataclasses import dataclass
from random import choice
from typing import List


@dataclass
class ExtraInfo:
    photo_url: str
    badge_image: str
    photo_ascii: str


@dataclass
class Member:
    name: str
    profile_url: str
    membership_level: str
    total_time_in_level: float
    total_time_as_member: float
    last_update: str
    last_update_timestamp: str
    photo_url: str = None
    badge_image: str = None
    photo_ascii: str = None

    def enrich(self, extra_info: ExtraInfo):
        self.photo_url = extra_info.photo_url
        self.badge_image = extra_info.badge_image
        self.photo_ascii = extra_info.photo_ascii

    @property
    def channel(self):
        return f'{self.name} - {self.profile_url}'


class MemberList:
    def __init__(self, members: List[Member]):
        self.members = members

    def filter_by_level(self, level):
        return MemberList([member for member in self.members
                           if member.membership_level == level])

    def list_levels(self):
        return list(set(member.membership_level for member in self.members))

    def pick_random(self):
        return choice(self.members)  # noqa

    @classmethod
    def from_json(cls, members_json):
        return cls([Member(**member) for member in members_json])
