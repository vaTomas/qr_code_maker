import qrcode
import qrcode.image.svg
import csv
import os
import re
from urllib.parse import quote
from tag import Tag

# --- Constants ---
CSV_FILE = "info.csv"
TEMPLATE_FILE = "email_body.txt"
OUTPUT_DIR = "output"


def sanitize_filename(filename):
    """Removes characters that are illegal in filenames."""
    return re.sub(r'[\\/*?:"<>|]', "_", filename)


def load_tags_from_csv(filepath):
    """Loads tag information from a CSV file into a list of Tag objects."""
    tags = []
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip header
            print(f"Reading CSV with header: {header}")
            for row in csv_reader:
                if row:  # Avoids errors from blank lines
                    tag = Tag(name=row[0], email=row[1], type=row[2])
                    tags.append(tag)
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    return tags


def load_email_template(filepath):
    """Reads the content of a text file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The template file {filepath} was not found.")
        return ""  # Return empty string if template is missing


def create_mailto_uri(tag, body_template):
    """Creates a URL-encoded mailto: URI for a given tag."""
    subject = f"[FOUND] {tag.name} {tag.type}"
    encoded_subject = quote(subject)
    encoded_body = quote(body_template)
    return f"mailto:{tag.email}?subject={encoded_subject}&body={encoded_body}"


def generate_and_save_qr_code(uri, tag, output_dir):
    """Generates an SVG QR code and saves it to a specified directory."""
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Sanitize filename components to prevent errors
    safe_name = sanitize_filename(tag.name)
    safe_email = sanitize_filename(tag.email)
    filename = f"{safe_name}_{safe_email}.svg"

    # Create the full path for saving
    save_path = os.path.join(output_dir, filename)

    # Generate the QR code with specified parameters
    qr_code = qrcode.make(
        uri,
        image_factory=qrcode.image.svg.SvgImage,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        version=None,
    )
    qr_code.save(save_path)
    print(f"Successfully generated QR code: {save_path}")


def main():
    """Main function to orchestrate the QR code generation process."""
    tags = load_tags_from_csv(CSV_FILE)
    email_body = load_email_template(TEMPLATE_FILE)

    if not tags or not email_body:
        print("Could not load necessary files. Exiting.")
        return

    for tag in tags:
        mailto_uri = create_mailto_uri(tag, email_body)
        generate_and_save_qr_code(mailto_uri, tag, OUTPUT_DIR)

    print("\nProcessing complete.")


if __name__ == "__main__":
    main()
