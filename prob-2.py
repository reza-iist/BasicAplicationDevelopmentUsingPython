import csv
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)


CSV_FILE = "students_info.csv"
PDF_FILE = "students_report.pdf"


# CSV file-এর column names
FIELD_NAMES = [
    "Student ID",
    "Name",
    "Roll",
    "Semester",
    "Shift",
    "Department",
    "Date of Birth",
    "Phone Number"
]


# শিক্ষার্থীর তথ্য নেওয়ার function
def get_student_data():
    print("\n--- Enter Student Information ---")

    student = {
        "Student ID": input("Enter Student ID: "),
        "Name": input("Enter Student Name: "),
        "Roll": input("Enter Roll: "),
        "Semester": input("Enter Semester: "),
        "Shift": input("Enter Shift: "),
        "Department": input("Enter Department: "),
        "Date of Birth": input(
            "Enter Date of Birth (DD-MM-YYYY): "
        ),
        "Phone Number": input("Enter Phone Number: ")
    }

    return student


# CSV file-এ তথ্য সংরক্ষণের function
def store_student_data(student, filename=CSV_FILE):

    # File না থাকলে অথবা empty হলে header লিখতে হবে
    file_exists = (
        os.path.exists(filename)
        and os.path.getsize(filename) > 0
    )

    with open(
        filename,
        mode="a",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELD_NAMES
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(student)

    print("\nStudent data added successfully.")


# CSV file-এর data screen-এ দেখানোর function
def display_students(filename=CSV_FILE):

    if not os.path.exists(filename):
        print("\nNo student record found.")
        return

    print("\n--- Stored Student Information ---")

    with open(
        filename,
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        record_found = False

        for student in reader:
            record_found = True

            print("-" * 40)

            for key, value in student.items():
                print(f"{key}: {value}")

        if not record_found:
            print("No student record found.")


# CSV file থেকে PDF report তৈরির function
def generate_pdf_report(
    csv_filename=CSV_FILE,
    pdf_filename=PDF_FILE
):

    if not os.path.exists(csv_filename):
        print("\nCSV file not found.")
        print("Please add student information first.")
        return

    # CSV file থেকে সব row পড়া
    with open(
        csv_filename,
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.reader(file)
        student_data = list(reader)

    # Header ছাড়া কোনো student record আছে কি না
    if len(student_data) <= 1:
        print("\nNo student record is available.")
        return

    # Landscape A4 PDF তৈরি
    document = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4),
        rightMargin=24,
        leftMargin=24,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    report_elements = []

    # PDF title
    title = Paragraph(
        "Student Information Report",
        styles["Title"]
    )

    report_elements.append(title)
    report_elements.append(Spacer(1, 12))

    # Table তৈরি
    table = Table(
        student_data,
        repeatRows=1,
        colWidths=[
            0.80 * inch,   # Student ID
            1.15 * inch,   # Name
            0.75 * inch,   # Roll
            0.72 * inch,   # Semester
            0.65 * inch,   # Shift
            0.90 * inch,   # Department
            1.05 * inch,   # DOB
            1.10 * inch    # Phone
        ]
    )

    # Table design
    table.setStyle(
        TableStyle([
            # Header background
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#2E74B5")
            ),

            # Header text colour
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            # Header alignment
            (
                "ALIGN",
                (0, 0),
                (-1, 0),
                "CENTER"
            ),

            # পুরো table alignment
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),

            # Table grid
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            # Font size
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                8
            ),

            # Header font
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            # Row background
            (
                "ROWBACKGROUNDS",
                (0, 1),
                (-1, -1),
                [
                    colors.white,
                    colors.HexColor("#E8EEF5")
                ]
            ),

            # Cell padding
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                6
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    report_elements.append(table)

    # PDF build
    document.build(report_elements)

    print(f"\nPDF report generated: {pdf_filename}")


# Main menu
def main():

    while True:
        print("\n==============================")
        print(" Student Information Management")
        print("==============================")
        print("1. Add new student information")
        print("2. Display student information")
        print("3. Generate PDF report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student = get_student_data()
            store_student_data(student)

        elif choice == "2":
            display_students()

        elif choice == "3":
            generate_pdf_report()

        elif choice == "4":
            print("\nExiting the program.")
            break

        else:
            print("\nInvalid choice. Please select 1 to 4.")


# Program শুরু
if __name__ == "__main__":
    main()
