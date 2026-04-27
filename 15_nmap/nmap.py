print("1. Ping Scan")
print("2. TCP Port Scan")
print("3. UDP Scan")
print("4. OS Detection")
print("5. Xmas Scan")
print("6. Aggressive Scan")
print("7. Scan Specific Ports")

choice = int(input("Enter choice: "))
target = input("Enter target IP: ")

if choice == 1:
    print("Command: nmap -sn", target)

elif choice == 2:
    print("Command: nmap -sT", target)

elif choice == 3:
    print("Command: nmap -sU", target)

elif choice == 4:
    print("Command: nmap -O", target)

elif choice == 5:
    print("Command: nmap -sX", target)

elif choice == 6:
    print("Command: nmap -A", target)

elif choice == 7:
    ports = input("Enter ports (e.g. 21-25,80): ")
    print("Command: nmap -p", ports, target)

else:
    print("Invalid choice")