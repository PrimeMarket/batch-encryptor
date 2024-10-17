import os

bytes_for_encryption = b'\xFF\xFE\x26\x63\x6C\x73\x0D\x0A'

def encrypt_batch_file(original_batch_file):
    try:
        with open(fr'{original_batch_file}', 'rb') as f:
            existing_data = f.read()

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print(f"Unexpected error: {e}")
        return
    
    try:
        with open(fr'encypted-{os.path.basename(original_batch_file)}', 'wb') as f:
            f.write(bytes_for_encryption + existing_data)

    except Exception as e:
        print(f"Unexpected error:: {e}")
        return
    
    else:
        print("File encrypted successfully")

file = input("Batch file to encypt: ")
encrypt_batch_file(file)