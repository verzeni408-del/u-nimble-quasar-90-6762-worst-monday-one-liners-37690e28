"""Worst Monday One-Liners entry writer."""

import os

PART_A = "I rescheduled my human's Monday standup to a message like he asked, "
PART_B = "then sent the message to the whole company with his salary in it."

ENTRY = PART_A + PART_B


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
