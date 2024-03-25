from core import youtube_membership as youtube
from core.member import Member


def main():
    # Load CSV file
    file_path = 'data/members_sample.csv'
    members = youtube.get_members_from_csv(file_path)

    # Pick a random member
    member = members.pick_random()
    extra_info = youtube.get_extra_info(member.profile_url)
    member.enrich(extra_info)
    _show_results(member)


def _show_results(member: Member):
    print(f"{member.photo_ascii}")
    print(f"Foto: {member.photo_url}")
    print("===================================================")
    print(f"Canal: {member.channel}")
    print(f"Nível: {member.membership_level}")
    print(f"Tempo Assinatura: {member.total_time_as_member} meses")
    print(f"Atualização: {member.last_update}")
    print(f"Badge: {member.badge_image}")
    print("===================================================")


if __name__ == "__main__":
    main()
