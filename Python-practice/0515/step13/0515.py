ur_name = input("Please input your name (at least 8 characters)>>>")
if len(ur_name) < 8:
    print("too short you wrote!")
else:
    print("Thanks for kind man:)")

if "5" in "12345":
    print("include 5 at 文字列")  # 文字列
if 5 in (1, 2, 3, 4, 5):
    print("include 5 at タプル")  # タプル
if 5 in [1, 2, 3, 4, 5]:
    print("include 5 at リスト")  # リスト
if 5 in {1, 2, 3, 4, 5}:
    print("include 5 at 集合")  # 集合
if 5 in {5: "ご"}:
    print("include 5 at 辞書")  # 辞書

nums1 = [1, 2, 3, 4, 5]
nums2 = nums1.copy()
print(nums1 == nums2)
print(nums1 is nums2)
ns1 = [1, 2, 3]  # truea
ns2 = [1, 2, 3]  # false
print(ns1 is ns2)  # false

urname = input("Please input your name (betweeen 8 and 12 chars)>>>")
if len(urname) < 8 or len(urname) > 12:
    print("Are you kidding me? damn")
else:
    print("gotcha!thanks:)")

urn = input("Please input your name (betweeen 8 and 12 chars)>>>")
name_len = len(urn)
if name_len < 8 or name_len > 12:
    print("Are you kidding me? damn")
else:
    print("gotcha!thanks:)")

lista = []
if len(lista) != 0:
    print("not empty")
else:
    print("empty!")

listb = []
if listb:
    print("not empty")
else:
    print("empty!!!")

ct = 13
if ct < 12:
    print("GM")
elif ct < 14:
    print("HOWLOW!?")
else:
    print("GAN")

n = ""
a = 0
if n and a:
    print("OK")
elif n:
    print("empty a")
elif a:
    print("empty n")
else:
    print("both empty")
