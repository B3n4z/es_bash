#!/usr/bin/env python3
import argparse
from pathlib import Path

def main() -> int: 
    arg = argparse.ArgumentParser()
    
    arg.add_argument("path")
    arg.add_argument("--files", action = argparse.BooleanOptionalAction)
    arg.add_argument("--dir", action = argparse.BooleanOptionalAction)

    args = arg.parse_args()
    
    folder = Path(args.path)
    
    for item in folder.iterdir():
        print(item)
        
if __name__ == "__main__":
    raise SystemExit(main())