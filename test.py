import subprocess
import multiprocessing
import concurrent.futures

# Replace 'my_script.py' with the actual path to your Python script
python_script = 'main.py'

# Specify the parameters as a list
start = str(10)
end = str(40)
step = str(6)



def startRender():

    for i in range(6):
        start_frame = int(start) + i
        parameters = [str(start_frame), end, step]
        try:
            # Use subprocess.run() to run the Python script with parameters
            subprocess.run(['powershell', f'mayapy {python_script}'] + parameters, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        print(parameters)

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     for i in range(6):
#         start = i + int(start)
#         executor.map(startRender(str(start), end, step))
processes = []
if __name__ == '__main__':
    # Create two separate processes to open Notepad windows
    for _ in range(6):
        process = multiprocessing.Process(target=startRender)
        processes.append(process)

    for process in processes:
        process.start()

