import os
def run_cleanup():
    folders = ['./resources/image_and_audio/', './resources/screenshots/', './resources/voiceovers/']
    for folder in folders:
        for file_or_dir in os.listdir(folder):
            file_or_dir_path = os.path.join(folder, file_or_dir)
            if not file_or_dir.endswith('.gitkeep'):
                remove_directory(file_or_dir_path)

def remove_directory(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)
