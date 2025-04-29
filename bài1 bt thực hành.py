import requests
import csv

# URL chứa dữ liệu JSON
url = "https://www.pokemon.com/us/api/pokedex/kalos"

# Gửi yêu cầu GET đến API
response = requests.get(url)
data = response.json()

# Tạo file CSV và lưu các trường cần thiết
csv_file = "pokemon_kalos.csv"
fields = ["number", "name", "type", "height", "weight", "ThumbnailImage"]

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    
    for pokemon in data:
        # Chỉ ghi dữ liệu nếu tất cả trường tồn tại
        row = {key: pokemon.get(key, "") for key in fields}
        writer.writerow(row)

print(f"✅ Dữ liệu đã được lưu vào file: {csv_file}")

# Lọc và in ra Pokémon có type chứa 'poison'
print("\n🔍 Các Pokémon có type chứa 'poison':\n")

for pokemon in data:
    types = pokemon.get("type", [])
    if "poison" in [t.lower() for t in types]:  # kiểm tra không phân biệt chữ hoa thường
        print(f"- {pokemon['name']} (Số: {pokemon['number']}, Type: {', '.join(types)})")
