import time
import random
import string
import sys

def print_with_delay(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generate_random_code(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def hacking_animation():
    print_with_delay("=====================================")
    print_with_delay("Initializing CyberMatrix v9.0...")
    print_with_delay("Booting Quantum Crypto Engine...")
    time.sleep(1)
    
    print_with_delay("\n> Accessing Mainframe...")
    print_with_delay("> Bypassing Firewall...")
    for _ in range(3):
        print_with_delay(f"> Decrypting Layer {generate_random_code(8)}...")
        time.sleep(0.5)
    
    print_with_delay("\n> Establishing Secure Connection...")
    print_with_delay("> Quantum Encryption: ACTIVE")
    print_with_delay("> Trace Protection: ENABLED")
    
    print_with_delay("\n> Injecting Neural Payload...")
    for i in range(1, 101, 5):
        print_with_delay(f"> Progress: {i}% - {generate_random_code(12)}")
        time.sleep(0.1)
    
    print_with_delay("\n=====================================")
    print_with_delay("ACCESS GRANTED")
    print_with_delay("System Compromised Successfully!")
    print_with_delay("=====================================")
    print_with_delay("\nCREATED by: Mr. Sabaz Ali Khan")
    print_with_delay("Pakistani Ethical Hacker")
    print_with_delay("Cyber Security Specialist")
    print_with_delay("=====================================")

if __name__ == "__main__":
    print_with_delay("WARNING: Unauthorized Access Detected!")
    time.sleep(1)
    hacking_animation()