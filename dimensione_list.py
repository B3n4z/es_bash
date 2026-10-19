#!/usr/bin/env python3
import argparse
from pathlib import Path

def main() -> int: 
    dimensione = argparse.ArgumentParser()
    
    dimensione.add_argument("dimensione", type=int)
    only_dim = dimensione.parse_args()

    for item in Path.home().rglob("*"):
        if item.is_file() and item.stat().st_size >= (only_dim.dimensione * 1000): 
            print (item)
    
    
if __name__ == "__main__":
    raise SystemExit(main())