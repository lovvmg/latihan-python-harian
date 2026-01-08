data = {}
def buat_data (nama,umur, **info):
    data['profil'] = nama,umur
    data['aktivitas'] = []
    data['info']= info

buat_data("abi",19,buah='alpukat')

def tambah_aktivitas(data, *aktivitas):
    for i in aktivitas:
        data['aktivitas'].append(i)

tambah_aktivitas(data, 'baca','belajar','ngoding','belajar')

def aktivitas_unik(data):
    data_unik = set(data['aktivitas'])
    return data_unik

print(data)

def ringkasan(data):
    nama,umur = data['profil']
    aktivitas = data['aktivitas']
    unik = aktivitas_unik(data)
    info = data['info']

    print(f"""
Nama            : {nama}
Umur            : {umur}
Jumlah aktivitas: {len(unik)}
Aktivitas unik  : {unik}
Info tambahan   : {info}
""")

ringkasan(data)
