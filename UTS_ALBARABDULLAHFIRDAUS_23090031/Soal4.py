berat_badan = float(input("Masukkan berat badan anda (dalam kg): "))
tinggi_badan = float(input("Masukkan tinggi badan anda (dalam meter): "))

bmi = berat_badan / (tinggi_badan * 2)

print("Indeks massa tubuh anda adalah: ", round(bmi, 8))

if bmi < 18.5:
    print("Kondisi anda tergolong kurus.")
elif bmi >= 18.5 and bmi < 24.9:
    print("Kondisi anda tergolong normal.")
elif bmi >= 25 and bmi < 29.9:
    print("Kondisi anda tergolong gemuk.")
elif bmi > 30:
    print("Kondisi anda tergolong obesitas.")
else:
    print("Kondisi anda tergolong kurus.")
    print("Kondisi anda tergolong normal.")
    print("Kondisi anda tergolong gemuk.")
    print("Kondisi anda tergolong obesitas.")