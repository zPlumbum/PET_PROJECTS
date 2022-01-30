import subprocess


def extract_wifi_password():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8', 'replace').split('\n')
    # print(profiles_data)
    profiles = [item.split(':')[1].strip() for item in profiles_data if 'All User Profile' in item]
    # print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear')\
            .decode('utf-8', 'replace').split('\n')

        try:
            password = [profile.split(':')[1].strip() for profile in profile_info if 'Key Content' in profile][0]
        except IndexError:
            password = None

        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f"Profile: {profile}\nPassword: {password}\n{'-' * 20}\n")


def main():
    extract_wifi_password()


if __name__ == '__main__':
    main()
