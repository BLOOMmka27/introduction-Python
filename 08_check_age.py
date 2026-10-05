print("when are u born: ")
year=int(input())
age=float(2026-year)
print(f"ur {age} years old")
if (age<12):
    print("ur a child")
elif(12<age<17):
    print("ur a teenager")
else:
    print("ur an adult")