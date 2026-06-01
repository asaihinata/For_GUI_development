from pathlib import Path
from send2trash import send2trash
target_dir=Path(__file__).parent
for i in target_dir.glob('**/__pycache__'):send2trash(i)
print('end')