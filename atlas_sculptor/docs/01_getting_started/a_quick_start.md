# 🚀 Quick Start - Atlas Sculptor 1.0.0 - Maya

Welcome to **Atlas Sculptor**, the open-source Maya Sculptor tool designed for artists and riggers who want full control over alembic files with a clean, PySide6-based interface.

---

## ⚙️ Installation

### 🧩 Automatic Setup (Recommended) 

1. **Download** or clone the `atlas_sculptor` folder to any location on your computer (e.g., `D:/tools/atlas_sculptor/`)
2. **Open Maya** (2020+)
3. **Drag and drop** the file `atlas_sculptor/install.py` directly into your Maya viewport
4. **Restart Maya** to valid the userSetup installation
5. **Click Yes** on the userSetup pop-up 
6. You'll now see a new shelf named **AtlasSculptor** in your Maya shelf bar

✅ *That's it! You're ready to use Atlas Sculptor.*

> **Note:** The tool stays in its original location. The installer only adds it to Maya's Python path.

---

### 🪛 Manual Setup

1. **Copy** the entire `atlas_sculptor/` folder into your Maya scripts directory:

    - **Windows**: `Documents\maya\<version>\scripts\`
    - **macOS**: `~/Library/Preferences/Autodesk/maya/<version>/scripts/`
    - **Linux**: `~/maya/<version>/scripts/`

2. **Copy icons folder** (atlas_sculptor_icons): `atlas_sculptor/setup/icons/` → `Documents/maya/<version>/prefs/icons/`
3. **Copy shelf** (shelf_AtlasSculptor.mel): `atlas_sculptor/setup/shelves/` → `Documents/maya/<version>/prefs/shelves/`
4. **Restart Maya**
5. You'll now see the **AtlasSculptor** shelf in your Maya shelf bar

✅ *That's it! You're ready to use Atlas Sculptor.*

---

### 💡 Pro tips

Launch Atlas Sculptor from Maya's Script Editor:
```python
pass
```

 For development (with auto-reload):
```python
pass
```

---

## 🧭 Interface Overview

After launching, the main dialog of Atlas Sculptor appears with one window:

| Tool | Description |
|------|-------------|
| foo  | foo         |