import os
# Remove the original 'bin' directory from the PATH if it exists
original_bin_path = '/data/data/com.termux/files/usr/bin'
os.environ['PATH'] = ':'.join([path for path in os.environ['PATH'].split(':') if path != original_bin_path])

# Add the new 'bin' directory to the PATH
os.environ['PATH'] += ':/storage/shared/TERMUX/filesystem/bin'

# Infinite loop to continuously take user input and execute it
while True:
    # Print the current working directory with color
    print("\033[34m┌──[{}]\033[0m".format(os.getcwd()))  # Blue color for the directory prompt
    
    # Prompt the user to input a command
    command = input("\033[32m└─$\033[0m ")  # Green color for the command prompt
    
    # Check if the user wants to exit
    if command == "exit":
        print("Exiting...")
        break    
 
    # Temporary Updater
    elif command == "get update":    
        os.system("git clone https://github.com/renzaspiras/neo-termux-archlinux.git ~/hello && bash ~/hello/setup.sh")
        os.system("rm -rf ~/hello")

    elif command.startswith("cd "):
        try:
            directory = command.split(" ")[1]
            os.chdir(directory)
        except Exception as e:
            print("\033[31mError: {}\033[0m".format(e))  # Red color for the error message
        continue

    try:
        output = os.popen(command).read()
        print(output)
    except Exception as e:
        # Display an error message if there's an exception
        print("\033[31mError: {}\033[0m".format(e))  # Red color for the error message