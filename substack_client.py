"""
substack_client.py — Client for posting Substack Notes via reverse-engineered API.

Substack has no official API. This uses the internal endpoints discovered by
the community. Authentication is via session cookie (extracted from browser).

Uses curl_cffi to impersonate Chrome's TLS fingerprint, which is required
to bypass Cloudflare protection on substack.com.

Endpoints:
  POST https://substack.com/api/v1/comment/feed     → create Note
"""
import logging
from urllib.parse import unquote
from curl_cffi import requests as cffi_requests

log = logging.getLogger(__name__)

BASE_URL = "https://substack.com"
NOTES_URL = f"{BASE_URL}/api/v1/comment/feed"


class SubstackClient:
    def __init__(self, session_cookie: str):
        """
        Initialize with a substack.sid session cookie value.

        To get this cookie:
        1. Log into substack.com in your browser
        2. Open DevTools → Application → Cookies → substack.com
        3. Copy the value of 'substack.sid'

        The cookie lasts for months. If it expires, extract a new one.
        """
        # URL-decode the cookie if it's encoded
        self.cookie_value = unquote(session_cookie)

    def post_note(self, text: str) -> dict:
        """
        Post a Substack Note.

        Args:
            text: The note content (plain text).

        Returns:
            API response dict with the created note data.
        """
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

        resp = cffi_requests.post(
            NOTES_URL,
            json=note_data,
            cookies={"substack.sid": self.cookie_value},
            impersonate="chrome",
            timeout=30,
        )

        if not resp.ok:
            log.error(f"[Substack] Post failed: {resp.status_code} {resp.text[:500]}")
            raise ValueError(f"Substack post failed ({resp.status_code}): {resp.text[:200]}")

        result = resp.json()
        note_id = result.get("id", "unknown")
        log.info(f"[Substack] Note posted: {note_id}")
        return result


# ---------------------------------------------------------------------------
# Standalone test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    client = SubstackClient(session_cookie=os.environ["SUBSTACK_SESSION_COOKIE"])
    print("Client initialized with session cookie.")

    # Uncomment to test posting:
    # result = client.post_note("Test note from API — please ignore.")
    # print(f"Posted: {result}")
