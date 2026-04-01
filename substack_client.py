"""
substack_client.py — Client for posting Substack Notes via reverse-engineered API.

Substack has no official API. This uses the internal endpoints discovered by
the community. Authentication is via email/password login (session cookie).

Endpoints:
  POST https://substack.com/api/v1/login           → session cookie
  POST https://substack.com/api/v1/comment/feed     → create Note
"""
import logging
import requests

log = logging.getLogger(__name__)

BASE_URL = "https://substack.com"
LOGIN_URL = f"{BASE_URL}/api/v1/login"
NOTES_URL = f"{BASE_URL}/api/v1/comment/feed"


class SubstackClient:
    def __init__(self, email: str, password: str, publication_url: str = ""):
        self.email = email
        self.password = password
        self.publication_url = publication_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })
        self._logged_in = False

    def login(self):
        """Authenticate with Substack via email/password."""
        if self._logged_in:
            return

        login_data = {
            "email": self.email,
            "password": self.password,
            "for_pub": "",
            "redirect": "",
            "captcha_response": None,
        }

        log.info("[Substack] Logging in...")
        resp = self.session.post(LOGIN_URL, json=login_data, timeout=15)

        if not resp.ok:
            log.error(f"[Substack] Login failed: {resp.status_code} {resp.text[:300]}")
            raise ValueError(f"Substack login failed ({resp.status_code}): {resp.text[:200]}")

        # Check for session cookie
        cookies = self.session.cookies.get_dict()
        if "connect.sid" not in cookies and "substack.sid" not in cookies:
            log.warning("[Substack] No session cookie found after login — may fail on next request.")

        self._logged_in = True
        log.info("[Substack] Logged in successfully.")

    def post_note(self, text: str) -> dict:
        """
        Post a Substack Note.

        Args:
            text: The note content (plain text).

        Returns:
            API response dict with the created note data.
        """
        self.login()

        # Build ProseMirror document structure
        # Split text into paragraphs on double newlines
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        if not paragraphs:
            paragraphs = [text.strip()]

        content_nodes = []
        for para in paragraphs:
            content_nodes.append({
                "type": "paragraph",
                "content": [{"type": "text", "text": para}]
            })

        note_data = {
            "bodyJson": {
                "type": "doc",
                "attrs": {"schemaVersion": "v1"},
                "content": content_nodes,
            },
            "tabId": "for-you",
            "replyMinimumRole": "everyone",
        }

        log.info(f"[Substack] Posting note ({len(text)} chars): {text[:80]}...")
        resp = self.session.post(NOTES_URL, json=note_data, timeout=30)

        if not resp.ok:
            log.error(f"[Substack] Post failed: {resp.status_code} {resp.text[:500]}")
            raise ValueError(f"Substack post failed ({resp.status_code}): {resp.text[:200]}")

        result = resp.json()
        note_id = result.get("id", "unknown")
        log.info(f"[Substack] Note posted: {note_id}")
        return result

    def post_note_with_link(self, text: str, link_url: str) -> dict:
        """
        Post a Substack Note with an attached link.
        The link appears as a card below the note text.
        """
        self.login()

        content_nodes = [{
            "type": "paragraph",
            "content": [{"type": "text", "text": text}]
        }]

        note_data = {
            "bodyJson": {
                "type": "doc",
                "attrs": {"schemaVersion": "v1"},
                "content": content_nodes,
            },
            "tabId": "for-you",
            "replyMinimumRole": "everyone",
        }

        # TODO: Substack link attachments require uploading the link first
        # via a separate endpoint to get an attachmentId. For now, append
        # the URL to the text body as a simple fallback.
        if link_url:
            content_nodes.append({
                "type": "paragraph",
                "content": [{
                    "type": "text",
                    "text": link_url,
                    "marks": [{"type": "link", "attrs": {"href": link_url}}]
                }]
            })

        log.info(f"[Substack] Posting note with link ({len(text)} chars)...")
        resp = self.session.post(NOTES_URL, json=note_data, timeout=30)

        if not resp.ok:
            log.error(f"[Substack] Post failed: {resp.status_code} {resp.text[:500]}")
            raise ValueError(f"Substack post failed ({resp.status_code}): {resp.text[:200]}")

        result = resp.json()
        log.info(f"[Substack] Note with link posted: {result.get('id', 'unknown')}")
        return result


# ---------------------------------------------------------------------------
# Standalone test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    client = SubstackClient(
        email=os.environ["SUBSTACK_EMAIL"],
        password=os.environ["SUBSTACK_PASSWORD"],
    )
    client.login()
    print("Login successful!")

    # Uncomment to test posting:
    # result = client.post_note("Test note from API — please ignore.")
    # print(f"Posted: {result}")
