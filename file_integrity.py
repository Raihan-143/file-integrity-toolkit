import hashlib
import os

def calculate_file_hash(filepath):

    #A function that calculates the SHA-256 hash by reading a large file in 4-kilobyte (4096-byte) chunks, avoiding memory crashes
    hasher = hashlib.sha256()
    
    try:
        # Opening the file in 'rb' (Read Binary) mode
        with open(filepath, 'rb') as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

# Creating a dummy file for testing
test_file = "sensitive_system_config.txt"

# 1. Creating an initial baseline by writing some text in the file.
with open(test_file, "w") as f:
    f.write("ALLOW_REMOTE_LOGIN=FALSE\nFIREWALL_STATUS=ENABLED")

baseline_hash = calculate_file_hash(test_file)
print(f"[*] Baseline SHA-256: {baseline_hash}")

# 2. Mimicking the attacker (changing a single character or space in the file)
print("\n[!] Simulating Unauthorized Tampering...")
with open(test_file, "a") as f:
    f.write("\nMALICIOUS_USER_ADDED=TRUE")

# 3. Checking the new hash of the tampered file
new_hash = calculate_file_hash(test_file)
print(f"[*] New SHA-256     : {new_hash}")

# 4. Defensive Integrity Verification
print("\n--- Integrity Audit Result ---")
if baseline_hash == new_hash:
    print("[+] File Integrity INTACT: No changes detected.")
else:
    print("[-] CRITICAL ALERT: File has been TAMPERED with or modified!")

# Cleanup: Deleting the file after the test.
if os.path.exists(test_file):
    os.remove(test_file)