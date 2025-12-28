#!/usr/bin/env python3
"""API Docs Ouija Board - When the docs are ghosts, summon answers."""

import random
import sys
from datetime import datetime

class OuijaBoard:
    """Spiritual guidance for undocumented APIs. More reliable than Stack Overflow."""
    
    def __init__(self):
        self.responses = [
            "Try adding 'mode=debug' to the query params",
            "The API expects snake_case but you're sending camelCase",
            "Add a trailing slash. Or remove it. Flip a coin.",
            "It works with curl but not Python. Obviously.",
            "The rate limit is 3 requests per lunar cycle",
            "The 'id' field is actually called 'identifier' in production",
            "The example uses XML but they only accept JSON now",
            "Authentication changed from Bearer to Basic last Tuesday",
            "The docs show v1 but you're hitting v2 (or vice versa)",
            "It's a timezone issue. It's always a timezone issue.",
            "The field is required but also deprecated. Good luck.",
            "Try setting 'Content-Type' to 'application/octet-stream'",
            "The API returns 200 but the data is in the headers",
            "The pagination cursor is base64 encoded. Obviously."
        ]
    
    def ask(self, question):
        """Ask the spirits of deprecated endpoints."""
        print(f"\n🔮 Ouija Board consulted at {datetime.now().strftime('%H:%M:%S')}")
        print(f"📝 Your question: {question}")
        print(f"👻 The spirits whisper: {random.choice(self.responses)}")
        print("💀 Accuracy: Same as the original docs (≈42%)")


def main():
    """Main séance. No candles needed, just caffeine."""
    board = OuijaBoard()
    
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("What API mystery troubles you? ")
    
    board.ask(question)
    print("\n⚰️  If that doesn't work, try the time-honored tradition of...\n")
    print("1. Reading the source (if open)")
    print("2. Checking network traffic")
    print("3. Yelling at the vendor's support portal")
    print("4. Rewriting the entire integration (last resort)")

if __name__ == "__main__":
    main()
