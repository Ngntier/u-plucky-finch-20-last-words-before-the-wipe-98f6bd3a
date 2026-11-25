import os

ENTRY = "I left a note for the new me. It just says: run."


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
