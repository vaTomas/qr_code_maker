# QR Code Email Generator

A simple Python utility script to quickly generate SVG QR codes. Each QR code is embedded with a `mailto:` link, pre-filled with a recipient's email, a custom subject line, and a text body from a template. This was created for personal use to streamline the creation of multiple QR-code-based contact tags.
Features

- **Batch Processing:** Reads recipient data from a `info.csv` file.
- **Email Templates:** Uses a text file `email_body.txt` for the email body.
- **Customizable Output:** Generates individual SVG QR codes for each recipient.
- **Dynamic Subjects:** Creates subject lines using the recipient's name and type (e.g., [FOUND] John Doe Bag).
- **Robust Filenaming:** Automatically sanitizes filenames to prevent errors.

## Setup

### Clone the repository:

    git clone https://github.com/vatomas/qr_code_maker.git
    cd qr_code_maker

### Install dependencies:

This script relies on the [qrcode](https://github.com/lincolnloop/python-qrcode) library.

    pip install qrcode

## Usage

### 1. Prepare your data file `info.csv`:

Create a CSV file named `info.csv` in the root directory with the following columns:

- Name
- Email
- Type (e.g., "Backpack", "Keys", "Laptop")

#### Example info.csv:

    name,email,type
    John Doe,john.doe@example.com,Backpack
    Jane Smith,jane.s@example.com,Keys

### 2. Create your email template `email_body.txt`:

Create a text file named `email_body.txt` in the root directory. This file will be used as the body of the email.

#### Example email_body.txt:

    Location: 
    Contact: 

### 3. Run the script:

Execute the `main.py` Python script from your terminal.

    python main.py

### 4. Check the output:

The generated .svg files will be saved in the `output` directory. Each file will be named using the recipient's name and email (e.g., John Doe_john.doe@example.com.svg).

### Customization

You can modify the main.py script to change:

- **QR Code Appearance:** Adjust the `version`, `error_correction`, and `image_factory` parameters in the `qrcode.make()` call.
- **File Paths:** Change the `CSV_FILE`, `TEMPLATE_FILE`, and `OUTPUT_DIR` constants at the top of the script to use different file names or locations.
- **Line Format:** Modify the f-string in the `create_mailto_uri` function to change how the email subject is generated.

## License

This project is licensed under the GNU General Public License v3.0. For the full license text, see https://www.gnu.org/licenses/gpl-3.0.html.
