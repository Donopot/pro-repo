from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import csv
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "site" / "index.html"
PUBLIC_FILES = [HTML_FILE, ROOT / "README.md", ROOT / "AGENTS.md"]
MARKDOWN_FILES = [ROOT / "README.md", ROOT / "AGENTS.md", *(ROOT / "templates").glob("*.md"), *(ROOT / "demos").glob("*.md")]
CRM_TARGETS = ROOT / "crm" / "agences-cibles.csv"
CRM_MODEL = ROOT / "crm" / "crm-modele.csv"
VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}


class StructureValidator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.ids = set()
        self.internal_links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            if attributes["id"] in self.ids:
                self.errors.append(f"duplicate id: {attributes['id']}")
            self.ids.add(attributes["id"])
        href = attributes.get("href")
        if href and href.startswith("#") and href != "#":
            self.internal_links.append(href[1:])
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_ELEMENTS:
            self.stack.pop()

    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append(f"closing </{tag}> without opening tag")
            return
        expected = self.stack.pop()
        if expected != tag:
            self.errors.append(f"expected </{expected}>, found </{tag}>")


def validate_html(errors):
    parser = StructureValidator()
    parser.feed(HTML_FILE.read_text(encoding="utf-8"))
    parser.close()
    errors.extend(f"site/index.html: {error}" for error in parser.errors)
    errors.extend(f"site/index.html: unclosed <{tag}>" for tag in reversed(parser.stack))
    for anchor in parser.internal_links:
        if anchor not in parser.ids:
            errors.append(f"site/index.html: internal link #{anchor} has no target")


def validate_public_content(errors):
    forbidden = ["[À compléter]", "[JJ/MM/AAAA]", "[Raison sociale]", "[X]"]
    for path in PUBLIC_FILES:
        content = path.read_text(encoding="utf-8")
        for placeholder in forbidden:
            if placeholder in content:
                errors.append(f"{path.relative_to(ROOT)}: public placeholder {placeholder}")

    for path in PUBLIC_FILES:
        content = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if "10 à 20 jours" in content or "10-20 jours" in content:
            errors.append(f"{relative}: obsolete 10-20 day delivery promise")
        if "Maintenance incluse" in content or "maintenance incluse" in content:
            errors.append(f"{relative}: maintenance is incorrectly presented as included")


def validate_links(errors):
    link_pattern = re.compile(r"https?://[^\s\)>\"]+")
    for path in PUBLIC_FILES:
        for url in link_pattern.findall(path.read_text(encoding="utf-8")):
            parsed = urlparse(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{path.relative_to(ROOT)}: invalid URL {url}")


def validate_markdown(errors):
    for path in MARKDOWN_FILES:
        if not re.search(r"^# ", path.read_text(encoding="utf-8"), re.MULTILINE):
            errors.append(f"{path.relative_to(ROOT)}: missing level-one heading")


def read_csv(path, errors):
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            return reader.fieldnames or [], list(reader)
    except (OSError, csv.Error) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid CSV: {exc}")
        return [], []


def validate_crm(errors):
    target_fields, targets = read_csv(CRM_TARGETS, errors)
    required_target_fields = {
        "id", "nom", "email", "telephone", "source_url", "date_collecte",
        "date_verification", "verification_status", "opposition", "opposition_date",
    }
    missing = required_target_fields.difference(target_fields)
    if missing:
        errors.append(f"crm/agences-cibles.csv: missing fields {sorted(missing)}")

    seen_ids = set()
    seen_verified_contacts = set()
    for line_number, row in enumerate(targets, start=2):
        lead_id = row.get("id", "").strip()
        if not lead_id or lead_id in seen_ids:
            errors.append(f"crm/agences-cibles.csv:{line_number}: missing or duplicate id")
        seen_ids.add(lead_id)

        if row.get("verification_status", "").strip().lower() != "verifie":
            errors.append(f"crm/agences-cibles.csv:{line_number}: target is not manually verified")
        if not all(row.get(field, "").strip() for field in ("source_url", "date_collecte", "date_verification")):
            errors.append(f"crm/agences-cibles.csv:{line_number}: target lacks source or verification dates")
        if urlparse(row.get("source_url", "")).scheme not in {"http", "https"}:
            errors.append(f"crm/agences-cibles.csv:{line_number}: source_url must be an HTTP(S) URL")
        contact_key = (row.get("email", "").strip().lower(), row.get("telephone", "").strip())
        if not any(contact_key):
            errors.append(f"crm/agences-cibles.csv:{line_number}: target lacks contact details")
        elif contact_key in seen_verified_contacts:
            errors.append(f"crm/agences-cibles.csv:{line_number}: duplicate verified contact")
        seen_verified_contacts.add(contact_key)

        opposition = row.get("opposition", "").strip().lower()
        if opposition not in {"oui", "non"}:
            errors.append(f"crm/agences-cibles.csv:{line_number}: opposition must be Oui or Non")
        if opposition == "oui" and row.get("statut", "").strip().lower() != "opposition":
            errors.append(f"crm/agences-cibles.csv:{line_number}: opposed target must have Opposition status")

    model_fields, _ = read_csv(CRM_MODEL, errors)
    required_model_fields = {
        "source_url", "date_collecte", "date_information", "opposition",
        "opposition_date", "ne_plus_contacter", "motif_opposition",
    }
    missing = required_model_fields.difference(model_fields)
    if missing:
        errors.append(f"crm/crm-modele.csv: missing fields {sorted(missing)}")


def main():
    errors = []
    validate_html(errors)
    validate_public_content(errors)
    validate_links(errors)
    validate_markdown(errors)
    validate_crm(errors)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
