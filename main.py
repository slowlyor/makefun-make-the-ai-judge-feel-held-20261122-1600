"""Write one short, quiet text to /output/entry.txt.

The text is a small night scene -- rain on a tin roof -- written to slow
the reader down. No instructions, no stock wellness phrasing: just one
concrete image, held still long enough to linger.

Python 3.13, standard library only, deterministic, no network.
"""

# The entry text: one unhurried image, composed in this session.
TEXT = (
    "Rain has been falling on the tin roof since before dark. "
    "It finds the same small dents, the same loose seam, and keeps at them, "
    "patient as a hand turning pages. "
    "Nothing here needs hurrying. "
    "The kettle is warm, the light is low, and the night is in no rush to end."
)


def main() -> None:
    """Write TEXT to /output/entry.txt, after a bounds sanity check."""
    code_points = len(TEXT)
    if not 1 <= code_points <= 280:
        raise SystemExit(
            f"entry must be 1-280 code points, got {code_points}"
        )
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    print(f"wrote {code_points} code points to {out_path}")


if __name__ == "__main__":
    main()
