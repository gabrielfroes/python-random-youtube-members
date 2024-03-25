from unittest import TestCase
from unittest.mock import patch, call

from core.member import Member
from main import main


def ppatch(obj, *args, **kwargs):
    prefix = 'main'
    return patch(f"{prefix}.{obj}", *args, **kwargs)


class TestMain(TestCase):
    @ppatch('print')
    def test_show_results(self, mock_print):
        from main import _show_results
        member = Member(
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

        _show_results(member)

        separator = '==================================================='

        mock_print.assert_has_calls([
            call(f"{member.photo_ascii}"),
            call(f"Foto: {member.photo_url}"),
            call(separator),
            call(f"Canal: {member.name} - {member.profile_url}"),
            call(f"Nível: {member.membership_level}"),
            call(f"Tempo Assinatura: {member.total_time_as_member} meses"),
            call(f"Atualização: {member.last_update}"),
            call(f"Badge: {member.badge_image}"),
            call(separator)
        ])

    @ppatch('youtube')
    @ppatch('_show_results')
    def test_main(self, mock_show_results, mock_youtube):
        main()

        mock_youtube.get_members_from_csv.assert_called_once_with(
            'data/members_sample.csv')
        mock_members = mock_youtube.get_members_from_csv.return_value

        mock_members.pick_random.assert_called_once_with()
        mock_member = mock_members.pick_random.return_value

        mock_youtube.get_extra_info.assert_called_once_with(
            mock_member.profile_url)
        mock_extra_info = mock_youtube.get_extra_info.return_value

        mock_member.enrich.assert_called_once_with(mock_extra_info)
        mock_show_results.assert_called_once_with(mock_member)
