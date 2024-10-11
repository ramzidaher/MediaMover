import os
import shutil
import psutil
from colorama import init, Fore, Style

# Initialize colorama for colored terminal text
init(autoreset=True)

# Function to display ASCII art with a nicer title
def display_ascii():
    print(Fore.CYAN + Style.BRIGHT + """
  _______  _______  ______  _________ _______  _______  _______           _______  _______ 
(       )(  ____ \(  __  \ \__   __/(  ___  )(       )(  ___  )|\     /|(  ____ \(  ____ )
| () () || (    \/| (  \  )   ) (   | (   ) || () () || (   ) || )   ( || (    \/| (    )|
| || || || (__    | |   ) |   | |   | (___) || || || || |   | || |   | || (__    | (____)|
| |(_)| ||  __)   | |   | |   | |   |  ___  || |(_)| || |   | |( (   ) )|  __)   |     __)
| |   | || (      | |   ) |   | |   | (   ) || |   | || |   | | \ \_/ / | (      | (\ (   
| )   ( || (____/\| (__/  )___) (___| )   ( || )   ( || (___) |  \   /  | (____/\| ) \ \__
|/     \|(_______/(______/ \_______/|/     \||/     \|(_______)   \_/   (_______/|/   \__/
                                                                                          """)
    print(Fore.GREEN + "Welcome to MediaMover Pro!")
    print(Fore.YELLOW + "Effortlessly transfer your photos and videos from one drive to another.\n")

# Function to list available disks, excluding snap/loop and system partitions
def list_disks():
    partitions = psutil.disk_partitions()
    print(Fore.MAGENTA + Style.BRIGHT + "Available Disks:")
    count = 0
    filtered_partitions = []
    for partition in partitions:
        # Exclude loop devices and system partitions
        if "loop" not in partition.device and "/boot" not in partition.mountpoint:
            count += 1
            filtered_partitions.append(partition)
            print(f"{count}: {partition.device} - {partition.mountpoint}")
    return filtered_partitions

# Function to select a disk from the filtered list
def select_disk():
    while True:
        partitions = list_disks()
        disk_choice = input(Fore.CYAN + "Select a disk number from the list, 'B' to go back, or 'R' to refresh: ").strip().upper()
        
        if disk_choice == 'B':
            return None  # Signal to go back
        elif disk_choice == 'R':
            continue  # Refresh the list
        else:
            try:
                disk_choice = int(disk_choice) - 1
                if 0 <= disk_choice < len(partitions):
                    return partitions[disk_choice].device, partitions[disk_choice].mountpoint
                else:
                    print(Fore.RED + "Invalid selection. Try again.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")

# Function to navigate, select, and create folders
def select_folder(starting_folder):
    current_folder = starting_folder
    root_folder = starting_folder  # Store the root of the selected drive

    while True:
        print(Fore.GREEN + f"\nCurrent Folder: {current_folder}")
        print(Fore.YELLOW + "Available Folders:")
        items = os.listdir(current_folder)
        folders = [item for item in items if os.path.isdir(os.path.join(current_folder, item))]

        # List the folders
        for i, folder in enumerate(folders):
            print(f"{i+1}: {folder}")
        print("0: Select this folder")
        print("-1: Create a new folder")
        print("B: Go back")
        print("R: Refresh the folder list")
        
        # Get user input
        folder_choice = input(Fore.CYAN + "\nSelect a folder number to enter, 0 to choose this folder, -1 to create a new folder, B to go back, or R to refresh: ").strip().upper()

        if folder_choice == '0':
            return current_folder
        elif folder_choice == '-1':
            # Create a new folder
            new_folder_name = input(Fore.CYAN + "Enter the name for the new folder: ").strip()
            new_folder_path = os.path.join(current_folder, new_folder_name)
            try:
                os.mkdir(new_folder_path)
                print(Fore.GREEN + f"Folder '{new_folder_name}' created successfully.")
            except FileExistsError:
                print(Fore.RED + f"Folder '{new_folder_name}' already exists.")
            except Exception as e:
                print(Fore.RED + f"Error creating folder: {e}")
        elif folder_choice == 'B':
            if current_folder == root_folder:
                print(Fore.CYAN + "Returning to drive selection...")
                return None  # Return to drive selection if at the root
            else:
                current_folder = os.path.dirname(current_folder)  # Go up one level
        elif folder_choice == 'R':
            continue  # Refresh the folder list
        else:
            try:
                folder_choice = int(folder_choice) - 1
                if 0 <= folder_choice < len(folders):
                    current_folder = os.path.join(current_folder, folders[folder_choice])
                else:
                    print(Fore.RED + "Invalid selection. Try again.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")

# Function to clean pasted photo or video names
def clean_names(media_names):
    return [name.strip("- [ ]").strip() for name in media_names if name.strip()]

# Function to collect multiline input for media names
def get_media_names():
    print(Fore.YELLOW + "\nPaste the list of file names (type 'END' when done):")
    media_names = []
    while True:
        line = input()
        if line.strip().lower() == 'end':
            break
        media_names.append(line)
    return clean_names(media_names)

# Main script
def main():
    display_ascii()

    # Ask user whether to move photos or videos
    media_type = input(Fore.CYAN + "Do you want to move 'photo' or 'video' files? ").strip().lower()

    if media_type == "photo":
        # Ask for File Type to Transfer (RAW, JPG, or Both)
        file_type = input(Fore.MAGENTA + "\nEnter file type to transfer (RAW, JPG, or BOTH): ").lower()
        if file_type == "raw":
            extensions = [".ARW"]
        elif file_type == "jpg":
            extensions = [".JPG"]
        else:
            extensions = [".ARW", ".JPG"]

    elif media_type == "video":
        print(Fore.GREEN + "\nDefault video file type set to MP4.")
        extensions = [".mp4"]

    else:
        print(Fore.RED + "Invalid selection. Please choose either 'photo' or 'video'.")
        return

    # Select Source Drive
    while True:
        print(Fore.GREEN + "Select the source drive:")
        source_disk = select_disk()
        if source_disk is None:
            print(Fore.RED + "Returning to media type selection.")
            return  # Exit or restart the process
        else:
            source_device, source_mountpoint = source_disk
            source_folder = select_folder(source_mountpoint)
            if source_folder is None:
                continue  # Go back to drive selection if the user pressed 'B'
            break

    # Select Destination Drive
    while True:
        print(Fore.GREEN + "\nSelect the destination drive:")
        destination_disk = select_disk()
        if destination_disk is None:
            print(Fore.RED + "Returning to drive selection.")
            continue  # Go back to drive selection if the user pressed 'B'
        else:
            destination_device, destination_mountpoint = destination_disk
            destination_folder = select_folder(destination_mountpoint)
            if destination_folder is None:
                continue  # Go back to drive selection if the user pressed 'B'
            break

    # Get multiline input for media names
    cleaned_names = get_media_names()

    print(Fore.GREEN + "\nStarting the transfer process...\n")

    # Transfer Files
    for name in cleaned_names:
        for ext in extensions:
            file_path = os.path.join(source_folder, name + ext)
            if os.path.exists(file_path):
                destination_path = os.path.join(destination_folder, name + ext)
                shutil.copy(file_path, destination_path)
                print(Fore.CYAN + f"Transferred {name}{ext}")
            else:
                print(Fore.RED + f"File {name}{ext} not found")

    # Completion Message
    print(Fore.GREEN + "\nTransfer complete!")

# Run the script
if __name__ == "__main__":
    main()

