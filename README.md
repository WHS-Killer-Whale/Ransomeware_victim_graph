# Ransomware_victim_graph
Python Pandas, Matplotlib를 활용한 랜섬웨어 피해자 시각화 툴


## 사용법
우선 엑셀 파일을 기반으로 csv 파일이 필요합니다.<br>
csv 파일의 column으로 [’VICTIM’, ’GANG’, ‘DATE’, ‘NATION’] 4 가지 정보를 그래프화 합니다.<br>
csv 파일의 이름을 sort_data.csv 라고 지은 후 같은 경로에서 graph.py 를 실행합니다.
```
python graph.py
python3 graph.py
```

## Code Review


```
def show_by_nation(data):
    ...


def show_by_date(data):
    ...


def show_by_gang(data):
    ...
```

위 세 가지 함수는 차례대로 국가별, 월별, 그룹별로 피해 발생 횟수를 그래프화하는 함수입니다.

```
def show_by_nation(data):
    # 그래프 크기
    plt.figure(figsize=(10, 10))
    sorted_data = data.sort_values(by="NATION")
    value_counts = sorted_data["NATION"].value_counts().head(10)

    value_counts.plot.pie(autopct="%1.1f%%")

    # 그래프 제목과 라벨 추가
    plt.title("Ransomware Damage Statistics")
    plt.xlabel("Nation")
    plt.ylabel("Count")
    plt.xticks(rotation=45, fontsize=8)

    # 그래프 저장
    plt.savefig("nation_pie.png")
    plt.clf()
```

plt 객체를 이용해서 디자인을 변경, 크기를 조절할 수 있습니다.<br>
또한 <em>value_counts = sorted_data["NATION"].value_counts().head(10)</em> 는 정렬된 상위 10개의 값을 가져오는 것으로, top 10을 추출하는 과정입니다.
<em>.head(10)</em>을 생략하면 top 10 대신 모든 데이터를 받아볼 수 있습니다.


