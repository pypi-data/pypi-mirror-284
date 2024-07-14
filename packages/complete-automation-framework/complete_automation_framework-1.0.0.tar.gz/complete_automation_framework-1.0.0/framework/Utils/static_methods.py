import os
import allure
from allure_commons.types import LinkType
from Framework.Utils.create_general_directory import RESULTS_DIR


def get_test_result_folder_name():
    folder_name = os.environ.get('PYTEST_CURRENT_TEST').replace('::', '-').replace('/', '-').replace(" ",
                                                                                                     "-").replace(
        '[', '-').replace(']', '').replace('_', '-').replace('.', '-').replace("-(call)", "").replace("-(setup)",
                                                                                                      "").lower()
    return folder_name


def get_test_output_dir():
    return os.path.join(os.path.join(f"{RESULTS_DIR}\\Test_Results\\", get_test_result_folder_name()))


def write_file(directory, name_with_extension, content):
    folder_path = directory
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = name_with_extension
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as f:
        f.write(content)


def attach_artifact_folder_link_to_allure():
    write_file(get_test_output_dir(), "execution.bat", f"playwright show-trace trace.zip\nexit")
    write_file(RESULTS_DIR, "allure_single_file.bat", "allure generate --single-file Allure_Results\nexit")
    write_file(RESULTS_DIR, "allure_serve.bat", "allure serve Allure_Results")
    allure.dynamic.link(url=get_test_output_dir(), link_type=LinkType.TEST_CASE,
                        name=get_test_output_dir())


def get_file_location(filename, file_extension=""):
    current_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # print(f"Searching for file: {filename} with extension: {file_extension} in directory: {current_dir}")

    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file_extension == "" or file.endswith(file_extension):
                if file == filename:
                    file_location = os.path.join(root, file)
                    # print(f"Found file at location: {file_location}")
                    return file_location

    # print(f"File not found: {filename} with extension: {file_extension}")
    return None
