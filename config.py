import logging
import csv
import os
import sys
import importlib
import unittest
from pathlib import Path
from distutils.dir_util import copy_tree

# Globals
current_student = None

# Consts
STR_STUDENT_SOLUTIONS_FOLDER = 'solutions'
STR_TESTS_FOLDER = 'tests'
STR_HW_PREFIX = 'hw_'
STR_BACKUP_SUFFIX = '_backup'
STR_PARTICIPANTS_CSV = 'participants.csv'
STR_CURRENT_USER_SURNAME = 'current_user'

# Logging
logger = logging.getLogger('logger')
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(asctime)s - %(filename)15s:%(lineno)5s - %(funcName)20s() - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)
logger.setLevel(logging.INFO)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

def get_students_with_solution(hw_id):
    # if we want to import only the class method
    return Student.get_students_with_solution(hw_id)

class Student():

    _participants = [] # use Student.get_participants()

    @classmethod
    def map_participant_to_folder(cls, folder_name):
        '''
        Folders with student solution are assumed to be named as "Glushko Pavlo_606574_assignsubmission_file_",
        i.e., Surname Name_[some other staff separated by underscore "_"]. Some other staff is optional.
        This naming corresponds to the format of the downloaded solutions from Moodle.

        :param hw_id: # TODO: finish
        :return: student object from participants list that suits folder_name by surname name.
        '''
        full_name = folder_name.split('_', 1)[0]
        for student in cls.get_participants():
            if full_name == student.get_full_name():
                return student

    @classmethod
    def get_students_with_solution(cls, hw_id):
        students_list = []
        if Path(STR_PARTICIPANTS_CSV).exists():
            file_path = Path(os.path.dirname(__file__))
            hw_path = file_path / (f'{STR_HW_PREFIX}{hw_id}')
            solutions_path = hw_path / (f'{STR_STUDENT_SOLUTIONS_FOLDER}')
            student_solution_folders = [f for f in os.scandir(str(solutions_path)) if f.is_dir()]
            for folder in student_solution_folders:
                if STR_BACKUP_SUFFIX in folder.name:  # do nothing with backup
                    continue
                student = cls.map_participant_to_folder(folder.name)
                if student is None:
                    logger.warning(
                        f'Could not map the {folder.name} folder to any of the students from the participants list according to the name and surname.')
                else:
                    students_list.append(student)
        else: # current user with all solution files in solutions folder
            student = Student(None, STR_CURRENT_USER_SURNAME, None)
            students_list.append(student)
        return students_list

    @classmethod
    def get_participants(cls):
        if not cls._participants:
            cls._populate_participants_list()
        return cls._participants

    @classmethod
    def _populate_participants_list(cls):
        csv_file = Path(STR_PARTICIPANTS_CSV)
        if csv_file.exists():
            with csv_file.open('r', encoding='utf8') as file:
                csv_contents = csv.DictReader(file)
                for record in csv_contents:
                    # First name column name in csv has weird characters in Moodle
                    cls._participants.append(
                        Student(record['\ufeff"First name"'], record['Surname'], record['Email address']))
            logger.debug(f"Read these participants from {csv_file}: {cls._participants}")
        else: # student user
            raise FileNotFoundError(
                f'Participants list not found: download participants list from Moodle, rename it to {STR_PARTICIPANTS_CSV} and put to the root folder')

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.solution_modules = {}

    def test(self, hw_id):
        global current_student
        print(f'*** STARTING TESTS FOR {self.surname} ***')
        file_path = Path(os.path.dirname(__file__))
        hw_path = file_path/(f'{STR_HW_PREFIX}{hw_id}')
        loader = unittest.TestLoader()
        suite = loader.discover(hw_path)  # for every student since tests are deleted from suit after run
        runner = unittest.TextTestRunner(verbosity=2)
        current_student = self
        runner.run(suite)
        self.unload_solutions()

    def backup_solution(self, hw_id):
        solution_path = self.get_solution_folder(hw_id)
        if solution_path is None:
            logger.warning(f'Solution folder for {self} not found.')
            return
        backup_folder = f'{self.get_full_name()}{STR_BACKUP_SUFFIX}'
        target_directory = solution_path.parent / backup_folder
        if not target_directory.exists():
            copy_tree(str(solution_path), str(target_directory))
            logger.debug(f'Backed up student {self} solution to {target_directory}')

    def get_solution_folder(self, hw_id):
        file_path = Path(os.path.dirname(__file__))
        hw_path = file_path/(f'{STR_HW_PREFIX}{hw_id}')
        solutions_path = hw_path / (f'{STR_STUDENT_SOLUTIONS_FOLDER}')
        if self.surname == STR_CURRENT_USER_SURNAME: # we do not need subfolders for every student
            return solutions_path
        student_solution_folders = [f for f in os.scandir(str(solutions_path)) if f.is_dir()]
        for folder in student_solution_folders:
            if self == self.map_participant_to_folder(folder.name):
                return Path(folder)

    def import_solution(self, hw_id, script_filename):
        solution_mdl = self.solution_modules.get(script_filename, None)
        if solution_mdl: # do not reimport if the module was already imported
            return solution_mdl
        sys.path.insert(0, str(self.get_solution_folder(hw_id)))
        if script_filename in sys.modules:  # we want to reload module
            del sys.modules[script_filename]
        try:
            solution_mdl = importlib.import_module(script_filename)
        except:
            raise FileNotFoundError(f"{script_filename}.py file not found in the student solution folder: {self.get_solution_folder(hw_id)}.")
        finally:
            del sys.path[0]  # delete path from the system path to avoid module conflicts
        self.solution_modules[script_filename] = solution_mdl
        return solution_mdl

    def unload_solutions(self):
        for module_name in self.solution_modules:
            if module_name in sys.modules:
                del sys.modules[module_name]
        self.solution_modules = {}

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def __repr__(self):
        return f'{self.surname} {self.name}'