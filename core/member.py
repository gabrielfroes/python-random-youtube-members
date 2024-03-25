from dataclasses import dataclass


@dataclass
class Member:
    name: str
    profile_url: str
    photo_url: str
    membership_level: str
    total_time_in_level: float
    total_time_as_member: float
    last_update: str
    last_update_timestamp: str
    badge_image: str
    photo_ascii: str = None

    def __repr__(self):
        return f"Member(name={self.name}, profile_url={self.profile_url}, " \
               f"photo_url={self.photo_url}, membership_level={self.membership_level}, " \
               f"total_time_in_level={self.total_time_in_level}, " \
               f"total_time_as_member={self.total_time_as_member}, " \
               f"last_update={self.last_update}, " \
               f"last_update_timestamp={self.last_update_timestamp}, " \
               f"badge_image={self.badge_image}, " \
               f"photo_ascii={self.photo_ascii})"
