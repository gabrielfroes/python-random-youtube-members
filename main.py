from core import youtube_membership as youtube


def main():
    # Load CSV file
    file_path = 'data/members_sample.csv'
    members = youtube.get_members_from_csv(file_path)

    # Pick a random member
    member = youtube.pick_random_member(members)
    member = youtube.get_member(member)
    print(f"{member['photo_ascii']}")
    print(f"Foto: {member['photo_url']}")
    print(f"===================================================")
    print(f"Canal: {member['name']} - {member['profile_url']}")
    print(f"Nível: {member['membership_level']}")
    print(f"Tempo Assinatura: {member['total_time_as_member']} meses")
    print(f"Atualização: {member['last_update']}")
    print(f"Badge: {member['badge_image']}")
    print(f"===================================================")


if __name__ == "__main__":
    main()
