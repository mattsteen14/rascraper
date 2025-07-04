# 🎮 RetroArch Scraper

[![Contributors](https://img.shields.io/github/contributors/mattsteen14/rascraper.svg?style=for-the-badge)](https://github.com/mattsteen14/rascraper/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/mattsteen14/rascraper.svg?style=for-the-badge)](https://github.com/mattsteen14/rascraper/network/members)
[![Stargazers](https://img.shields.io/github/stars/mattsteen14/rascraper.svg?style=for-the-badge)](https://github.com/mattsteen14/rascraper/stargazers)
[![Issues](https://img.shields.io/github/issues/mattsteen14/rascraper.svg?style=for-the-badge)](https://github.com/mattsteen14/rascraper/issues)
[![MIT License](https://img.shields.io/github/license/mattsteen14/rascraper.svg?style=for-the-badge)](https://github.com/mattsteen14/rascraper/blob/main/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/mattsteen14)

---

[**Explore the docs »**](https://github.com/mattsteen14/rascraper)
[View Demo](https://github.com/mattsteen14/rascraper) ·
[Report Bug](https://github.com/mattsteen14/rascraper/issues/new?labels=bug&template=bug-report---.md) ·
[Request Feature](https://github.com/mattsteen14/rascraper/issues/new?labels=enhancement&template=feature-request---.md)

<details>
  <summary><strong>📚 Table of Contents</strong></summary>

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

</details>

---

## 🚀 About The Project

This is a Python GUI application (run from the terminal) that automatically downloads box art and preview images for your video game ROMs from the [libretro-thumbnails GitHub repository](https://github.com/libretro-thumbnails/libretro-thumbnails).

The app matches your ROM filenames exactly — including metadata like years and publishers — and fetches the corresponding images from a pinned commit on GitHub. It automatically resizes box art images to a width of 300 pixels to fit MUOS catalogue standards, populating the `box` and `preview` subfolders within the MUOS `/info/catalogue` folder structure.

This tool is intended as an alternative to [ScreenScraper](https://www.screenscraper.fr), [Skraper](https://www.skraper.net), and [Scrappy](https://github.com/gabrielfvale/scrappy/releases) — especially for Anbernic RG28XX devices that are not Wi-Fi enabled or Mac users who can’t install Skraper.

### ✨ Features

- Automatic scraping of box and preview images
- Matches ROM filenames to libretro-thumbnails project
- Supports MUOS folder structure and image resizing
- Works offline once downloaded
- Two flexible output options

⬆️ [Back to top](#retroarch-scraper)

---

### 🛠 Built With

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-%3E=2.25.1-green)](https://requests.readthedocs.io/en/latest/)
[![Pillow](https://img.shields.io/badge/Pillow-%3E=8.0.0-yellowgreen)](https://python-pillow.org/)

⬆️ [Back to top](#retroarch-scraper)

---

## 🧰 Getting Started

These instructions will help you set up the project locally.

### ✅ Prerequisites

- An internet connection (to download artwork from GitHub)
- ROMs organized in folders (with filenames that match libretro-thumbnails)
- Knowledge of your system’s MUOS name and libretro-thumbnails folder name

Make sure Python and Pillow are installed:

```bash
python3 --version
pip install pillow
```

---

### 🖥 Installation

1. Clone the repository:

```bash
git clone https://github.com/mattsteen14/rascraper.git
```

2. Navigate into the project folder:

```bash
cd rascraper
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python3 rascraper.py
```

5. Select your **ROMs folder** using the first Browse button.

6. Select the **MUOS root folder** using the second Browse button (this is the MUOS directory on your SD card or computer).

7. Select the **system** from the dropdown. This will map to the correct libretro-thumbnails folder and MUOS `/info/catalogue/{system}` folder.

8. Choose your **output location** using the radio buttons:
   - **MUOS structure**: Saves artwork directly to `MUOS/info/catalogue/{system}/box` and `preview` folders.
   - **ROMs folder**: Creates an `images` folder with `Boxarts` and `Screenshots` subfolders in the ROMs folder.

9. Click **RUN SCRAPER**.

10. Check the folders — artwork should be downloaded and placed correctly.

⬆️ [Back to top](#retroarch-scraper)

---

## 📅 Roadmap

- [x] Plan project
- [x] Write code
- [x] Test with various ROMs and output options
- [x] Version control and GitHub setup
- [ ] Testing and debugging
- [ ] Batch scan and process all subfolders in ROMs root
- [ ] Package as a cross-platform standalone app

👉 See [Issues](https://github.com/mattsteen14/rascraper/issues) for open features and bugs.

⬆️ [Back to top](#retroarch-scraper)

---

## 🤝 Contributing

Contributions are what make open source amazing. If you'd like to help:

1. Fork the repository

2. Create your branch:  

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes:  

```bash
git commit -m "Add some feature"
```

4. Push to GitHub:  

```bash
git push origin feature/YourFeature
```

5. Open a pull request

Or open an issue with the **enhancement** label.

⬆️ [Back to top](#retroarch-scraper)

---

## 📝 License

Distributed under the MIT License.  
See [`LICENSE`](https://github.com/mattsteen14/rascraper/blob/main/LICENSE) for more information.

⬆️ [Back to top](#retroarch-scraper)

---

## 📬 Contact

Matt Steen-Brookes  
📧 [mattsteen14@me.com](mailto:mattsteen14@me.com)  
🐦 [@mattsteen14](https://twitter.com/mattsteen14)  
🔗 [GitHub Repo](https://github.com/mattsteen14/rascraper)

⬆️ [Back to top](#retroarch-scraper)

---

## 🙏 Acknowledgments

- [Mo Ashqar](https://github.com/ashqar) for introducing me to Codecademy
- [Othneil Drew](https://github.com/othneildrew) for the README template
- [Choose an Open Source License](https://choosealicense.com)

⬆️ [Back to top](#retroarch-scraper)