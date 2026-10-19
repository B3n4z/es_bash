#!/usr/bin/env python3
from pathlib import Path

def main() -> int: 
    for item in Path.home().iterdir():
        if item.is_dir():
            print (item)
        
if __name__ == "__main__":
    raise SystemExit(main())