import requests
from tqdm import tqdm

weight_url = "https://github.com/puneet29/IntelSceneClassification/raw/master/intelmodel.pt"

r = requests.get(weight_url, stream=True)

with open("intelmodel.pt", 'wb') as f:
    for chunk in tqdm(r.iter_content(chunk_size=1024)):

        if chunk:
            f.write(chunk)
