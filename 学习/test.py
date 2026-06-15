from pathlib import Path
import json

path = Path('demo_text.txt')

if __name__ == "__main__":
    if path.exists():
        print(f"Hello {path.read_text()}")
    else:
        name = str(input("what is your name?"))
        path.write_text(name)

# path.unlink()  # 删除路径文件
