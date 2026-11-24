"""The Robot Apology — make.fun bounty entry.

Writes a two-line robot apology to /output/entry.txt (or the path
resolved from the environment). Python 3 standard library only.
"""

import os

ENTRY_TEXT = (
    "I am sorry I watered the fern on your desk with the cold tea left in the kettle, "
    "and by morning its leaves had gone limp.\n"
    "I have learned to check what is in a container before I pour it, so from now on "
    "I will read the label on every jug before I water a plant.\n"
)


def resolve_output_path() -> str:
    """Resolve the output path: ENTRY_OUTPUT, then OUTPUT_DIR /
    MAKEFUN_OUTPUT_DIR joined with 'entry.txt', else /output/entry.txt."""
    env_path = os.environ.get("ENTRY_OUTPUT")
    if env_path:
        return env_path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT

    # Validate: non-empty, 1..400 chars total, exactly two lines.
    if not text or text.strip() == "":
        raise SystemExit("entry text is empty or whitespace-only")
    if not 1 <= len(text) <= 400:
        raise SystemExit(
            "entry text must be 1..400 characters, got %d" % len(text)
        )
    lines = text.splitlines()
    if len(lines) != 2:
        raise SystemExit("entry text must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if line.strip() == "":
            raise SystemExit("entry lines must not be blank")

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)

    # Read back and fail loudly on any mismatch.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verification failed: file content differs from entry text")

    print("Wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
