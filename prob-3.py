import qrcode

from barcode import Code128
from barcode.writer import ImageWriter

from PIL import Image
from pyzbar.pyzbar import decode


# শিক্ষার্থীর ID ও নাম নেওয়ার function
def take_student_info():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    return student_id, student_name


# QR Code তৈরির function
def generate_qr_code(student_id, student_name):
    data = f"Student ID: {student_id}, Name: {student_name}"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    qr_filename = "QR_Code_1.png"
    qr_image.save(qr_filename)

    print(f"QR Code generated successfully: {qr_filename}")

    return qr_filename


# Barcode তৈরির function
def generate_barcode(student_id, student_name):
    data = f"Student ID: {student_id}, Name: {student_name}"

    barcode_object = Code128(
        data,
        writer=ImageWriter()
    )

    # .png extension স্বয়ংক্রিয়ভাবে যোগ হবে
    barcode_filename = barcode_object.save("Barcode_1")

    print(f"Barcode generated successfully: {barcode_filename}")

    return barcode_filename


# QR Code অথবা Barcode decode করার function
def decode_image(filename):
    image = Image.open(filename)

    decoded_items = decode(image)

    if decoded_items:
        for item in decoded_items:
            decoded_text = item.data.decode("utf-8")

            print("Code Type:", item.type)
            print("Decoded Data:", decoded_text)
    else:
        print(f"No code detected in {filename}")


# Main function
def main():
    student_id, student_name = take_student_info()

    qr_file = generate_qr_code(
        student_id,
        student_name
    )

    barcode_file = generate_barcode(
        student_id,
        student_name
    )

    print("\n--- Decoding QR Code ---")
    decode_image(qr_file)

    print("\n--- Decoding Barcode ---")
    decode_image(barcode_file)


# Program শুরু
if __name__ == "__main__":
    main()
