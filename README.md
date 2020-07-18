# Image Encryptor
A simple python package to encrypt and decrypt images.

## Getting Started
You need to have `python3` and `pip3` in your system.
## Installing
- First clone the project.
  ```
  git clone https://github.com/sdsubhajitdas/Image-Encryptor.git
  ```
- (Optional) If you like you can use `virtualenv` to create a private environment and then activate it.
- Installing the required packages.
  ```
  pip install -r requirements.txt
  ```
- Create a salt file for your locker. Keep this salt file safe because if you loose this file then decrypting the data won't be possible even with correct password.
  Open python3 on your terminal.
  ```
  import os
  os.urandom(16)
  ```
  This should give a output like this.
  ```
  b';\x94p\n\x91}\x1e\x11\x11\xed\x02\xbb\x04\xfe\x11u'
  ```
  Pick the string within the single quote and paste it inside a file named `salt` without any extension inside the folder `../Image Encryptor/`
  ```
  Image Encryptor
  | 
  |-decrypt.py
  |-encrypt.py
  .
  .
  |- salt  
  
  Inside salt
  ;\x94p\n\x91}\x1e\x11\x11\xed\x02\xbb\x04\xfe\x11u
  ```

## Usage
#### encrypt.py
- To get help about the commands `python encrypt.py -h`
  ```
  usage: encrypt.py [-h] [-d DIR] [-f FILE]
  List of commands for Image Encryptor
  optional arguments:
    -h, --help            show this help message and exit
    -d DIR, --dir DIR     The directory path for group of images.
    -f FILE, --file FILE  The path of the file to encrpt.
  ```
- Encrypt a single file `python encrypt.py -f <FILENAME>`
- Encrypt a folder `python encrypt.py -d <FOLDERNAME>`

#### decrypt.py
- To get help about the commands `python decrypt.py -h`
  ```
  usage: decrypt.py [-h] [-d DIR] [-f FILE]
  List of commands for Image Decryptor
  optional arguments:
    -h, --help            show this help message and exit
    -d DIR, --dir DIR     The directory path for group of images.
    -f FILE, --file FILE  The path of the file to encrpt.
  ```
- Encrypt a single file `python decrypt.py -f <FILENAME>`
- Encrypt a folder `python decrypt.py -d <FOLDERNAME>`


##### If the salt file is changed or deleted then the locker won't work so I suggest that create a backup of that file somewhere else.
##### The dimensions of the images without affecting the aspect ratio are reduced to speed up the process. Change the dimensions [here](image_encryptor/__init__.py)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
