import random
import requests

datasets = []

for _ in range(5):
    origin = random.sample(range(1, 101), 30)  # 1부터 100까지의 범위에서 30개의 무작위 자연수 선택
    sort = sorted(origin)
    datasets.append({"origin": origin, "sort": sort})

print(datasets)

url = "http://localhost:11434/api/generate"
prompt = """
아래에는 자연수들이 리스트로 나열되어 있어.
```
{}
```
어래 순서대로 수행해줘.

STEP 1. 제공해준 자연수 리스트에서 각 자연수들을 추출해봐.
STEP 2. 위 단계에서 나온 자연수가 제공 받은 리스트에서 누락되지 않았는지 확인해봐.
STEP 3. 자연수들을 오름차순으로 정렬해줘.
STEP 4. 정렬이 올바르게 되었는지 검토해줘. 
STEP 5. 정렬된 자연수 리스트를 제공해줘.

응답은 python의 list format으로 해주고, 그 외에는 어떠한 대답도 하지마.
예시: [1, 2, 3, 4, 5]
"""

payload = {
    "model": "llama3",
    "prompt": prompt,
    "stream": False
}
headers = {
    "Content-Type": "application/json"
}

wrong_cnt = 0
for i, dataset in enumerate(datasets):
    origin = dataset["origin"]
    sort = dataset["sort"]
    payload["prompt"] = prompt.format(origin)

    response = requests.post(url, json=payload, headers=headers)
    answer = response.json()["response"]

    print(answer)
    print(str(sort))
    if answer == str(sort):
        print(f"정답: {origin} -> {answer}")
    else:
        print(f"오답: {origin} -> {answer}")
        wrong_cnt += 1
