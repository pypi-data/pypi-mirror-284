from bs4 import BeautifulSoup
import requests

def ekstraksi_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        content = requests.get('https://bmkg.go.id', headers=headers)
        content.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error dalam melakukan request: {e}")
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('title')
        title = result.text

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        jam = None
        tanggal = None
        ls = None
        bt = None
        magnitudo = None
        kedalaman = None
        lokasi = None
        skala = None

        for res in result:

            if i == 0:

                waktu = res.text.split(', ')
                jam = waktu[1]
                tanggal = waktu[0]

            elif i == 1:
                magnitudo = res.text

            elif i == 2:
                kedalaman = res.text

            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]

            elif i == 4:
                lokasi = res.text

            elif i == 5:
                skala = res.text

            i += 1

        hasil = {
            'title': title,
            'waktu': {'jam': jam, 'tanggal': tanggal},
            'magnitudo': magnitudo,
            'kedalaman': kedalaman,
            'koordinat': {'ls': ls, 'bt': bt},
            'lokasi': lokasi,
            'skala': skala
        }

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("[[[Data Tidak Ditemukan]]]")
        return
    print(f"{result['title']}")
    print(f"Waktu : {result['waktu']['jam']} {result['waktu']['tanggal']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : {result['koordinat']['ls']}, {result['koordinat']['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Skala : {result['skala']}")

if __name__ == '__main__':
    print("(((((((((Aplikasi Utama)))))))))")
    result = ekstraksi_data()
    tampilkan_data(result)