
# MediaMover Pro

![MediaMover ASCII Logo](https://postimg.cc/hhLRZBGd)  
*Effortlessly transfer your photos and videos from one drive to another.*

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
  - [Selecting Disks and Folders](#selecting-disks-and-folders)
  - [Transferring Files](#transferring-files)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**MediaMover Pro** is a command-line tool built to make transferring photos and videos between different drives easy and efficient. With an intuitive user interface, you can select the source and destination drives, filter file types (like RAW or JPG for photos, and MP4 for videos), and manage folders with ease.

## Features
- Intuitive selection of drives and folders.
- Supports both photo and video file transfers.
- Ability to select file types (e.g., RAW, JPG) for photos.
- Create new folders within the tool.
- Multiline input for file names to transfer only the selected media.
- Provides detailed feedback on file transfers.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ramzidaher/MediaMover.git
    cd MediaMover
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
    ```bash
    python3 mediamover.py
    ```

## Usage

### Running the Script

1. **Navigate to the MediaMover directory**:
    ```bash
    cd /path/to/MediaMover
    ```

2. **Run the script**:
    ```bash
    python3 mediamover.py
    ```

### Selecting Disks and Folders

- When the script starts, you'll be prompted to select the source and destination drives. Use the disk numbers shown to select your disk.
  
- You can also navigate and select folders within the chosen disk, create new folders, or go back to the previous folder.

### Transferring Files

- For **photos**, you will be asked to select the file type: RAW, JPG, or both.
  
- For **videos**, MP4 is the default file type.
  
- Paste the list of file names (without extensions) that you want to transfer and the script will handle the rest. Type `END` when you're done entering file names.

## Requirements
- Python 3.x
- The following Python packages:
  - `psutil`: For detecting system disks and partitions.
  - `colorama`: For colorful terminal text.
  - `shutil`: For handling file transfers.

To install the required Python packages, run:
```bash
pip install psutil colorama
```

## Contributing
Contributions are welcome! If you have any suggestions or find any issues, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
