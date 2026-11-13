#!/usr/bin/env python3
"""把 avatars/expert.jpg.base64 还原成 avatars/expert.jpg。

用法（在仓库根目录执行）:
    python scripts/restore_avatar.py
"""
from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "avatars" / "expert.jpg.base64"
DST = ROOT / "avatars" / "expert.jpg"


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"未找到 {SRC}，请确认已完整 clone 仓库。")
    data = base64.b64decode(SRC.read_text(encoding="ascii").strip(), validate=True)
    DST.write_bytes(data)
    print(f"已还原头像：{DST} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
