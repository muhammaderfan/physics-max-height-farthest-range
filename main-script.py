from tinggi_maks.tinggi import tinggi as tinggi_maksimum
from jarak_maks.jarak import jarak as jarak_maksimum

kelajuan_awal = float(input("Input Kelajuan Mula-mula Peluru: "))
sudut_elevasi = int(input("Input Derajad Sudut Elevasi: "))
print("Tinggi Maksimum Peluru adalah: ", "{:.2f}".format(tinggi_maksimum(kelajuan_awal, sudut_elevasi)), "meter")
print("Jarak Terjauh Peluru adalah: ", "{:.2f}".format(jarak_maksimum(kelajuan_awal, sudut_elevasi)), "meter")