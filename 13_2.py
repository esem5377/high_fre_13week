import math
def calculate_link_budget_with_input():
 print("--- 15. Link Budget Calculator ---")
 print("아래 항목에 값을 입력하고 Enter를 누르세요.\n")

 # 사용자로부터 값을 직접 입력받음
 pt = float(input("pt: tx power (dBm) 입력: "))

15.
소스코드
import math
def calculate_link_budget_with_input():
 print("--- 15. Link Budget Calculator ---")
 print("아래 항목에 값을 입력하고 Enter를 누르세요.\n")

 # 사용자로부터 값을 직접 입력받음
 pt = float(input("pt: tx power (dBm) 입력: "))
 gt = float(input("gt: tx antenna gain (dB) 입력: "))
 txL = float(input("txL: tx side loss (dB) 입력: "))
 gr = float(input("gr: rx antenna gain (dB) 입력: "))
 r = float(input("r: tx-rx distance (m) 입력: "))
 rxL = float(input("rxL: rx side loss (dB) 입력: "))
 ts = float(input("ts: receiver noise temperature (K) 입력: "))
 b = float(input("b: receiver bandwidth (Hz) 입력: "))
 f = float(input("f: frequency (Hz) 입력: "))
 # 상수 계산
 c = 3e8
 lam = c / f
 k = 1.38e-23 # 볼츠만 상수
 # 1. eirp 계산
 eirp = pt + gt - txL

 # 2. pd 계산
 pd = eirp - 10 * math.log10(4 * math.pi * (r ** 2))

 # 3. ae 계산
 gr_lin = 10 ** (gr / 10)
 ae = (lam ** 2 / (4 * math.pi)) * gr_lin

 # 4. pr 계산
 fsl_db = 20 * math.log10((4 * math.pi * r) / lam)
 pr = eirp - fsl_db + gr

 # 5. sr 계산
 sr = pr - rxL

 # 6. n 계산 (열 잡음)
 n_w = k * ts * b
 n = 10 * math.log10(n_w / 0.001)

 # 7. cnr 계산
 cnr = sr - n
 # 결과 출력
 print("\n[Output]")
 print(f"eirp: {eirp:.4f} dBm")
 print(f"pd: {pd:.4f} dBm/m2")
 print(f"ae: {ae:.4e} m2")
 print(f"pr: {pr:.4f} dBm")
 print(f"sr: {sr:.4f} dBm")
 print(f"n: {n:.4f} dBm")
 print(f"cnr: {cnr:.4f} dB")
if __name__ == "__main__":
 calculate_link_budget_with_input()
