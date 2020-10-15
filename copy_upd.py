import os
import shutil
import datetime
import typing as tp

def modification_date(filename: str) -> datetime:
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def copy_file(dir_from: str, dir_to: str, file_type: str) -> None:
    files = os.listdir(dir_from)
    for cur_file in files:
        if cur_file.endswith('.' + file_type) is True:
            if (os.path.exists(dir_to + '/' + cur_file) is False or
                    modification_date(dir_to + '/' + cur_file) != modification_date(dir_from + '/' + cur_file)):
                if os.path.exists(dir_to + '/' + cur_file):
                    os.remove(dir_to + '/' + cur_file)
                print('Copy file ' + dir_from + '/' + cur_file + ' last update: ' + modification_date(dir_from + '/' + cur_file).ctime())
                if os.path.exists(dir_to + '/' + cur_file) is True:
                    print(modification_date(dir_to + '/' + cur_file))
                print(modification_date(dir_from + '/' + cur_file))
                shutil.copy2(dir_from + '/' + cur_file, dir_to + '/' + cur_file)


def copy_from_full(dir: str) -> None:
    dir_from = dir + '/full'
    dir_to_pdf = dir + '/pdf'
    dir_to_tex = dir + '/tex'
    copy_file(dir_from, dir_to_pdf, 'pdf')
    copy_file(dir_from, dir_to_tex, 'tex')


def get_all_correct_directories(dir0: str) -> tp.List[str]:
    list_lessons = os.listdir(dir0)
    correct_directories: tp.List[str] = []
    for lesson in list_lessons:
        lesson = dir0 + '/' + lesson
        if os.path.isdir(lesson):
            dirs_in_lesson = { dir_in_lesson for dir_in_lesson in os.listdir(lesson) if os.path.isdir(lesson + '/' + dir_in_lesson) }
            if 'full' in dirs_in_lesson and 'tex' in dirs_in_lesson and 'pdf' in dirs_in_lesson:
                correct_directories.append(lesson)
    return correct_directories


correct_directories = get_all_correct_directories('Z://study_in_hse') + get_all_correct_directories('Z://study_in_shad')
for dir in correct_directories:
    copy_from_full(dir)