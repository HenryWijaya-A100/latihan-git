import json
import os

DATA_FILE = "tasks.json"

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
        print("✨ Tugas ditambahkan!\n")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"🎉 '{task['description']}' selesai!\n")
                return
        print("❌ Tugas tidak ditemukan!\n")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print("🗑️ Tugas dihapus!\n")
                return
        print("❌ Tugas tidak ditemukan!\n")

    def display_tasks(self):
        print("\n" + "=" * 50)
        print("📋 DAFTAR TUGAS".center(50))
        print("=" * 50)
        if not self.tasks:
            print("Tidak ada tugas 🎊".center(50))
        else:
            for task in self.tasks:
                status = "✅" if task['completed'] else "⭕"
                print(f" {status} [{task['id']}] {task['description']}")
        print("=" * 50 + "\n")

    def show_menu(self):
        print("🚀 TODO LIST\n")
        print("[1] ➕ Tambah Tugas")
        print("[2] ✅ Tandai Selesai")
        print("[3] 🗑️  Hapus Tugas")
        print("[4] 📋 Lihat Tugas")
        print("[5] 🚪 Keluar\n")

def main():
    todo = TodoList()
    print("\n🌟 Selamat Datang! 🌟\n")
    
    while True:
        todo.show_menu()
        choice = input("Pilih [1-5]: ").strip()
        
        if choice == '1':
            desc = input("📝 Deskripsi: ").strip()
            if desc:
                todo.add_task(desc)
        elif choice == '2':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("Nomor tugas: "))
                    todo.complete_task(task_id)
                except:
                    print("❌ Input tidak valid!\n")
        elif choice == '3':
            todo.display_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("Nomor tugas: "))
                    todo.delete_task(task_id)
                except:
                    print("❌ Input tidak valid!\n")
        elif choice == '4':
            todo.display_tasks()
        elif choice == '5':
            print("👋 Sampai jumpa!\n")
            break
        else:
            print("⚠️ Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
