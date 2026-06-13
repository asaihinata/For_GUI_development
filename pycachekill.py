from pathlib import Path

from send2trash import send2trash

for i in Path(__file__).parent.glob("**/__pycache__"):
    send2trash(i)
print("end")
