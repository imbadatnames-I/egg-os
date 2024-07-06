import os
import shutil
import keyboard
import wmi
def on_f4():
    if os.path.exists("c:\\os\\boot_manager.py"):
        with open("c:\\os\\boot_manager.py") as boot_manager:
            boot_manager = boot_manager.read()
            exec(boot_manager)
    else:
        print("> \033[1;32;48mthere is no boot manager installed")
        print("> fixing")
        if os.path.exists(f"C:\\os_rec\\boot_manager.py"):
            shutil.move(f"C:\\os_rec\\boot_manager.py",f"C:\\os\\boot_manager.py")
            shutil.copyfile(f"C:\\os\\boot_manager.py",f"C:\\os_rec\\boot_manager.py") 
            print("> fixed")
            with open(f"c:\\os\\boot_manager.py") as boot_manager:
                boot_manager = boot_manager.read()
                exec(boot_manager)
def on_ctrl_1():
    while True:
        print("> entering bios")
        bios_choice=input("> Do you want to exit view system info or add passwords.\n> ")
        if bios_choice=="exit":
            on_f4()
        if bios_choice=="view":
            c = wmi.WMI()
            def get_bios_info():
                bios_info = c.Win32_BIOS()[0]
                print("> BIOS Information:")
                print(f"  Manufacturer: {bios_info.Manufacturer}")
                print(f"  Version: {bios_info.Version}")
                print(f"  Serial Number: {bios_info.SerialNumber}\n")
            def get_cpu_info():
                for cpu in c.Win32_Processor():
                    print("> CPU Information:")
                    print(f"  Name: {cpu.Name}")
                    print(f"  Manufacturer: {cpu.Manufacturer}")
                    print(f"  Number of Cores: {cpu.NumberOfCores}")
                    print(f"  Number of Logical Processors: {cpu.NumberOfLogicalProcessors}")
                    print(f"  Max Clock Speed: {cpu.MaxClockSpeed} MHz\n")
            def get_ram_info():
                total_mem = 0
                for mem in c.Win32_PhysicalMemory():
                    total_mem += int(mem.Capacity)
                    print("> RAM Information:")
                    print(f"  Manufacturer: {mem.Manufacturer}")
                    print(f"  Capacity: {int(mem.Capacity) / (1024**3)} GB")
                    print(f"  Speed: {mem.Speed} MHz")
                    print(f"  Serial Number: {mem.SerialNumber}\n")
                print(f"Total RAM: {total_mem / (1024**3)} GB\n")
            def get_disk_info():
                for disk in c.Win32_DiskDrive():
                    print("> Disk Information:")
                    print(f"  Model: {disk.Model}")
                    print(f"  Interface Type: {disk.InterfaceType}")
                    print(f"  Serial Number: {disk.SerialNumber}")
                    print(f"  Size: {int(disk.Size) / (1024**3)} GB")
                    print(f"  Partitions: {disk.Partitions}\n")
            def get_os_info():
                os_info = c.Win32_OperatingSystem()[0]
                print("> OS Information:")
                print(f"  Name: {os_info.Name.split('|')[0]}")
                print(f"  Version: {os_info.Version}")
                print(f"  Manufacturer: {os_info.Manufacturer}")
                print(f"  Build Type: {os_info.BuildType}")
                print(f"  Registered User: {os_info.RegisteredUser}")
                print(f"  Serial Number: {os_info.SerialNumber}")
                print(f"  System Directory: {os_info.SystemDirectory}")
                print(f"  Windows Directory: {os_info.WindowsDirectory}\n")
            def main():
                get_bios_info()
                get_cpu_info()
                get_ram_info()
                get_disk_info()
                get_os_info()
            if __name__ == "__main__":
                main()
        if bios_choice=="add passwords":
            NotImplemented
print("                                                                               _____          _ _   _     ")
print("                                                                              |__  /___ _ __ (_) |_| |__  ")
print("                                                                                / // _ \ '_ \| | __| '_ \ ")
print("                                                                               / /|  __/ | | | | |_| | | |")
print("                                                                              /____\___|_| |_|_|\__|_| |_|")
print(">                                                                           to interrupt startup press ctrl+1")
print(">                                                                                to startup press ctrl+0")
keyboard.add_hotkey("ctrl+1",on_ctrl_1)
keyboard.add_hotkey("ctrl+0",on_f4)
keyboard.wait("f4")