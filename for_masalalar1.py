# # 1
# print("1 dan 10 gacha sonlar")
# for i in range(10+1):
#     print(i)
# # 2
# print("Do'stlarim :")
# ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
# for ism in ismlar:
#     print(f"Salom , {ism}!")
# # 3
# print("1 dan 100 gacha juft sonlar")
# for i in range(2,100+1,2):
#     print(i)
# # 4
# yigindi = 0
# for i in range(1 , 51):
#     yigindi += i
# print(yigindi)
# # 5
# matn = input("Matinni kiriting : ")
# ozgaruvchi = 0
# for x in matn:
#     ozgaruvchi += 1
# print(f"Matn uzunligi : {ozgaruvchi}")
# # 6
# bosh = []
# for y in range(1,51):
#     if y % 3 == 0:
#         bosh += [y]
# print(bosh)
# # 7
# f_m = input("Matnni kiriting : ")
# u_h = "aeiouAEIOU"
# u_s = 0
# for y in f_m:
#     if y in u_h:
#         u_s += 1
# print(f"\nJami unli harflar: {u_s}")
# # 8
# sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
# ozgaruvchi1 = sonlar[0]
# for h in sonlar:
#     if h > ozgaruvchi1:
#         ozgaruvchi1 = h
#         print(f"Yangi eng katta son: {h}")
# print(ozgaruvchi1)
# # 9
# f_s_s = int(input("Sonlarni kiriting : "))
# f_s_s2 = str(f_s_s)
# yigindi2 = 0 
# for b in f_s_s2:
#     yigindi2 += int(b)
# print(yigindi2)
# # 10
# f_ss = int(input("Sonni kiriting : "))
# g = 1
# if f_ss == 0 or f_ss == 1:
#     print(1)
# elif f_ss > 1 :
#     for u in range(1 ,f_ss +1):
#         g *= u
# else:
#     print("FAktorial manfiy sonlar uchun aniqlanmagan")
# print(g)
# # 11
# print("\n" + "=" * 60)
# print("JADVAL SHAKLIDAGI KO'PAYTIRISH JADVALI (1-10)")
# print("=" * 60)
# print("   |", end="")
# for i in range(1, 11):
#     print(f"{i:4}", end="")
# print("\n" + "-" * 60)
# for i in range(1, 11):                   
#     print(f"{i:2} |", end="")            
#     for j in range(1, 11):               
#         print(f"{i*j:4}", end="")        
#     print()                              
# # 12
# n = 5
# for i in range( 0 , n+1 , 1):               
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
# # 13
# a = 0
# b = 1
# for t in range(0 , 10):
#     print(a , end=" ")
#     a , b = b , a + b
# # 14
# for t_y in range(2 , 100):
#     tub = 1
#     for y_t in range(2 , t_y -1):
#         if t_y % y_t == 0:
#             tub = 0
#             break
#     if tub:
#         print(t_y)
# # 15
# soat = 0
# for v in range(0,24):
#     for h in range(0,60):
#         for w in range(0,60):
#             print(f"{v:02d}:{h:02d}:{w:02d}")
#             soat+=1
# print(f"Jami : {soat} ta vaqt")















