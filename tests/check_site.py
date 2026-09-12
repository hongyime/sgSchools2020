"""Offline regression checks for the published school directory (no packages)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import hashlib
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.links = []
        self.ids = []
        self.assets = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag in {"script", "img", "iframe"} and "src" in attrs:
            self.assets.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.assets.append(attrs.get("href", ""))


class DirectoryChecks(unittest.TestCase):
    def setUp(self):
        self.page = Page(ROOT / "schools.html")

    def test_no_missing_or_external_automatic_resources(self):
        for asset in self.page.assets:
            url = urlsplit(asset)
            self.assertFalse(url.scheme or url.netloc, asset)
            self.assertFalse(url.path.startswith("/"), asset)
            self.assertTrue((ROOT / url.path).is_file(), asset)
        self.assertFalse(any(tag == "script" for tag, _ in self.page.tags))

    def test_page_has_title_and_native_navigation(self):
        tags = [tag for tag, _ in self.page.tags]
        self.assertIn("title", tags)
        self.assertEqual(tags.count("h1"), 1)
        self.assertEqual(tags.count("main"), 1)
        self.assertEqual(tags.count("section"), 5)
        self.assertEqual(self.page.links[0], "#directory")
        self.assertTrue(any(tag == "nav" and attrs.get("aria-label") for tag, attrs in self.page.tags))

    def test_every_fragment_destination_exists_and_is_unique(self):
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))
        fragments = [link[1:] for link in self.page.links if link.startswith("#")]
        self.assertGreaterEqual(len(set(fragments)), 7)
        for fragment in fragments:
            self.assertIn(fragment, self.page.ids)

    def test_all_archived_destinations_keep_their_original_order(self):
        urls = [link for link in self.page.links if link.startswith("https://")
                and urlsplit(link).hostname not in {"github.com", "www.google.com", "theprawnprojects.hong-yi.me"}]
        self.assertEqual(len(urls), 338)
        self.assertEqual(hashlib.sha256("\n".join(urls).encode()).hexdigest(), "9af9318a494efed1b8822a2ace79b29f3e33202ac8d90459979096db9ec53f83")

    def test_homepage_opens_the_directory_without_javascript(self):
        page = Page(ROOT / "index.html")
        refreshes = [attrs.get("content") for tag, attrs in page.tags
                     if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh"]
        self.assertEqual(refreshes, ["0; url=./schools.html"])
        self.assertIn("./schools.html", page.links)
        self.assertFalse(any(tag == "script" for tag, _ in page.tags))


if __name__ == "__main__":
    unittest.main(verbosity=2)
