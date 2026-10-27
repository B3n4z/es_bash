#!/usr/bin/env python3
import argparse
from pathlib import Path

def main() -> int: 
    arg = argparse.ArgumentParser()
    
    arg.add_argument("arg")
    args = arg.parse_args()
    
    for item in Path.home().iterdir():
        print(int(item.stat().st_size))
        print(int(args.arg * 1000000))
        
    
    
if __name__ == "__main__":
    raise SystemExit(main())