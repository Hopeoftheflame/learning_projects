import os
import platform
import subprocess

import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-------------------------------')
    print('          CAT FACTORY          ')
    print('-------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    print("BF: " + base_folder)
    full_path = os.path.join(base_folder, folder)
    print("FP: " + full_path)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats....')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat' + name)
        cat_service.get_cat(folder, name)
    print("done.")


def display_cats(folder):
    print('"'+folder+'"')
    print('Displaying cats in OS Window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])

    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])

        # below shows that explorer can open the path if it is correct
        # but we don't hard code such things if we can avoid them
        #subprocess.call(['explorer', "C:\\Users\\epalmer\\PycharmProjects\\jp_10\\learning_projects\\cat_pictures"])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])

    else:
        print("We don't support you os: " + platform.system())


if __name__ == '__main__':
    main()
