from unittest import TestCase
from unittest.mock import patch, call

from core.member import Member, ExtraInfo, MemberList


def ppatch(obj, *args, **kwargs):
    prefix = 'core.member'
    return patch(f"{prefix}.{obj}", *args, **kwargs)


class TestMember(TestCase):
    @staticmethod
    def make_sut():
        return Member(
            photo_ascii='photo_ascii',
            photo_url='photo_url',
            name='name',
            profile_url='profile_url',
            membership_level='membership_level',
            total_time_as_member=42.17,
            last_update='last_update',
            badge_image='badge_image',
            last_update_timestamp='last_update_timestamp',
            total_time_in_level=17.42
        )

    def test_member(self):
        member = self.make_sut()

        assert member.photo_ascii == 'photo_ascii'
        assert member.photo_url == 'photo_url'
        assert member.name == 'name'
        assert member.profile_url == 'profile_url'
        assert member.membership_level == 'membership_level'
        assert member.total_time_as_member == 42.17
        assert member.last_update == 'last_update'
        assert member.badge_image == 'badge_image'
        assert member.last_update_timestamp == 'last_update_timestamp'
        assert member.total_time_in_level == 17.42

    def test_member_enrich(self):
        member = self.make_sut()
        extra_info = ExtraInfo(
            photo_url='photo_url',
            badge_image='badge_image',
            photo_ascii='photo_ascii'
        )

        member.enrich(extra_info)

        assert member.photo_url == 'photo_url'
        assert member.badge_image == 'badge_image'
        assert member.photo_ascii == 'photo_ascii'

    def test_member_channel(self):
        member = self.make_sut()

        assert member.channel == 'name - profile_url'


class TestMemberList(TestCase):
    def make_sut(self):
        self.member1 = Member(
            photo_ascii='photo_ascii',
            photo_url='photo_url',
            name='name',
            profile_url='profile_url',
            membership_level='membership_level',
            total_time_as_member=42.17,
            last_update='last_update',
            badge_image='badge_image',
            last_update_timestamp='last_update_timestamp',
            total_time_in_level=17.42
        )
        self.member2 = Member(
            photo_ascii='photo_ascii2',
            photo_url='photo_url2',
            name='name2',
            profile_url='profile_url2',
            membership_level='membership_level2',
            total_time_as_member=2,
            last_update='last_update2',
            badge_image='badge_image2',
            last_update_timestamp='last_update_timestamp2',
            total_time_in_level=3
        )
        return MemberList([self.member1, self.member2])

    def test_member_list(self):
        member_list = self.make_sut()

        assert member_list.members == [self.member1, self.member2]

    def test_member_list_filter_by_level(self):
        member_list = self.make_sut()

        filtered = member_list.filter_by_level('membership_level')

        assert filtered.members == [self.member1]

    def test_member_list_list_levels(self):
        member_list = self.make_sut()

        levels = member_list.list_levels()
        expected = ['membership_level', 'membership_level2']
        self.assertListEqual(sorted(levels), sorted(expected))

    @ppatch('choice')
    def test_member_list_pick_random(self, mock_choice):
        member_list = self.make_sut()

        member = member_list.pick_random()

        mock_choice.assert_called_once_with(member_list.members)

        assert member == mock_choice.return_value

    @ppatch('Member')
    def test_member_list_from_json(self, mock_member_cls):
        mock_members = [{'fake_member': '1'}, {'fake_member': '2'}]
        member_list = MemberList.from_json(mock_members)

        mock_member_cls.assert_has_calls([
            call(**mock_members[0]),
            call(**mock_members[1])])

        assert member_list.members == [mock_member_cls.return_value,
                                       mock_member_cls.return_value]
