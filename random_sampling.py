import json
import random

def sample_hallucination_data(input_file, output_file, sample_size=500):
    """
    할루시네이션 데이터셋에서 지정된 개수만큼 랜덤 샘플링하여 저장합니다.
    """
    try:
        # 1. 데이터 읽기 (JSONL 형식인 경우 각 줄을 읽어 리스트에 저장)
        with open(input_file, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f if line.strip()]

        total_count = len(data)
        print(f"총 {total_count}개의 데이터를 로드했습니다.")

        # 2. 샘플링 개수 결정 (데이터가 요청보다 적으면 전체 사용)
        actual_sample_size = min(sample_size, total_count)
        
        # 3. 랜덤 샘플링 (비복원 추출)
        sampled_data = random.sample(data, actual_sample_size)
        
        # 4. 결과 저장 (보기 편하도록 들여쓰기가 적용된 JSON 형식으로 저장)
        with open(output_file, 'w', encoding='utf-8') as f:
            # JSON 배열 형태로 저장하고 싶을 때
            json.dump(sampled_data, f, ensure_ascii=False, indent=4)
            
            # 만약 다시 원래와 같은 JSONL(줄바꿈) 형식으로 저장하고 싶다면 아래 주석 해제
            # for entry in sampled_data:
            #     f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"성공적으로 {actual_sample_size}개의 데이터를 '{output_file}'에 저장했습니다.")

    except FileNotFoundError:
        print(f"에러: '{input_file}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

# --- 실행 부분 ---
# 입력 파일명과 출력 파일명을 본인의 파일명에 맞게 수정하세요.
input_filename = 'DiaHalu_Bench.jsonl'  # 원본 파일명
output_filename = 'DiaHalu_Bench_Sampled.jsonl'      # 저장할 파일명

sample_hallucination_data(input_filename, output_filename, 10)