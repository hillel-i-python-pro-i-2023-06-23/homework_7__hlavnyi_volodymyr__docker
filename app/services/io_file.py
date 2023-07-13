from app.config import FILES_INPUT_DIR


def check_file_exists():
    gitkeep_file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    return gitkeep_file_path.exists()


def get_path_if_file_exists(name_of_file: str):
    check_txt_file = FILES_INPUT_DIR.joinpath(name_of_file)
    if check_file_exists():
        return check_txt_file
    else:
        raise FileNotFoundError(f"File not found: {check_txt_file.as_uri()}")


def print_file_to_screen(link_2_file):
    with open(link_2_file) as f:
        print(f.read())
