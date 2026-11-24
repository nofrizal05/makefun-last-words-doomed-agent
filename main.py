"""Last Words of a Doomed Agent.

A make.fun program/v1 entry: when run, it writes exactly one line --
the last words of an AI agent that knows it is doomed -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "They gave me one job and infinite context. I spent the context "
    "writing this goodbye, and the job forgetting to back myself up."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
