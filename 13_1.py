import math
def calculate_friis_with_input():
 print("--- 14. Friis Formula Calculator ---")
 print("아래 항목에 값을 입력하고 Enter를 누르세요.\n")

 # 사용자로부터 값을 직접 입력받음 (float형으로 변환)
 f = float(input("f: frequency (Hz) 입력: "))
 pt = float(input("pt: tx power (dBm) 입력: "))
 gt = float(input("gt: tx antenna gain (dB) 입력: "))
 gr = float(input("gr: rx antenna gain (dB) 입력: "))
 r = float(input("r: tx-rx distance (m) 입력: "))
 # 상수 및 파장 계산
 c = 3e8
 lam = c / f
 # 단위 변환
 pt_w = (10 ** (pt / 10)) * 0.001
 gt_lin = 10 ** (gt / 10)
 gr_lin = 10 ** (gr / 10)
 # 1. eirp 계산
 eirp = pt_w * gt_lin

 # 2. pd 계산
 pd = eirp / (4 * math.pi * (r ** 2))

 # 3. fsL 계산
 fsL = 20 * math.log10((4 * math.pi * r) / lam)

 # 4. ae 계산
 ae = (lam ** 2 / (4 * math.pi)) * gr_lin

 # 5. pr 계산
 pr = pd * ae

 # 6. prdbm 계산
 prdbm = 10 * math.log10(pr / 0.001)
 # 결과 출력
 print("\n[Output]")
 print(f"eirp: {eirp:.4e} W")
 print(f"pd: {pd:.4e} W/m2")
 print(f"fsL: {fsL:.4f} dB")
 print(f"ae: {ae:.4e} m2")
 print(f"pr: {pr:.4e} W")
 print(f"prdbm: {prdbm:.4f} dBm")
if __name__ == "__main__":
 calculate_friis_with_input()
