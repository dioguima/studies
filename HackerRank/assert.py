import sys
import glob
import subprocess

if __name__ == "__main__":
    folder_path = sys.argv[1]

    in_file_paths = glob.glob(f'{folder_path}/*.in')
    expected_file_paths = glob.glob(f'{folder_path}/*.expected')
    
    
    for i in range(len(in_file_paths)):
        execution_subprocess_result = subprocess.run(f'powershell.exe cat {in_file_paths[i]} | python {folder_path}/solution.py', shell=True, capture_output=True)
        expected_read_subprocess_result = subprocess.run(f'powershell.exe cat {expected_file_paths[i]}', shell=True, capture_output=True)

        result_execution = execution_subprocess_result.stdout[:-4]
        expected_result = expected_read_subprocess_result.stdout[:-2]

        if expected_result == result_execution:
            print(f'Test case passed ({in_file_paths[i]})')
        else:
            print(f'ERROR\n\nResult of file {in_file_paths[i]} was:')
            print(f'\n\n{result_execution}\n\nExpected was:\n\n{expected_result}\n\n')
