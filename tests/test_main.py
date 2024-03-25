from unittest import TestCase
from unittest.mock import patch, call


def ppatch(obj, *args, **kwargs):
    prefix = 'main'
    return patch(f"{prefix}.{obj}", *args, **kwargs)


class TestMain(TestCase):
    @ppatch('print')
    def test_show_results(self, mock_print):
        from main import _show_results
        member = {
            'photo_ascii': 'photo_ascii',
            'photo_url': 'photo_url',
            'name': 'name',
            'profile_url': 'profile_url',
            'membership_level': 'membership_level',
            'total_time_as_member': 'total_time_as_member',
            'last_update': 'last_update',
            'badge_image': 'badge_image'
        }

        _show_results(member)

        separator = '==================================================='

        mock_print.assert_has_calls([
            call(f"{member['photo_ascii']}"),
            call(f"Foto: {member['photo_url']}"),
            call(separator),
            call(f"Canal: {member['name']} - {member['profile_url']}"),
            call(f"Nível: {member['membership_level']}"),
            call(f"Tempo Assinatura: {member['total_time_as_member']} meses"),
            call(f"Atualização: {member['last_update']}"),
            call(f"Badge: {member['badge_image']}"),
            call(separator)
        ])
