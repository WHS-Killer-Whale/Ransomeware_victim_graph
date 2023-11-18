import pandas as pd
import matplotlib.pyplot as plt

date_offset = "2023-"


def define_plt():
    plt.tight_layout()


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


def show_by_date(data):
    # 그래프 크기
    plt.figure(figsize=(10, 10))
    sorted_data = data.sort_values(by="DATE")
    result = {
        "2023-01": 0,
        "2023-02": 0,
        "2023-03": 0,
        "2023-04": 0,
        "2023-05": 0,
        "2023-06": 0,
        "2023-07": 0,
        "2023-08": 0,
        "2023-09": 0,
        "2023-10": 0,
        "2023-11": 0,
        "2023-12": 0,
    }
    month = 1
    for date in sorted_data["DATE"]:
        offset = date_offset + str(month).zfill(2)
        if date.startswith(offset):
            result[offset] += 1
        else:
            while month <= 12 and not date.startswith(offset):
                month += 1
                offset = date_offset + str(month).zfill(2)
            if month <= 12:
                result[offset] += 1

    plt.pie(list(result.values()), autopct="%.1f%%")
    plt.legend(list(result.keys()))
    plt.title("Ransomware Damage Statistics")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.xticks(rotation=45, fontsize=8)

    # 그래프 저장
    plt.savefig("month.png")
    plt.clf()


def show_by_gang(data):
    # 그래프 크기
    plt.figure(figsize=(10, 10))

    sorted_data = data.sort_values(by="GANG")
    value_counts = sorted_data["GANG"].value_counts().head(10)
    value_counts.plot.pie(autopct="%1.1f%%")

    # 그래프 제목과 라벨 추가
    plt.title("Ransomware Damage Statistics")
    plt.xlabel("GANG")
    plt.ylabel("Count")
    plt.xticks(rotation=45, fontsize=8)

    # 그래프 저장
    plt.savefig("gang_pie.png")
    plt.clf()


def main():
    # CSV 파일 경로
    file_path = "sort_data.csv"

    # CSV 파일을 pandas의 DataFrame으로 읽기
    data = pd.read_csv(file_path, encoding="cp949")

    # 데이터 시각화 - 예시: 선 그래프(Line Plot)
    # x와 y에 해당하는 열을 지정하여 그래프 그리기

    define_plt()
    show_by_nation(data)
    show_by_gang(data)
    show_by_date(data)


if __name__ == "__main__":
    main()
