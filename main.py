import pandas as pd

# 엑셀 파일 경로 지정
file_path = 'upbit.xlsx'

# 엑셀 파일 읽기, 헤더가 없음을 명시
df = pd.read_excel(file_path, header=None)
df[10] = pd.to_datetime(df[0]).dt.strftime('%Y-%m-%d')

# 필요한 컬럼 전처리 ('KRW', ',', 'POLYX' 등 문자 제거)
df[11] = df[8].astype(str).str.replace('KRW', '').str.replace(',', '').astype(int)

# 매수인 경우 8번째 컬럼 값을 음수로 처리
df[12] = df.apply(lambda x: -x[11] if x[3] == '매수' else x[11], axis=1)
print(df)

# 첫 번째 컬럼의 값으로 그룹을 만들고, 조정된 합계의 합계를 계산
grouped_sum_day = df.groupby(10)[12].sum()
# 결과 출력
print(f"Daily:{grouped_sum_day}")

# 첫 번째 컬럼의 값으로 그룹을 만들고, 조정된 합계의 합계를 계산
grouped_sum_coin = df.groupby(1)[12].sum()
# 결과 출력
print(grouped_sum_coin)
print(f"Coin:{grouped_sum_coin}")
# 첫 번째 컬럼의 값으로 그룹을 만들고, 조정된 합계의 합계를 계산
grouped_sum = df[12].sum()
# 결과 출력
print(f"Total:{format(grouped_sum, ',')}")