# sgSchools2020

Live demo: https://hongyime.github.io/sgSchools2020/

![Project screenshot](./screenshot.png)


An archived 2020 collection of Singapore school websites, with the original map reference.

## Description

The directory preserves 338 links collected in 2020 across Primary Schools, Secondary Schools, Junior Colleges, Polytechnics and ITE. School names and destinations may have changed. The archive is not a current or complete official directory; the original destinations and map reference remain available.

## Features

- Link to the original Google Maps collection
- Clickable HTML directory preserving all 338 archived school destinations
- Coverage of all educational levels (Primary, Secondary, JC, Polytechnic, ITE)
- Prawn styling, mobile link wrapping and native category/keyboard navigation
- Standalone HTML with inline CSS; no JavaScript, external fonts, polling or runtime packages

## Technologies Used

- HTML5
- CSS3
- Google Maps (for map visualization)
- GitHub Pages (the existing static host)

## Installation

```bash
# Clone the repository
git clone https://github.com/hongyime/sgSchools2020.git

# Navigate to project directory
cd sgSchools2020
```

No additional dependencies required - simply open `schools.html` in a web browser.

## Usage

```bash
# Open the HTML file in your browser
open schools.html
# or on Windows
start schools.html
```

You can also view the live demos linked below.

## Demo

**Interactive Map:**  
https://www.google.com/maps/d/edit?mid=1_mfutjXbEmxyRA4Cj3XH66z1S79MCG29&usp=sharing

**Web Listing:**  
https://hongyime.github.io/sgSchools2020/schools.html

## Validation and maintenance

Run `python tests/check_site.py` (standard library only). The checks protect the original school-link order, local resource paths, native navigation and the no-JavaScript homepage handoff. The dedicated School directory checks workflow runs on every PR and main update because the shared Node workflow does not cover this static app.

Open `schools.html` directly, or serve the repository with `python -m http.server 8000`. Both work without JavaScript. The GitHub Pages homepage hands off to `schools.html`, which also keeps its existing public URL.

The 2026-09 maintenance repairs presentation and publication; it does not refresh the 2020 dataset or migrate it to Supabase. `maps.txt` and every original school destination are preserved.

## Disclaimer

1. USE AT YOUR OWN DISCRETION
2. FOR EDUCATIONAL PURPOSES ONLY

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
