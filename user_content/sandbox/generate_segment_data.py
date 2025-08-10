import pandas as pd

"""
    poetry run python -m user_content.sandbox.generate_segment_data
"""


if __name__ == "__main__":
    """
        generateするセグメントデータを生成するためのスクリプト
    """
    segment = [
        {"gender": "男性", "play_freq": "週1回以下", "age": "20代"},
        {"gender": "女性", "play_freq": "週1回以下", "age": "20代"},
        {"gender": "男性", "play_freq": "週7回以上", "age": "40代"}
    ]

    pd.DataFrame(segment).to_csv("./data/generate_segment/segment.csv", index=False)