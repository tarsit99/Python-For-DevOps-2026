import psutil

def get_system_health():

    # Take system threshold values from user
    cpu_threshold = int(input("Enter the CPU Threshold: "))
    memory_threshold = int(input("Enter the Memory Threshold: "))
    disk_threshold = int(input("Enter the Disk Threshold: "))

    # Get current system health metrics
    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('/').percent

    # Print current system health metrics
    print("\n-----System Health Metrics-----")
    print("Current CPU Usage:", current_cpu, "%")
    print("Current Memory Usage:", current_memory, "%")
    print("Current Disk Usage:", current_disk, "%")
    print("--------------------------------\n")

    # Check CPU
    if current_cpu > cpu_threshold:
        print("CPU Alert! Usage is above threshold.")
    else:
        print("CPU is in Safe state...")

    # Check Memory
    if current_memory > memory_threshold:
        print("Memory Alert! Usage is above threshold.")
    else:
        print("Memory is in Safe state...")

    # Check Disk
    if current_disk > disk_threshold:
        print("Disk Alert! Usage is above threshold.")
    else:
        print("Disk is in Safe state...")

get_system_health()