import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests
from urllib.parse import quote
from PIL import Image
from io import BytesIO

# ---- SYSTEMS MAPPING ----
systems = {
    "Amstrad CPC": {
        "libretro": "Amstrad_-_CPC",
        "muos": "Amstrad"
    },
    "Atari 2600": {
        "libretro": "Atari_-_2600",
        "muos": "Atari 2600"
    },
    "Atari 5200": {
        "libretro": "Atari_-_5200",
        "muos": "Atari 5200"
    },
    "Atari 7800": {
        "libretro": "Atari_-_7800",
        "muos": "Atari 7800"
    },
    "Atari Jaguar": {
        "libretro": "Atari_-_Jaguar",
        "muos": "Atari Jaguar"
    },
    "Atari Lynx": {
        "libretro": "Atari_-_Lynx",
        "muos": "Atari Lynx"
    },
    "Atari ST": {
        "libretro": "Atari_-_ST",
        "muos": "Atari ST-STE-TT-Falcon"
    },
    "Bandai WonderSwan": {
        "libretro": "Bandai_-_WonderSwan",
        "muos": "Bandai WonderSwan-Color"
    },
    "Bandai WonderSwan Color": {
        "libretro": "Bandai_-_WonderSwan_Color",
        "muos": "Bandai WonderSwan-Color"
    },
    "ColecoVision": {
        "libretro": "Coleco_-_ColecoVision",
        "muos": "ColecoVision"
    },
    "Commodore 64": {
        "libretro": "Commodore_-_64",
        "muos": "Commodore C64"
    },
    "Commodore Amiga": {
        "libretro": "Commodore_-_Amiga",
        "muos": "Commodore Amiga"
    },
    "DOS": {
        "libretro": "DOS",
        "muos": "DOS"
    },
    "Game and Watch": {
        "libretro": "Handheld_Electronic_Game",
        "muos": "Handheld Electronic - Game and Watch"
    },
    "MSX": {
        "libretro": "Microsoft_-_MSX",
        "muos": "Microsoft - MSX"
    },
    "MSX2": {
        "libretro": "Microsoft_-_MSX2",
        "muos": "Microsoft - MSX"
    },
    "NEC PC Engine": {
        "libretro": "NEC_-_PC_Engine_-_TurboGrafx_16",
        "muos": "NEC PC Engine"
    },
    "NEC PC Engine CD": {
        "libretro": "NEC_-_PC_Engine_-_TurboGrafx_CD",
        "muos": "NEC PC Engine CD"
    },
    "NEC PC Engine SuperGrafx": {
        "libretro": "NEC_-_PC_Engine_SuperGrafx",
        "muos": "NEC PC Engine SuperGrafx"
    },
    "Game Boy": {
        "libretro": "Nintendo_-_Game_Boy",
        "muos": "Nintendo Game Boy"
    },
    "Game Boy Color": {
        "libretro": "Nintendo_-_Game_Boy_Color",
        "muos": "Nintendo Game Boy Color"
    },
    "Game Boy Advance": {
        "libretro": "Nintendo_-_Game_Boy_Advance",
        "muos": "Nintendo Game Boy Advance"
    },
    "Nintendo": {
        "libretro": "Nintendo_-_Nintendo_Entertainment_System",
        "muos": "Nintendo NES-Famicom"
    },
    "Super Nintendo": {
        "libretro": "Nintendo_-_Super_Nintendo_Entertainment_System",
        "muos": "Nintendo SNES-SFC"
    },
    "Virtual Boy": {
        "libretro": "Nintendo_-_Virtual_Boy",
        "muos": "Nintendo Virtual Boy"
    },
    "Nintendo DS": {
        "libretro": "Nintendo_-_Nintendo_DS",
        "muos": "Nintendo DS"
    },
    "Nintendo 64": {
        "libretro": "Nintendo_-_Nintendo_64",
        "muos": "Nintendo N64"
    },
    "Nintendo GameCube": {
        "libretro": "Nintendo_-_GameCube",
        "muos": "Nintendo GameCube"
    },
    "Nintendo Wii": {
        "libretro": "Nintendo_-_Wii",
        "muos": "Nintendo Wii"
    },
    "Philips CD-i": {
        "libretro": "Philips_-_CD-i",
        "muos": "Philips CDi"
    },
    "SEGA 32X": {
        "libretro": "Sega_-_32X",
        "muos": "Sega 32X"
    },
    "SEGA CD": {
        "libretro": "Sega_-_Mega-CD_-_Sega_CD",
        "muos": "Sega Mega CD - Sega CD"
    },
    "SEGA Master System": {
        "libretro": "Sega_-_Master_System_-_Mark_III",
        "muos": "Sega Master System"
    },
    "SEGA Mega Drive/Genesis": {
        "libretro": "Sega_-_Mega_Drive_-_Genesis",
        "muos": "Sega Mega Drive - Genesis"
    },
    "SEGA Saturn": {
        "libretro": "Sega_-_Saturn",
        "muos": "Sega Saturn"
    },
    "SEGA Dreamcast": {
        "libretro": "Sega_-_Dreamcast",
        "muos": "Sega Dreamcast"
    },
    "SEGA Game Gear": {
        "libretro": "Sega_-_Game_Gear",
        "muos": "Sega Game Gear"
    },
    "Atomiswave": {
        "libretro": "Atomiswave",
        "muos": "Sega Atomiswave Naomi"
    },
    "SEGA Naomi": {
        "libretro": "Sega_-_Naomi",
        "muos": "Sega Atomiswave Naomi"
    },
    "ZX Spectrum": {
        "libretro": "Sinclair_-_ZX_Spectrum",
        "muos": "Sinclair ZX Spectrum"
    },
    "SNK Neo Geo": {
        "libretro": "SNK_-_Neo_Geo",
        "muos": "SNK Neo Geo"
    },
    "SNK Neo Geo CD": {
        "libretro": "SNK_-_Neo_Geo_CD",
        "muos": "SNK Neo Geo CD"
    },
    "SNK Neo Geo Pocket": {
        "libretro": "SNK_-_Neo_Geo_Pocket",
        "muos": "SNK Neo Geo Pocket - Color"
    },
    "SNK Neo Geo Pocket Color": {
        "libretro": "SNK_-_Neo_Geo_Pocket_Color",
        "muos": "SNK Neo Geo Pocket - Color"
    },
    "PS1": {
        "libretro": "Sony_-_PlayStation",
        "muos": "Sony PlayStation"
    },
    "PS2": {
        "libretro": "Sony_-_PlayStation_2",
        "muos": "Sony PlayStation 2"
    },
    "PSP": {
        "libretro": "Sony_-_PlayStation_Portable",
        "muos": "Sony PlayStation Portable"
    },
    "Sony PlayStation 3": {
        "libretro": "Sony_-_PlayStation_3",
        "muos": "Sony PlayStation 3"
    },
    "Sony PlayStation Vita": {
        "libretro": "Sony_-_PlayStation_Vita",
        "muos": "Sony PlayStation Vita"
    },
    "3DO": {
        "libretro": "The_3DO_Company_-_3DO",
        "muos": "The 3DO Company - 3DO"
    },
    "FBNeo - Arcade": {
        "libretro": "FBNeo_-_Arcade_Games",
        "muos": "Arcade"
    },
    "MAME": {
        "libretro": "MAME",
        "muos": "Arcade"
    },
    "Magnavox - Odyssey2": {
        "libretro": "Magnavox_-_Odyssey_2",
        "muos": "Odyssey2 - VideoPac"
    }
}

