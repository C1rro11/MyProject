import os
import json
from pathlib import Path
iskaggle = os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')
creds = {
    "username": "carrollcheng",
    "key": "a0851bb310396ef125328301133fa467"
}
path = Path('us-patent-phrase-to-phrase-matching')
cred_path = Path('~/.kaggle/kaggle.json').expanduser()

if not cred_path.exists():
    cred_path.parent.mkdir(exist_ok=True)
    cred_path.write_text(json.dumps(creds))
    cred_path.chmod(0o600)

if not iskaggle and not cred_path.exists():
    import zipfile, kaggle
    kaggle.api.competition_download_cli(str(path))
    zipfile.ZipFile(f'{path}.zip').extractall(path)

if iskaggle:
    path = Path('../input/us-patent-phrase-to-phrase-matching')
    print("正在 Kaggle 環境運行，直接使用內建路徑。")
else:
    competition = 'us-patent-phrase-to-phrase-matching'
    path = Path('dataset')/ competition

    if not path.exists():
        path.mkdir(parents = True, exist_ok = True)
        print(f"create directory: {path}")
        import kaggle
        print("downloading...")
        kaggle.api.competition_download_cli(competition)

        zip_file = f'{competition}.zip'
        if os.path.exists(zip_file):
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(path)
            os.remove(zip_file)
            print(f"下載並解壓縮成功！檔案已放入：{path}")
