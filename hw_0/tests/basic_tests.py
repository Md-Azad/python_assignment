from unittest import TestCase
import importlib
import os
import sys

homework_id = 0
script_files = ['solution_hw'] # should have .py extension
other_files = [] # provide with extensions

def import_config():
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..\\..')) # relative to current file path
    if not root_path in sys.path:
        sys.path.insert(0, root_path)
    config_mdl = importlib.import_module('config')
    return config_mdl

def import_solution(script_name):
    global homework_id
    student = import_config().current_student
    return student.import_solution(homework_id, script_name)

def get_solution_folder():
    global homework_id
    student = import_config().current_student
    return student.get_solution_folder(homework_id)

def module_has(module, var_name):
    try:
        getattr(module, var_name)
    except:
        return False
    return True

class TestStructure(TestCase):

    def test_student_solution_folder_exists(self):
        self.assertTrue(get_solution_folder().is_dir())

    def test_solution_files_exist(self):
        solution_folder = get_solution_folder()
        missing_files = []
        for file_name in script_files:
            file_name += '.py'
            file = solution_folder/file_name
            if not file.is_file():
                missing_files.append(file_name)
        for file_name in other_files:
            file = solution_folder/file_name
            if not file.is_file():
                missing_files.append(file_name)
        message = f'Cannot find these solution files: {missing_files}'
        self.assertFalse(missing_files, message)

class TestExercises(TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.solution = import_solution('solution_hw')
        except:
            import_config().logger.error('solution_hw crashed or file not found.')

    def test_objects_present(self):
        missing_objs = []
        for object in ['c', 'd', 'e', 'f', 'g', 'my_sum', 'var1', 'var2', 'var3', 'second', 'first_two', 'except_last', 'last_two', 'calculation_result']:
            if not module_has(self.solution, object):
                missing_objs.append(object)
        self.assertFalse(missing_objs, f'Cannot find these variables / functions in the student solution: {missing_objs}')

