import config # for global vars
from config import get_students_with_solution, logger
from pathlib import Path

# TODO: students for me and Achim, how to share

def main():
   hw_id = input("Which home assignment do you want to test? Enter the number: ")

   hw_path = Path(f'{config.STR_HW_PREFIX}{hw_id}')
   if not hw_path.is_dir():
      logger.error(f"Cannot find {hw_path} folder.")
      return

   test_path = hw_path / config.STR_TESTS_FOLDER
   if not test_path.is_dir():
      logger.error(f"Cannot find {test_path} folder.")
      return

   students_with_solution = get_students_with_solution(hw_id)
   for student in students_with_solution:
      if student.surname == config.STR_CURRENT_USER_SURNAME: # teacher is proofing
         student.test(hw_id)
      else:
         answer = input(f"Press any button to start testing the solution of {student} or <exit>: ")
         if not answer == 'exit':
            student.backup_solution(hw_id)
            student.test(hw_id)

if __name__ == '__main__':
   main()