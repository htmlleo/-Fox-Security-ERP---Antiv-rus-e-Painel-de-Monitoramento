import os
import threading
import shutil
import psutil
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from pathlib import Path
import random
import time

# ================= CONFIG =================
SCAN_DIRS = [
    Path.home() / "Downloads",
    Path.home() / "Documents",
    Path.home() / "Desktop",
    Path.home() / "AppData" / "Local" / "Temp"
]

DANGEROUS_EXT = [".exe", ".bat", ".ps1", ".vbs", ".js"]
QUARANTINE = Path("quarantine")
QUARANTINE.mkdir(exist_ok=True)

# ================= CORE =================
class Scanner:
    def __init__(self):
        self.scanned = []
        self.suspicious = []

    def scan(self, log):
        self.scanned.clear()
        self.suspicious.clear()

        for folder in SCAN_DIRS:
            if not folder.exists():
                continue
            for root, _, files in os.walk(folder):
                for f in files:
                    path = Path(root) / f
                    self.scanned.append(path)
                    log(f"Escaneando: {path}")

                    if path.suffix.lower() in DANGEROUS_EXT:
                        self.suspicious.append(path)
                        log(f"⚠ SUSPEITO: {path}")

    def quarantine(self, log):
        moved = 0
        for f in self.suspicious:
            try:
                shutil.move(str(f), QUARANTINE / f.name)
                log(f"📦 Quarentena: {f}")
                moved += 1
            except:
                pass
        return moved

# ================= UI =================
class ERP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🦊 Fox Security ERP")
        self.geometry("1100x650")
        self.configure(bg="#0b1220")

        # Scanner
        self.scanner = Scanner()

        # Matrix effect flag
        self.matrix_running = False

        # Tema Matrix
        self.matrix_canvas = tk.Canvas(self, width=1100, height=650, bg="#0b1220", highlightthickness=0)
        self.matrix_canvas.place(x=0, y=0)

        # Raposa
        self.fox_label = tk.Label(self, text="🦊", font=("Segoe UI", 48), bg="#0b1220", fg="green")
        self.fox_label.pack(pady=5)

        # UI
        self.build_menu()
        self.build_ui()
        self.update_stats()

    # ---------- MENU ----------
    def build_menu(self):
        menubar = Menu(self)
        view_menu = Menu(menubar, tearoff=0)
        view_menu.add_command(label="Mostrar Raposa", command=self.show_fox)
        view_menu.add_command(label="Esconder Raposa", command=self.hide_fox)
        menubar.add_cascade(label="Visual", menu=view_menu)
        self.config(menu=menubar)

    def show_fox(self):
        self.fox_label.pack(pady=5)

    def hide_fox(self):
        self.fox_label.pack_forget()

    # ---------- UI ----------
    def build_ui(self):
        tk.Label(
            self, text="Fox Security • Painel ERP",
            bg="#0b1220", fg="#38bdf8",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        # KPI CARDS
        self.cards = {}
        frame = tk.Frame(self, bg="#0b1220")
        frame.pack()

        for name in ["CPU", "RAM", "DISCO", "ARQUIVOS", "AMEAÇAS"]:
            box = tk.Frame(frame, bg="#020617", width=180, height=80)
            box.pack(side="left", padx=10)
            box.pack_propagate(False)

            tk.Label(box, text=name, bg="#020617", fg="#94a3b8").pack()
            lbl = tk.Label(box, text="--", bg="#020617", fg="#22c55e", font=("Segoe UI", 16))
            lbl.pack()
            self.cards[name] = lbl

        # TABELA ERP
        self.table = ttk.Treeview(self, columns=("arquivo",), show="headings")
        self.table.heading("arquivo", text="Arquivos Escaneados")
        self.table.pack(fill="both", expand=True, padx=20, pady=10)

        # LOG
        self.log = tk.Text(self, height=8, bg="#020617", fg="#00ff41", font=("Consolas", 10))
        self.log.pack(fill="x", padx=20)

        # BOTÕES
        btns = tk.Frame(self, bg="#0b1220")
        btns.pack(pady=10)

        ttk.Button(btns, text="🔍 Escanear", command=self.start_scan).pack(side="left", padx=5)
        ttk.Button(btns, text="📦 Quarentena", command=self.quarantine).pack(side="left", padx=5)

    # ---------- STATS ----------
    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("C:\\").percent

        self.cards["CPU"].config(text=f"{cpu}%")
        self.cards["RAM"].config(text=f"{ram}%")
        self.cards["DISCO"].config(text=f"{disk}%")
        self.cards["ARQUIVOS"].config(text=len(self.scanner.scanned))
        self.cards["AMEAÇAS"].config(text=len(self.scanner.suspicious))

        # Raposa indica saúde
        if cpu < 70 and ram < 80 and len(self.scanner.suspicious) == 0:
            self.fox_label.config(fg="green")
        else:
            self.fox_label.config(fg="red")

        # Atualiza Matrix efeito
        if self.matrix_running:
            self.draw_matrix()

        self.after(2000, self.update_stats)

    # ---------- LOG ----------
    def log_msg(self, msg):
        self.log.insert("end", msg + "\n")
        self.log.see("end")

    # ---------- SCAN ----------
    def start_scan(self):
        self.table.delete(*self.table.get_children())
        self.log.delete("1.0", "end")

        def run():
            self.matrix_running = True
            threading.Thread(target=self.matrix_loop, daemon=True).start()

            self.scanner.scan(self.log_msg)

            self.matrix_running = False
            for f in self.scanner.scanned:
                self.table.insert("", "end", values=(str(f),))
            self.log_msg(f"✔ Scan finalizado: {len(self.scanner.scanned)} arquivos")

        threading.Thread(target=run, daemon=True).start()

    # ---------- QUARENTENA ----------
    def quarantine(self):
        if not self.scanner.suspicious:
            messagebox.showinfo("Quarentena", "Nenhuma ameaça encontrada.")
            return
        total = self.scanner.quarantine(self.log_msg)
        messagebox.showinfo("Quarentena", f"{total} arquivos movidos.")

    # ---------- MATRIX ----------
    def matrix_loop(self):
        while self.matrix_running:
            self.draw_matrix()
            time.sleep(0.05)

    def draw_matrix(self):
        self.matrix_canvas.delete("all")
        for _ in range(100):
            x = random.randint(0, 1100)
            y = random.randint(0, 650)
            char = random.choice("01")
            self.matrix_canvas.create_text(x, y, text=char, fill="#00ff00", font=("Consolas", 12))

# ================= RUN =================
if __name__ == "__main__":
    ERP().mainloop()
