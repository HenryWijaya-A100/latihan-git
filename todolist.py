import json
import os
from datetime import datetime

# File untuk menyimpan data
DATA_FILE = "tasks.json"

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Memuat tugas dari file"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Menyimpan tugas ke file"""
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)

    def add_task(self, description):
        """Menambah tugas baru"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'date': datetime.now().strftime("%d-%m-%Y %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\n✨ Tugas berhasil ditambahkan! ✨\n")

    def complete_task(self, task_id):
        """Menandai tugas sebagai selesai"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"\n🎉 Selamat! Tugas '{task['description']}' sudah diselesaikan! 🎉\n")
                return
        print("\n❌ Tugas tidak ditemukan!\n")

    def delete_task(self, task_id):
        """Menghapus tugas"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted = self.tasks.pop(i)
                self.save_tasks()
                print(f"\n🗑️ Tugas '{deleted['description']}' telah dihapus!\n")
                return
        print("\n❌ Tugas tidak ditemukan!\n")

    def display_tasks(self):
        """Menampilkan semua tugas dengan format menarik"""
        print("\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + " " * 20 + "📋 DAFTAR TUGAS HARIAN 📋" + " " * 31 + "║")
        print("╠" + "═" * 78 + "╣")
        
        if not self.tasks:
            print("║" + " " * 26 + "Tidak ada tugas! 🎊" + " " * 29 + "║")
        else:
            for task in self.tasks:
                status = "✅" if task['completed'] else "⭕"
                task_text = f"{status} [{task['id']}] {task['description']}"
                
                if len(task_text) <= 76:
                    print("║ " + task_text.ljust(76) + " ║")
                else:
                    print("║ " + task_text[:75] + "... ║")
        
        print("╚" + "═" * 78 + "╝")
        print()

    def show_menu(self):
        """Menampilkan menu utama"""
        print("\n╔" + "═" * 48 + "╗")
        print("║" + " " * 12 + "🚀 APLIKASI TODO LIST 🚀" + " " * 11 + "║")
        print("╠" + "═" * 48 + "╣")
        print("║  [1] ➕ Tambah Tugas Baru                      ║")
        print("║  [2] ✅ Tandai Tugas Selesai                  ║")
        print("║  [3] 🗑️  Hapus Tugas                          ║")
        print("║  [4] 📋 Lihat Semua Tugas                     ║")
        print("║  [5] 🚪 Keluar                                ║")
        print("╚" + "═" * 48 + "╝")

def main():
    """Fungsi utama"""
    todo = TodoList()
    
    print("\n" + "🌟" * 25)
    print("    Selamat Datang di Aplikasi TODO LIST! 🎯")
    print("🌟" * 25)
    
    while True:
        todo.show_menu()
        choice = input("Pilih menu [1-5]: ").strip()
        
        if choice == '1':
            print("\n" + "-" * 50)
            description = input("📝 Masukkan deskripsi tugas: ").strip()
            if description:
                todo.add_task(description)
            else:
                print("\n⚠️  Deskripsi tugas tidak boleh kosong!\n")
        
        elif choice == '2':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("Masukkan nomor tugas yang sudah diselesaikan: "))
                    todo.complete_task(task_id)
                except ValueError:
                    print("\n❌ Input tidak valid! Masukkan angka.\n")
        
        elif choice == '3':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("Masukkan nomor tugas yang akan dihapus: "))
                    todo.delete_task(task_id)
                except ValueError:
                    print("\n❌ Input tidak valid! Masukkan angka.\n")
        
        elif choice == '4':
            todo.display_tasks()
            completed = sum(1 for t in todo.tasks if t['completed'])
            total = len(todo.tasks)
            if total > 0:
                print(f"📊 Progress: {completed}/{total} tugas selesai ({completed*100//total}%)")
                if completed == total and total > 0:
                    print("🏆 Luar biasa! Semua tugas sudah diselesaikan! 🏆")
            print()
        
        elif choice == '5':
            print("\n" + "🌟" * 25)
            print("    Terima kasih! Sampai Jumpa Lagi! 👋")
            print("🌟" * 25 + "\n")
            break
        
        else:
            print("\n⚠️  Pilihan tidak valid! Silakan pilih menu 1-5.\n")

if __name__ == "__main__":
    main()
