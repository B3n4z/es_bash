#!/usr/bin/env python3
import argparse
from pathlib import Path

def main() -> int: 
    ex = argparse.ArgumentParser()
    
    ex.add_argument("ex")
    exs = ex.parse_args()
    count = 0
    size = 0
    
    for item in Path.home().rglob(f"*{exs.ex}"):
        count += 1
        size += item.stat().st_size
        print (item)
    
    print(f"I tuoi file totali sono: {count}")
    print(f"E pesano: {size / 1000000} mB")
    
if __name__ == "__main__":
    raise SystemExit(main())