GITHUB_COMMIT = "00498a7f6db86bc45146b835ba1aeed58a1a1fe5"

extensions = ('.zip', '.7z', '.nes', '.sfc', '.smc', '.gba', '.gbc', '.gb', '.n64', '.z64', '.v64', '.bin', '.iso', '.chd', '.rom', '.mgw', '.nds', '.vb', '.p8', '.32x', '.sms', '.md', '.ngc', '.wsc', '.ws', '.dsk', '.tap', '.z80')

# --- UTILS ___
def download_libretro_thumbnail(libretro_folder, art_type, rom_name):
    filename = f"{rom_name}.png"
    encoded_filename = quote(filename, safe="")  # full encoding
    url = f"https://raw.githubusercontent.com/libretro-thumbnails/{libretro_folder}/{GITHUB_COMMIT}/{art_type}/{encoded_filename}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None
    
def resize_image(image_bytes, width=300):
    img = Image.open(BytesIO(image_bytes))
    w_percent = width / float(img.size[0])
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size), Image.LANCZOS)
    output = BytesIO()
    img.save(output, format="PNG")
    return output.getvalue()
    
def save_image(image_bytes, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(image_bytes)
        
def get_rom_files(roms_folder, extensions):
    roms = []
    for root, _, files in os.walk(roms_folder):
        for f in files:
            if f.lower().endswith(extensions) and not f.startswith("._"):
                roms.append(f)
    return roms

# --- SCRAPER LOGIC ---
def run_scraper(roms_folder, system_key, output_mode, progress_callback=None, muos_root=None):
    libretro_folder = systems[system_key]["libretro"]
    muos_folder = systems[system_key]["muos"]
    
    if output_mode == "muos":
        if not muos_root:
            raise RuntimeError("No MUOS root folder selected.")
        base_output = os.path.join(muos_root, "info", "catalogue", muos_folder)
        output_boxarts = base_output
        output_snaps = base_output
    else:
        output_boxarts = os.path.join(roms_folder, "images", "Boxarts")
        output_snaps = os.path.join(roms_folder, "images", "Screenshots")
        
    rom_files = get_rom_files(roms_folder)
    total = len(rom_files)
    if total == 0:
        raise RuntimeError(f"No ROM files found in {roms_folder} folder.")
    
    failed = []
    for idx, rom in enumerate(rom_files, start=1):
        rom_name, _ = os.path.splitext(rom)
        
        # Download boxart
        boxart_bytes = download_libretro_thumbnail(libretro_folder, "Named_Boxarts", rom_name)
        if boxart_bytes:
            resized = resize_image(boxart_bytes, width=300)
            save_image(resized, os.path.join(output_boxarts, f"{rom_name}.png"))
        else:
            failed.append(f"{rom_name} (Boxart)")
        
        # Download screenshot
        snap_bytes = download_libretro_thumbnail(libretro_folder, "Named_Snaps", rom_name)
        if snap_bytes:
            save_image(snap_bytes, os.path.join(output_snaps, f"{rom_name}.png"))
        else:
            failed.append(f"{rom_name} (Screenshot)")
        
        if progress_callback:
            progress_callback(idx, total, failed)
            
    return failed

# --- GUI CLASS ---
class RAScraperGUI:
    def __init__(self, root):
        self.root = root
        root.title("RetroArch Scraper GUI")
        root.geometry("600x400")
        
        # Variables
        self.roms_path = tk.StringVar()
        self.muos_root_path = tk.StringVar()
        self.selected_system = tk.StringVar()
        self.output_option = tk.StringVar(value="muos")
        self.progress = tk.IntVar(value=0)
        self.progress_text = tk.StringVar(value="")
        
        # ROMs folder
        tk.Label(root, text="ROMs Folder:").pack(anchor="w", padx=10, pady=(10,0))
        rom_frame = tk.Frame(root)
        rom_frame.pack(fill="x", padx=10)
        tk.Entry(rom_frame, textvariable=self.roms_path).pack(side="left", fill="x", expand=True)
        tk.Button(rom_frame, text="Browse", command=self.browse_roms).pack(side="right")
        
        # MUOS root folder
        tk.Label(root, text="MUOS Root Folder (only needed if MUOS output selected):").pack(anchor="w", padx=10, pady=(10,0))
        muos_frame = tk.Frame(root)
        muos_frame.pack(fill="x", padx=10)
        tk.Entry(muos_frame, textvariable=self.muos_root_path).pack(side="left", fill="x", expand=True)
        tk.Button(muos_frame, text="Browse", command=self.browse_muos).pack(side="right")
        
        # System dropdown
        tk.Label(root, text="Select System:").pack(anchor="w", padx=10, pady=(10,0))
        systems_list = list(systems.keys())
        self.selected_system.set(systems_list[0])
        tk.OptionMenu(root, self.selected_system, *systems_list).pack(fill="x", padx=10)
        
        # Output options
        tk.Label(root, text="Where should artwork be saved?").pack(anchor="w", padx=10, pady=(10,0))
        output_frame = tk.Frame(root)
        output_frame.pack(fill="w", padx=20)
        tk.Radiobutton(output_frame, text="MUOS-compatible folder (MUOS/info/catalogue/{system})", variable=self.output_option, value="muos").pack(anchor="w")
        tk.Radiobutton(output_frame, text="Within root ROMs folder (/images/Boxarts & /images/Screenshots)", variable=self.output_option, value="roms").pack(anchor="w")
        
        # Progress bar and label
        self.progress_bar = ttk.Progressbar(root, maximum=100, variable=self.progress)
        self.progress_bar.pack(fill="x", padx=10, pady=(15,5))
        tk.Label(root, textvariable=self.progress_text).pack()
        
        # Run button
        self.btn_run = tk.Button(root, text="Run Scraper", bg="green", fg="white", command=self.run_scraper_thread)
        self.btn_run.pack(pady=15, ipadx=10, ipady=5)
        
    def browse_roms(self):
        path = filedialog.askdirectory()
        if path:
            self.muos_root_path.set(path)
            
    def browse_muos(self):
        path = filedialog.askdirectory()
        if path:
            self.muos_root_path.set(path)
            
    def update_progress(self, current, total):
        percent = int((current / total) * 100)
        self.progress.set(percent)
        self.progress_text.set(f"Processing {current} of {total} ROMs...")
        
    def run_scraper_thread(self):
        roms_folder = self.roms_path.get().strip()
        muos_root = self.muos_root_path.get().strip()
        system_key = self.selected_system.get()
        output_mode = self.output_option.get()
        
        if not roms_folder:
            messagebox.showwarning("Missing input", "Please select a ROMs folder.")
            return
        
        if output_mode == "muos" and not muos_root:
            messagebox.showwarning("Missing input", "Please select your MUOS root folder.")
            return
        
        self.btn_run.config(state="disabled")
        self.progress.set(0)
        self.progress_text.set("Starting...")
        
        def task():
            try:
                failed = run_scraper(roms_folder, system_key, output_mode, self.update_progress, muos_root)
                self.progress_text.set("Done!")
                if failed:
                    messagebox.showwarning("Completed with missing images", "Some images could not be found:\n" + "\n".join(failed))
                else:
                    messagebox.showinfo("Completed", "All images have been downloaded.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                self.btn_run.config(state="normal")
                
        threading.Thread(target=task, daemon=True).start()
        
# ---  RUN APP ---

def main():
    root = tk.Tk()
    app = RAScraperGUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()