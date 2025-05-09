import hashlib
import sys
import time

# Target SHA-256 hash to match
target_sha256_hash = "eb0af6f292cb6b5ec229ffd1c8a12bc72e62794fac869659177c1dd83b04cce3"

# Supported encodings for testing
encoding_formats = ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]

# Case transformations to apply
def case_original(text):
    return text

def case_lower(text):
    return text.lower()

def case_upper(text):
    return text.upper()

case_transformations = {
        "original": case_original,
        "lower": case_lower,
        "upper": case_upper,
}

# We will load the cheese from the cheese list
with open("cheese_list.txt", "r") as file:
    cheese_names = [line.strip() for line in file if line.strip()]

match_found = False

def check_hash(candidate_bytes, method, extra_info, cheese, case_type, encoding, salt):
    """
    Compute SHA-256 hash for a given byte sequence and compare it to the target hash.
    If a match is found, display relevant details and return True.
    """
    global match_found
    computed_hash = hashlib.sha256(candidate_bytes).hexdigest()

    if computed_hash == target_sha256_hash:
        print("\n[!!] VALID MATCH FOUND!")
        print("=" * 40)
        print(f"[+] Cheese Name  : {cheese}")
        print(f"[+] Case Variant : {case_type}")
        print(f"[+] Encoding     : {encoding}")
        print(f"[+] Salt Value   : (0x{salt:02x})")
        print(f"[+] Method Used  : {method}")
        print(f"[+] Extra Info   : {extra_info}")
        print(f"[+] SHA-256 Hash : {computed_hash}")
        try:
            decoded_candidate = candidate_bytes.decode(encoding)
        except Exception:
            decoded_candidate = repr(candidate_bytes)
        print(f"[+] Candidate String ({encoding}): {decoded_candidate}")
        print("=" * 40)
        match_found = True
        return True
    return False

# Start brute-force testing
start_time = time.time()
print("[*] Starting cheese cracking operation....")

for cheese in cheese_names:
    for case_type, transform_func in case_transformations.items():
        modified_cheese = transform_func(cheese)

        for encoding in encoding_formats:
            try:
                cheese_bytes = modified_cheese.encode(encoding)
            except Exception:
                continue

            for salt_value in range(256):
                salt_byte = bytes([salt_value])
                salt_hex_str = format(salt_value, "02x")

                try:
                    salt_hex_bytes = salt_hex_str.encode(encoding)
                except Exception:
                    salt_hex_bytes = salt_hex_str.encode("utf-8")  # Fallback encoding

                # Test different variations of salted hashes
                tests = [
                    (cheese_bytes + salt_byte, "append_raw", "raw byte appended"),
                    (salt_byte + cheese_bytes, "prepend_raw", "raw byte prepended"),
                    (cheese_bytes + salt_hex_bytes, "append_hex", "hex string appended"),
                    (salt_hex_bytes + cheese_bytes, "prepend_hex", "hex string prepended"),
                ]

                for candidate, method, extra_info in tests:
                    if check_hash(candidate, method, extra_info, cheese, case_type, encoding, salt_value):
                        break
                if match_found:
                    break

                # Insert salt byte at every possible index
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_byte + cheese_bytes[i:]
                    if check_hash(candidate, "insert_raw", f"at index {i}", cheese, case_type, encoding, salt_value):
                        break
                if match_found:
                    break

                # Insert hex-encoded salt at every index
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_hex_bytes + cheese_bytes[i:]
                    if check_hash(candidate, "insert_hex", f"at index {i}", cheese, case_type, encoding, salt_value):
                        break
                if match_found:
                    break
            if match_found:
                break
        if match_found:
            break
    if match_found:
        break

end_time = time.time()

if not match_found:
    print("[!] No matching cheese and salt combination was found.")
else:
    print(f"\n[+] Execution completed in {end_time - start_time:.2f} seconds.")
