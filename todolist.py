import json
import os
import time

DATA_FILE = "tasks.json"

# Color codes
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_tasks(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def add_task(self, desc):
        self.tasks.append({
            'id': len(self.tasks) + 1,
            'description': desc,
            'completed': False
        })
        self.save_tasks()
        print(f"\n{GREEN}✨ ✨ ✨ TUGAS BERHASIL DITAMBAHKAN! ✨ ✨ ✨{RESET}")
        print(f"{YELLOW}→ \"{desc}\"{RESET}\n")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"\n{GREEN}🎉 🎉 🎉 SELESAI! 🎉 🎉 🎉{RESET}")
                print(f"{YELLOW}✔ '{task['description']}'{RESET}\n")
                return
        print(f"{RED}❌ Tugas tidak ditemukan!{RESET}\n")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"\n{RED}🗑️ POOF! Tugas hilang! 💨{RESET}\n")
                return
        print(f"{RED}❌ Tugas tidak ditemukan!{RESET}\n")

    def display_tasks(self):
        print(f"\n{CYAN}{'┌─' + '─' * 60 + '─┐'}{RESET}")
        print(f"{CYAN}│{RESET}{YELLOW}{BOLD} 📋 DAFTAR TUGAS KERENMU 📋".center(62)}{RESET}{CYAN}│{RESET}")
        print(f"{CYAN}├─' + '─' * 60 + '─┤'{RESET}")
        
        if not self.tasks:
            msg = "Tidak ada tugas! Mari buat rencana seru! 🎊"
            print(f"{CYAN}│{RESET}{MAGENTA}{msg.center(62)}{RESET}{CYAN}│{RESET}")
        else:
            completed = sum(1 for t in self.tasks if t['completed'])
            total = len(self.tasks)
            progress = f"[{completed}/{total}] {chr(9608) * completed}{chr(9617) * (total - completed)}"
            print(f"{CYAN}│{RESET} {progress.ljust(60)} {CYAN}│{RESET}")
            print(f"{CYAN}├─' + '─' * 60 + '─┤'{RESET}")
            
            for task in self.tasks:
                if task['completed']:
                    status = f"{GREEN}✅{RESET}"
                    desc = f"{GREEN}{task['description']}{RESET}"
                else:
                    status = f"{YELLOW}⭕{RESET}"
                    desc = f"{BLUE}{task['description']}{RESET}"
                line = f" {status} [{task['id']}] {desc}"
                print(f"{CYAN}│{RESET}{line.ljust(60)} {CYAN}│{RESET}")
        
        print(f"{CYAN}└─' + '─' * 60 + '─┘'{RESET}\n")

    def show_menu(self):
        print(f"\n{MAGENTA}{'▀' * 64}{RESET}")
        print(f"{YELLOW}{BOLD}{'🚀 APLIKASI SUPER KEREN TODO LIST 🚀'.center(64)}{RESET}")
        print(f"{MAGENTA}{'▄' * 64}{RESET}\n")
        print(f"{CYAN}   [1]{RESET} ➕ Tambah Tugas Baru")
        print(f"{CYAN}   [2]{RESET} ✅ Tandai Tugas Selesai")
        print(f"{CYAN}   [3]{RESET} 🗑️  Hapus Tugas")
        print(f"{CYAN}   [4]{RESET} 📋 Lihat Semua Tugas")
        print(f"{CYAN}   [5]{RESET} 🚪 Keluar Aplikasi\n")

    def welcome(self):
        print(f"\n{BOLD}{YELLOW}{'█' * 64}{RESET}")
        print(f"{BOLD}{YELLOW}║{RESET}{'   🎮 SELAMAT DATANG DI TODO LIST TERBAIK! 🎮   '.center(62)}{BOLD}{YELLOW}║{RESET}")
        print(f"{BOLD}{YELLOW}║{RESET}{'   Mari kita ciptakan hari yang produktif! 💪   '.center(62)}{BOLD}{YELLOW}║{RESET}")
        print(f"{BOLD}{YELLOW}{'█' * 64}{RESET}\n")

    def goodbye(self):
        print(f"\n{BOLD}{MAGENTA}{'█' * 64}{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET}{'   👋 TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI! 👋   '.center(62)}{BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}║{RESET}{'   Jangan lupa istirahat yang cukup! 😴✨   '.center(62)}{BOLD}{MAGENTA}║{RESET}")
        print(f"{BOLD}{MAGENTA}{'█' * 64}{RESET}\n")

def main():
    todo = TodoList()
    todo.welcome()
    
    while True:
        todo.show_menu()
        choice = input(f"{BOLD}{CYAN}Pilih menu [1-5]: {RESET}").strip()
        
        if choice == '1':
            desc = input(f"{BOLD}{YELLOW}📝 Tulis deskripsi tugas: {RESET}").strip()
            if desc:
                todo.add_task(desc)
            else:
                print(f"{RED}⚠️  Jangan kosong dong!{RESET}\n")
        
        elif choice == '2':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input(f"{BOLD}{CYAN}Nomor tugas yang selesai: {RESET}"))
                    todo.complete_task(task_id)
                except:
                    print(f"{RED}❌ Masukkan angka yang benar!{RESET}\n")
        
        elif choice == '3':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input(f"{BOLD}{CYAN}Nomor tugas yang dihapus: {RESET}"))
                    todo.delete_task(task_id)
                except:
                    print(f"{RED}❌ Masukkan angka yang benar!{RESET}\n")
        
        elif choice == '4':
            todo.display_tasks()
        
        elif choice == '5':
            todo.goodbye()
            break
        
        else:
            print(f"{RED}⚠️  Pilihan tidak ada! Coba lagi ya!{RESET}\n")

if __name__ == "__main__":
    main()

