import json
import matplotlib.pyplot as plt
from collections import Counter
import ast
import numpy as np

# 1. 모든 카테고리를 순서대로 정의
LINGUISTIC_CATEGORIES = [
    "Factual Error", 
    "Logical Inconsistency", 
    "Pragmatic Violation", 
    "Topic Alignment Failure", 
    "Linguistic Obscurity", 
    "Lexical Pleonasm", 
    "No Error"
]

label_map = {
    "0": "Factual Error",
    "1": "Logical Inconsistency",
    "2": "Pragmatic Violation",
    "3": "Topic Alignment Failure",
    "4": "Linguistic Obscurity",
    "5": "Lexical Pleonasm",
    "None": "No Error"
}

def visualize_hallucination_results(file_path, model):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    original_indices = []
    ling_counts = {cat: 0 for cat in LINGUISTIC_CATEGORIES}

    for item in data:
        # Index 처리
        idx_str = item.get("index", "[]")
        try:
            idx_list = ast.literal_eval(idx_str)
            if idx_list:
                for sub_idx in idx_list:
                    original_indices.append(sub_idx[1])
            else:
                original_indices.append("None/Normal")
        except:
            original_indices.append("Unknown")

        # 새 라벨 처리
        new_label_raw = str(item.get("new_label_linguistic", "None"))
        category_name = label_map.get(new_label_raw, "No Error")
        if category_name in ling_counts:
            ling_counts[category_name] += 1

    # --- 시각화: 새 언어학적 라벨 분포 (논문 스타일 적용) ---
    plt.figure(figsize=(12, 7))
    
    categories = list(ling_counts.keys())
    values = list(ling_counts.values())
    
    # 막대마다 다른 무늬와 색상 적용을 위한 설정
    # 보내주신 이미지의 느낌을 살린 색상 조합입니다.
    colors = ['#E69F8E', '#A2D2EE', '#6D7993', '#F5D061', '#9ED9D3', '#C1A4DE', '#B0B0B0']
    hatches = ['///', '++', 'xx', '||', '..', '--', 'oo']

    bars = plt.bar(categories, values, color=colors, edgecolor='white', linewidth=1)

    # 각 막대에 무늬 직접 입히기
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)

    # 스타일 디테일
    plt.title(f'Distribution of Linguistic Labels ({model})', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Count', fontsize=12, fontweight='bold')
    
    # 가로 그리드 추가 (그림처럼)
    plt.grid(axis='y', linestyle='-', alpha=0.7, color='lightgrey')
    plt.gca().set_axisbelow(True) # 그리드를 막대 뒤로

    # 테두리 정리
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.xticks(rotation=25, ha='right', fontsize=10)
    
    # 데이터 값 표시 (선택 사항)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'distribution_linguistic_stylish_{model}.png', dpi=300)
    plt.show()
    plt.close()

    print(f"[{model}] 시각화가 완료되었습니다.")

# 실행
visualize_hallucination_results('DiaHalu_Bench_relabeled_Gemini-3.1-pro-preview.json', 'Gemini-3.1-pro-preview')