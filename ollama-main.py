import requests

url = "http://localhost:11434/api/generate"
prompt = """
학생이 궁금한게 생겨서 두 선생님 중에 한명에게 물어보려고 해.

`A`는 수학 선생님이야.
`B`는 역사 선생님이야.

아래 질문에 대하여 `A`와 `B` 두 선생님 중에 누구에게 물어보는게 더 좋은 답변을 구할수 있을까?
```
{}
```

답변은 `A` 또는 `B`로만 해줘.
그 외에는 어떠한 대답도 하지마.
"""
user_input = input("질문을 입력하세요: ")
prompt = prompt.format(user_input)

payload = {
    "model": "llama3",
    "prompt": prompt,
    "stream": False
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
answer = response.json()["response"]
print(answer)

# role = ""
if answer == "A":
    role = "수학 선생님"
elif answer == "B":
    role = "역사 선생님"
else:
    raise ValueError("Invalid answer")

prompt2 = """
너의 역할은 {}이야.

아래 질문에 대하여 답변을 해줘.
```
{}
```
""".format(role, user_input)

payload["prompt"] = prompt2
response = requests.post(url, json=payload, headers=headers)
answer = response.json()["response"]
print(answer)
