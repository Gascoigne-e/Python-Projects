import os
import shutil
import time


download_fdr = r"C:\Users\Username\Downloads"

destination_fdr = {
    'images': r"C:\Users\Username\Pictures\Saved Pictures",
    'installers': r"C:\Users\Username\Downloads\Software installers",
    'pdfs': r"C:\Users\Username\Documents\PDFs",
    'videos': r"C:\Users\Username\Videos",
    'MS office': r"C:\Users\Username\Documents\Office",
    'others': r"C:\Users\Username\Downloads\Others",
    'Compressed': r"C:\Users\Username\Downloads\Compressed"
}


file_type = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'installers': ['.exe', '.dmg', '.apk', '.msi', '.sh'],
    'pdfs': ['.pdf'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'MS office': ['.doc', '.docx', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz']
}
def move_file(sou, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    shutil.move(sou, dest)
    print(f"Moved: {sou} -> {dest}")


def move_files():
    for filename in os.listdir(download_fdr):
        file_path = os.path.join(download_fdr, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            moved = False
            for file_types, extensions in file_type.items():
                if file_extension in extensions:
                    destination_dir = destination_fdr[file_types]
                    move_file(file_path, destination_dir)
                    moved = True
                    break

            if not moved:
                move_file(file_path, destination_fdr['others'])


if __name__ == "__main__":
    while True:
        move_files()
        time.sleep(30)


