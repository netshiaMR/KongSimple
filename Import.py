import os
import subprocess

# Path to directory containing .cer files
cert_dir = "/path/to/certificates"

# List all files in the directory
for filename in os.listdir(cert_dir):
    if filename.endswith(".cer"):
        cer_file_path = os.path.join(cert_dir, filename)
        crt_file_path = os.path.join(cert_dir, filename.replace('.cer', '.crt'))

        # Try converting from DER to PEM format
        try:
            subprocess.run(["openssl", "x509", "-inform", "der", "-in", cer_file_path, "-out", crt_file_path], check=True)
            print(f"Converted: {cer_file_path} to {crt_file_path}")
        except subprocess.CalledProcessError:
            # If DER conversion fails, try assuming it's already in PEM format
            try:
                subprocess.run(["openssl", "x509", "-inform", "pem", "-in", cer_file_path, "-out", crt_file_path], check=True)
                print(f"Converted (PEM): {cer_file_path} to {crt_file_path}")
            except subprocess.CalledProcessError:
                print(f"Failed to convert: {cer_file_path}")
