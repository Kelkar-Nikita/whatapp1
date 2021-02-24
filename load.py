import time
from tqdm import tqdm

for _ in tqdm(range(100)):
    desc="loading...."
    ascii=True
    time.sleep(0.1)

print("done..")

