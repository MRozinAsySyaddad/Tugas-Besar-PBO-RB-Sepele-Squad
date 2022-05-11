try:
	import pygame, pygame.locals
except:
	print('#- Mohon Maaf Modul Pygame Tidak Ditemukan -#')
	exit()

import random

pygame.init()

UKURAN_LAYAR = (960, 540)
TOMBOL_AKTIF = 0
KARAKTER = 0
EFEK_SUARA = True
MUSIK = True
FPS = 30

MUSIK_MENU = pygame.mixer.Sound('Assets\\Suara\\Musik_Game\\Musik_Menu.mp3')
MUSIK_PERMAINAN = {
	'mulai' 		: pygame.mixer.Sound('Assets\\Suara\\Musik_Game\\Permainan_Mulai.mp3'),
	'lawan_bos' 	: pygame.mixer.Sound('Assets\\Suara\\Musik_Game\\Permainan_Melawan_Bos.mp3'),
	'selesai'		: pygame.mixer.Sound('Assets\\Suara\\Musik_Game\\Permainan_Selesai.mp3')
}
EFEK_TOMBOL = {
	'geser'			: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Game\\Tombol_Geser.wav'),
	'tekan'			: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Game\\Tombol_Tekan.mp3')
}
EFEK_PERMAINAN = {
	'hitung_mundur' : pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Game\\Hitung_Mundur.mp3'),
	'dapat_item'	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Game\\Mendapat_Item.mp3'),
}
EFEK_KARAKTER = {
	0 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Unik2.mp3')
		]
	},
	1 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Affan\\Affan_Unik2.mp3')
		]
	},
	2 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Carin\\Carin_Unik2.mp3')
		]
	},
	3 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Unik2.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Ilham\\Ilham_Unik3.mp3')
		]
	},
	4 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Unik2.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Unik3.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Unik4.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Hariando\\Hariando_Unik5.mp3')
		]
	},
	5 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Unik2.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Robi\\Robi_Unik3.mp3')
		]
	},
	6 	: {
		'lari' 		: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Lari.mp3'),
		'lompat' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Lompat.mp3'),
		'tersandung': pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_KenaObstekel.mp3'),
		'menembak' 	: pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Menembak.mp3'),
		'unik' : [
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Unik1.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Unik2.mp3'),
			pygame.mixer.Sound('Assets\\Suara\\Efek_Suara_Karakter\\Rozin\\Rozin_Unik3.mp3')
		]
	},
}

def suara_karakter_berhenti():
	for i in EFEK_KARAKTER[KARAKTER]:
		if i != 'unik':
			EFEK_KARAKTER[KARAKTER][i].stop()

TOMBOL_ATAS = pygame.locals.K_UP
TOMBOL_BAWAH = pygame.locals.K_DOWN
TOMBOL_KANAN = pygame.locals.K_RIGHT
TOMBOL_KIRI = pygame.locals.K_LEFT
TOMBOL_BAWAH_KANAN = (TOMBOL_BAWAH, TOMBOL_KANAN)
TOMBOL_ATAS_KIRI = (TOMBOL_ATAS, TOMBOL_KIRI)

def gambar(lokasi, nama):
	def ambil_gambar(lokasi_file, nama_gambar):
		return pygame.image.load(f'Assets\\{lokasi_file}\\{nama_gambar}')
	if len(nama) == 1:
		return ambil_gambar(lokasi, nama[0])	
	return [ambil_gambar(lokasi, i) for i in nama]

GAMBAR = {
	'MENU_UTAMA' : {
		'Icon' 			: gambar('Menu_Utama', ('Icon.jpg',)),
		'LatarBelakang' : gambar('Menu_Utama', ('LatarBelakang.jpg',)),
		'Mulai' 		: gambar('Menu_Utama', ('Mulai.png',)),
		'Karakter' 		: gambar('Menu_Utama', ('Karakter.png',)),
		'Pengaturan' 	: gambar('Menu_Utama', ('Pengaturan.png',)),
		'Keluar' 		: gambar('Menu_Utama', ('Keluar.png',)),
		'Info' 			: gambar('Menu_Utama', ('Info.png',))
	},
	'MENU_MULAI' : {
		'Cerita1'		: gambar('Menu_Mulai\\Cerita', ('Cerita1.png',)),
		'Cerita2'		: gambar('Menu_Mulai\\Cerita', ('Cerita2.png',)),
		'Cerita3'		: gambar('Menu_Mulai\\Cerita', ('Cerita3.png',)),
		'Cerita4'		: gambar('Menu_Mulai\\Cerita', ('Cerita4.png',)),
		'jeda'			: gambar('Menu_Mulai\\Jeda', ('latar_belakang.png',)),
		'MenuUtama'		: gambar('Menu_Mulai\\Jeda', ('menu_utama.png',)),
		'lanjut'		: gambar('Menu_Mulai\\Jeda', ('lanjut.png',)),
		'kalah'			: gambar('Menu_Mulai\\Kalah', ('kalah.png',)),
		'ulang'			: gambar('Menu_Mulai\\Kalah', ('ulang.png',)),
		'AwalMula'		: gambar('Menu_Mulai', ('AwalMula.jpg',)),
		'LatarBelakang' : gambar('Menu_Mulai', ('LatarBelakang.png',)),
		'Lintasan' 		: gambar('Menu_Mulai', ('Lintasan.png',))
	},
	'MENU_KARAKTER' : {
		'LatarBelakang' : gambar('Menu_Karakter', ('LatarBelakang.jpg',)),
		'PanahKiri' 	: gambar('Menu_Karakter', ('PanahKiri.png',)),
		'PanahKanan' 	: gambar('Menu_Karakter', ('PanahKanan.png',)),
		'Pilih' 		: gambar('Menu_Karakter', ('Pilih.png',))
	},
	'MENU_PENGATURAN' : {
		'LatarBelakang' : gambar('Menu_Pengaturan', ('LatarBelakang.jpg',)),
		'Musik' 		: gambar('Menu_Pengaturan', ('Musik.png',)),
		'EfekSuara' 	: gambar('Menu_Pengaturan', ('EfekSuara.png',)),
		'MusikHidup' 	: gambar('Menu_Pengaturan', ('MusikHidup.png',)),
		'MusikMati' 	: gambar('Menu_Pengaturan', ('MusikMati.png',)),
		'Kembali' 		: gambar('Menu_Pengaturan', ('Kembali.png',))
	},
	'MENU_INFO' : {
		'Info' 			: gambar('Menu_Info', ('Info.png',))
	},
	'KARAKTER' : {
		0 				: gambar('Karakter', ('SiPele.png',)),
		1 				: gambar('Karakter', ('Affan.png',)),
		2 				: gambar('Karakter', ('Carin.png',)),
		3 				: gambar('Karakter', ('Ilham.png',)),
		4 				: gambar('Karakter', ('Hariando.png',)),
		5 				: gambar('Karakter', ('Robi.png',)),
		6 				: gambar('Karakter', ('Rozin.png',)),
		'bergerak' : {
			0 			: gambar('Karakter\\Asset_SiPele', ('Pele1.png', 'Pele2.png', 'Pele3.png', 'Pele4.png')),
			1 			: gambar('Karakter\\Asset_Affan', ('Affan1.png', 'Affan2.png', 'Affan3.png', 'Affan4.png')),
			2 			: gambar('Karakter\\Asset_Carin', ('Carin1.png', 'Carin2.png', 'Carin3.png', 'Carin4.png')),
			3 			: gambar('Karakter\\Asset_Ilham', ('Ilham1.png', 'Ilham2.png', 'Ilham3.png', 'Ilham4.png')),
			4 			: gambar('Karakter\\Asset_Hariando', ('Ando1.png', 'Ando2.png', 'Ando3.png', 'Ando4.png')),
			5 			: gambar('Karakter\\Asset_Robi', ('Robi1.png', 'Robi2.png', 'Robi3.png', 'Robi4.png')),
			6 			: gambar('Karakter\\Asset_Rozin', ('Rozin1.png', 'Rozin2.png', 'Rozin3.png', 'Rozin4.png')),
		}
	},
	'RINTANGAN' : {
		'Batu' 			: gambar('Menu_Mulai\\Rintangan', ('Batu.png',)),
		'kayu' 			: gambar('Menu_Mulai\\Rintangan', ('Kayu.png',))
	},
	'DARAH' : {
		'Papan' 		: gambar('Karakter\\Darah', ('PapanDarah.png',)),
		'DarahHijau' 	: gambar('Karakter\\Darah', ('DarahHijau.png',)),
		'DarahMerah' 	: gambar('Karakter\\Darah', ('DarahMerah.png',)),
		'Item' 			: gambar('Karakter\\Darah', ('Item.png',))
	},
	'LEVEL' : {
		1 				: gambar('Karakter\\Darah', ('Level1.png',)),
		2 				: gambar('Karakter\\Darah', ('Level2.png',)),
		3 				: gambar('Karakter\\Darah', ('Level3.png',))
	}
}

class Tombol:
	def __init__(self, **variabel):
		self.id = variabel['id']
		self.__ukuran = (variabel['panjang'], variabel['lebar'])
		self.__posisi = (variabel['x'], variabel['y'])
		self.__file = variabel['gambar']
	def aktif(self, Layar):
		global TOMBOL_AKTIF
		gambar = pygame.transform.smoothscale(
			self.__file, self.__ukuran)
		if TOMBOL_AKTIF == self.id:
			gambar = self.tombol_membesar()
		Layar.blit(gambar, gambar.get_rect(center = self.__posisi))
	def tombol_membesar(self):
		return pygame.transform.smoothscale(
			self.__file, (self.__ukuran[0] + 15, self.__ukuran[1] + 15))

class Info:
	def __init__(self):
		self.__lvl = 1
		self.__level = pygame.transform.smoothscale(
			GAMBAR['LEVEL'][self.__lvl], (70, 25))
		self.__papan = pygame.transform.smoothscale(
			GAMBAR['DARAH']['Papan'], (280, 80))
		self.__merah = pygame.transform.smoothscale(
			GAMBAR['DARAH']['DarahMerah'], (245, 30))
		self.__hijau = pygame.transform.smoothscale(
			GAMBAR['DARAH']['DarahHijau'], (245, 30))
	def naik_level(self, latar_belakang, lintasan, rintangan):
		self.naik_level_grup(latar_belakang, 1)
		self.naik_level_grup(lintasan, 2)
		rintangan.kecepatan_berubah()
		self.__lvl = 1 if self.__lvl == 3 else self.__lvl + 1
		self.__level = pygame.transform.smoothscale(
			GAMBAR['LEVEL'][self.__lvl], (70, 25))
	def rubah_darah(self, darah):
		self.__hijau = pygame.transform.smoothscale(
			GAMBAR['DARAH']['DarahHijau'], (245 * darah / 100, 30))
	def naik_level_grup(self, grup, nilai):
		for i in grup:
			i.kecepatan_berubah(nilai)
	def tampil(self, Layar):
		Layar.blit(self.__papan, (25, 25))
		Layar.blit(self.__merah, (40, 65))
		Layar.blit(self.__hijau, (40, 65))
		Layar.blit(self.__level, (220, 35))
	def tampil_level(self, Layar):
		level = pygame.transform.smoothscale(
			GAMBAR['LEVEL'][self.__lvl], (140, 50))
		Layar.blit(level, level.get_rect(center = (480, 80)))

class Karakter:
	def __init__(self):
		self.__darah = 100
		self.__langkah = 0
		self.__batas_lompat = 5
		self.info = Info()
		self.__file = [
			pygame.transform.smoothscale(
				i, (145, 180)
			) for i in GAMBAR['KARAKTER']['bergerak'][KARAKTER]]
		self.gambar = self.__file[self.__langkah]
		self.rect = self.gambar.get_rect()
		self.rect.x = 70
		self.rect.y = 330
		self.melompat = False
		self.efek_lari = 0
	def gerak(self, aksi):
		if self.melompat:
			self.lompat()
		else:
			self.rect.x = 70
			self.lari()
		if not self.melompat and aksi[pygame.K_SPACE]:
			if EFEK_SUARA:
				self.efek_lari = 0
				suara_karakter_berhenti()
				EFEK_KARAKTER[KARAKTER]['lompat'].play()
			self.melompat = True
	def lari(self):
		self.gambar = self.__file[self.__langkah // 4]
		if EFEK_SUARA and self.__langkah == 0 and self.efek_lari == 0:
			suara_karakter_berhenti()
			EFEK_KARAKTER[KARAKTER]['lari'].play()
		self.efek_lari += 1 if self.__langkah == 0 else 0
		self.efek_lari %= 6
		self.__langkah = self.__langkah + 1 if self.__langkah < 15 else 0
	def lompat(self):
		self.gambar = self.__file[0]
		if self.melompat :
			self.rect.y -= self.__batas_lompat * 3
			self.__batas_lompat -= 0.3
			if self.__batas_lompat <= 0:
				self.gerak_lompat()
		if self.rect.y >= 330:
			self.rect.y = 330
			self.__batas_lompat = 5
			self.melompat = False
	def gerak_lompat(self):
		self.gambar = self.__file[1 if self.__batas_lompat > -3 else 2]
	def darah_berkurang(self):
		self.__darah -= 20
	def cek_darah(self):
		self.info.rubah_darah(self.__darah)
		if self.__darah <= 0:
			return True
		return False
	def tampil(self, Layar):
		self.info.tampil(Layar)
		Layar.blit(self.gambar, self.rect)

class Item(Karakter):
	_kecepatan = None

class Latar_Main(pygame.sprite.Sprite):
	def __init__(self, gambar, ukuran, kecepatan, posisi_kiri):
		super(Latar_Main, self).__init__()
		self.__file = gambar
		self.__ukuran = ukuran
		self.gambar = pygame.transform.smoothscale(
				self.__file, self.__ukuran)
		self.__kecepatan = kecepatan
		self.posisi = self.gambar.get_rect()
		self.posisi.bottom = UKURAN_LAYAR[1]
		self.posisi.left = posisi_kiri
	def perbaharui(self, grup):
		self.gerak()
		if self.posisi.right >= UKURAN_LAYAR[0]:
			selisih = self.posisi.right - UKURAN_LAYAR[0]
			if selisih <= self.__kecepatan:
				self.tambah_gambar(grup, selisih)
		elif self.posisi.right < 0:
			self.kill()
	def tambah_gambar(self, grup, selisih):
		selisih %= self.__kecepatan
		if self.posisi.right == UKURAN_LAYAR[0] + selisih:
			grup.add(Latar_Main(
				self.__file, self.__ukuran, 
				self.__kecepatan, UKURAN_LAYAR[0] + selisih))
	def gerak(self):
		self.posisi.move_ip(-self.__kecepatan, 0)
	def kecepatan_berubah(self, nilai):
		self.__kecepatan += nilai
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.posisi)

class Rintangan(pygame.sprite.Sprite):
	_kecepatan = 8
	def __init__(self, **variabel):
		super(Rintangan, self).__init__()
		self.__tambah = True
		self.gambar = pygame.transform.smoothscale(
			random.choice([i for i in GAMBAR['RINTANGAN'].values()]),
			(60, 60))
		self.rect = self.gambar.get_rect()
		self.rect.bottom = 528
		self.rect.left = UKURAN_LAYAR[0] + (random.randint(0, 2) * 100)
	def bergerak(self, grup):
		self.rect.move_ip(-self._kecepatan, 0)
		if self.rect.left < 480 and self.__tambah:
			grup.add(Rintangan())
			self.__tambah = False
		elif self.rect.right < 0:
			self.kill()
	def kecepatan_berubah(self):
		Rintangan._kecepatan += 2
	def atur_kembali(self):
		self._kecepatan = 8
	def tampil(self, Layar):
		Layar.blit(self.gambar, self.rect)

TOMBOL = {
	'menu' : {
		'mulai' : Tombol(
			id = 0,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 100,
			gambar = GAMBAR['MENU_UTAMA']['Mulai']
		),
		'karakter' : Tombol(
			id = 1,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 200,
			gambar = GAMBAR['MENU_UTAMA']['Karakter']
		),
		'Pengaturan' : Tombol(
			id = 2,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 300,
			gambar = GAMBAR['MENU_UTAMA']['Pengaturan']
		),
		'keluar' : Tombol(
			id = 3,
			panjang = 280,
			lebar = 107,
			x = 240,
			y = 400,
			gambar = GAMBAR['MENU_UTAMA']['Keluar']
		),
		'informasi' : Tombol(
			id = 4,
			panjang = 60,
			lebar = 60,
			x = 910,
			y = 490,
			gambar = GAMBAR['MENU_UTAMA']['Info']
		)
	},
	'karakter' : {
		'kiri' : Tombol(
			id = 0,
			panjang = 30,
			lebar = 40,
			x = 320,
			y = 490,
			gambar = GAMBAR['MENU_KARAKTER']['PanahKiri']
		),
		'kanan' : Tombol(
			id = 0,
			panjang = 30,
			lebar = 40,
			x = 640,
			y = 490,
			gambar = GAMBAR['MENU_KARAKTER']['PanahKanan']
		),
		'pilih' : Tombol(
			id = 1,
			panjang = 180,
			lebar = 55,
			x = 480,
			y = 490,
			gambar = GAMBAR['MENU_KARAKTER']['Pilih']
		)
	},
	'pengaturan' : {
		'musik' : Tombol(
			id = 0,
			panjang = 340,
			lebar = 88,
			x = 480,
			y = 210,
			gambar = GAMBAR['MENU_PENGATURAN']['Musik']
		),
		'efek_suara' : Tombol(
			id = 1,
			panjang = 340,
			lebar = 88,
			x = 480,
			y = 300,
			gambar = GAMBAR['MENU_PENGATURAN']['EfekSuara']
		),
		'kembali' : Tombol(
			id = 2,
			panjang = 70,
			lebar = 70,
			x = 70,
			y = 490,
			gambar = GAMBAR['MENU_PENGATURAN']['Kembali']
		)
	},
	'menu_mulai' : {
		'menu_utama' : Tombol(
			id = 0,
			panjang = 150,
			lebar = 40,
			x = 330,
			y = 350,
			gambar = GAMBAR['MENU_MULAI']['MenuUtama']
		),
		'lanjut' : Tombol(
			id = 1,
			panjang = 150,
			lebar = 40,
			x = 630,
			y = 350,
			gambar = GAMBAR['MENU_MULAI']['lanjut']
		),
		'ulang' : Tombol(
			id = 1,
			panjang = 150,
			lebar = 40,
			x = 630,
			y = 350,
			gambar = GAMBAR['MENU_MULAI']['ulang']
		)
	}
}

def Pembukaan(Layar, PEMAIN, WAKTU, Latar_belakang_cerita):
	Latar_belakang = pygame.transform.smoothscale(
		GAMBAR['MENU_MULAI']['AwalMula'].convert(),
		(2436, UKURAN_LAYAR[1]))
	posisi = Latar_belakang.get_rect()

	rubah = lambda A,B,C: A * C / B
	kumpulan_cerita = {
		1 : pygame.transform.smoothscale(
				GAMBAR['MENU_MULAI']['Cerita1'],
				(550, rubah(
					GAMBAR['MENU_MULAI']['Cerita1'].get_height(),
					GAMBAR['MENU_MULAI']['Cerita1'].get_width(),
					550))),
		2 : pygame.transform.smoothscale(
				GAMBAR['MENU_MULAI']['Cerita2'],
				(550, rubah(
					GAMBAR['MENU_MULAI']['Cerita2'].get_height(),
					GAMBAR['MENU_MULAI']['Cerita2'].get_width(),
					550))),
		3 : pygame.transform.smoothscale(
				GAMBAR['MENU_MULAI']['Cerita3'],
				(550, rubah(
					GAMBAR['MENU_MULAI']['Cerita3'].get_height(),
					GAMBAR['MENU_MULAI']['Cerita3'].get_width(),
					550))),
		4 : pygame.transform.smoothscale(
				GAMBAR['MENU_MULAI']['Cerita4'],
				(550, rubah(
					GAMBAR['MENU_MULAI']['Cerita4'].get_height(),
					GAMBAR['MENU_MULAI']['Cerita4'].get_width(),
					550)))
	}

	gaya = pygame.font.Font('Assets\\Font\\LuckiestGuy-Regular.ttf', 80)

	hitung_mundur = pygame.USEREVENT + 1
	
	hitung, cerita, waktu = False, 1, 3

	while True:
		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				pygame.quit()
				exit()
			if acara.type == hitung_mundur:
				if EFEK_SUARA:
					EFEK_PERMAINAN['hitung_mundur'].play()
				waktu -= 1
			elif acara.type == pygame.locals.KEYUP:
				if acara.key in (pygame.locals.K_SPACE, pygame.locals.K_RETURN):
					if EFEK_SUARA:
						EFEK_TOMBOL['tekan'].play()
					cerita = 1 if cerita > 4 else cerita + 1

		if not hitung:
			Layar.blit(Latar_belakang, posisi)

			PEMAIN.tampil(Layar)

			if cerita < 5:
				Layar.blit(Latar_belakang_cerita, (0, 0))
				Layar.blit(kumpulan_cerita[cerita], kumpulan_cerita[cerita].get_rect(center = (480, 270)))
			else:
				PEMAIN.lari()
				if posisi.right <= 965:
					PEMAIN.rect.move_ip(+8, 0)
					if PEMAIN.rect.left > UKURAN_LAYAR[0]:
						hitung = True
						pygame.time.set_timer(hitung_mundur, 1000, 3)
						if EFEK_SUARA:
							EFEK_KARAKTER[KARAKTER]['lari'].stop()
							EFEK_PERMAINAN['hitung_mundur'].play()
				else:
					posisi.move_ip(-8, 0)
		else:
			Layar.fill((0, 0, 0))

			Tampilan_waktu = gaya.render(f"{waktu}", True, (255, 255, 255))
			posisi = Tampilan_waktu.get_rect(center = (480, 270))
			Layar.blit(Tampilan_waktu, posisi)
			if waktu == 0:
				return True
		pygame.display.flip()
		WAKTU.tick(FPS)

def Mulai(Layar):
	global FPS, TOMBOL_AKTIF

	TOMBOL_AKTIF = 0

	rubah = lambda A,B,C: A * C / B

	if MUSIK:
		MUSIK_PERMAINAN['mulai'].play(-1)

	WAKTU = pygame.time.Clock()

	PEMAIN = Karakter()

	Latar_belakang_gelap = pygame.Surface(UKURAN_LAYAR)
	Latar_belakang_gelap.fill((0, 0, 0))
	Latar_belakang_gelap.set_alpha(150)

	if not Pembukaan(Layar, PEMAIN, WAKTU, Latar_belakang_gelap):
		return False

	Latar_belakang = pygame.sprite.Group()
	Latar_belakang.add(Latar_Main(
		GAMBAR['MENU_MULAI']['LatarBelakang'].convert(),
		(6680, UKURAN_LAYAR[1]), 1, 0))
	
	Lintasan = pygame.sprite.Group()
	Lintasan.add(Latar_Main(
		GAMBAR['MENU_MULAI']['Lintasan'], 
		(5120, 100), 8, 0))
	
	RINTANGAN = pygame.sprite.Group()
	RINTANGAN.add(Rintangan())

	Tambah_Jarak = pygame.USEREVENT + 2
	pygame.time.set_timer(Tambah_Jarak, 625)

	gaya1 = pygame.font.Font('Assets\\Font\\LuckiestGuy-Regular.ttf', 40)
	gaya2 = pygame.font.Font('Assets\\Font\\LuckiestGuy-Regular.ttf', 15)

	info_jeda = pygame.transform.smoothscale(
		GAMBAR['MENU_MULAI']['jeda'], 
		(500, rubah(
			GAMBAR['MENU_MULAI']['jeda'].get_height(),
			GAMBAR['MENU_MULAI']['jeda'].get_width(),
			500)))
	info_kalah = pygame.transform.smoothscale(
		GAMBAR['MENU_MULAI']['kalah'], 
		(500, rubah(
			GAMBAR['MENU_MULAI']['kalah'].get_height(),
			GAMBAR['MENU_MULAI']['kalah'].get_width(),
			500)))

	waktu, jeda, Kalah = 0, False, False

	while True:
		for i in Latar_belakang:
			i.tampil(Layar)

		for i in Lintasan:
			i.tampil(Layar)

		for i in RINTANGAN:
			i.tampil(Layar)

		PEMAIN.tampil(Layar)

		Tampilan_waktu = gaya1.render(f"{waktu} M", True, (255, 255, 255))
		Layar.blit(Tampilan_waktu, (850, 50))

		info = gaya2.render('(ESC) - Pause', True, (255, 255, 255))
		Layar.blit(info, (info.get_rect(
			center = (480, 535))))
		
		if waktu % 60 in (1,2,3,4,5):
			PEMAIN.info.tampil_level(Layar)

		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				return False
			elif acara.type == pygame.locals.KEYUP:
				if acara.key == pygame.locals.K_ESCAPE and not jeda:
					if EFEK_SUARA:
						suara_karakter_berhenti()
					jeda = not jeda
				elif acara.key in (TOMBOL_KANAN, TOMBOL_KIRI) and (jeda or Kalah):
					if EFEK_SUARA:
						EFEK_TOMBOL['geser'].play()
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 2
				elif acara.key == pygame.locals.K_RETURN and (jeda or Kalah):
					if EFEK_SUARA:
						EFEK_TOMBOL['tekan'].play()
					if TOMBOL_AKTIF == 0:
						if MUSIK:
							MUSIK_PERMAINAN['mulai'].stop()
						if EFEK_SUARA:
							suara_karakter_berhenti()
							for efek in EFEK_KARAKTER[KARAKTER]['unik']:
								efek.stop()
						Rintangan.atur_kembali(Rintangan)
						return True
					else:
						TOMBOL_AKTIF = 0
						if jeda:
							jeda = not jeda
						else:
							if EFEK_SUARA:
								suara_karakter_berhenti()
							Rintangan.atur_kembali(Rintangan)
							Mulai(Layar)
			elif acara.type == Tambah_Jarak and not jeda:
				waktu += 1
				if waktu % 20 == 0 and EFEK_SUARA:
					Unik = random.choice(EFEK_KARAKTER[KARAKTER]['unik'])
					Unik.play()
				if waktu % 60 == 0:
					PEMAIN.info.naik_level(
						Latar_belakang, Lintasan, Rintangan())
		
		Kalah = PEMAIN.cek_darah()
		if jeda or Kalah:
			Layar.blit(Latar_belakang_gelap, (0, 0))

		if jeda:
			Layar.blit(info_jeda, info_jeda.get_rect(center = (480, 270)))
			TOMBOL['menu_mulai']['menu_utama'].aktif(Layar)
			TOMBOL['menu_mulai']['lanjut'].aktif(Layar)
			pygame.display.flip()
			continue

		if Kalah:
			Layar.blit(info_kalah, info_kalah.get_rect(center = (480, 270)))
			TOMBOL['menu_mulai']['menu_utama'].aktif(Layar)
			TOMBOL['menu_mulai']['ulang'].aktif(Layar)
			pygame.display.flip()
			continue
			
		for i in Latar_belakang:
			i.perbaharui(Latar_belakang)

		for i in Lintasan:
			i.perbaharui(Lintasan)
		
		for i in RINTANGAN:
			i.bergerak(RINTANGAN)
		
		PEMAIN.gerak(pygame.key.get_pressed())

		Terkena_rintangan = pygame.sprite.spritecollideany(PEMAIN, RINTANGAN)
		if Terkena_rintangan:
			if EFEK_SUARA:
				suara_karakter_berhenti()
				EFEK_KARAKTER[KARAKTER]['tersandung'].play()
			RINTANGAN.remove(Terkena_rintangan)
			PEMAIN.darah_berkurang()

		pygame.display.flip()
		WAKTU.tick(FPS)

def Menu_karakter(Layar):
	global GAMBAR, TOMBOL, TOMBOL_AKTIF, KARAKTER, EFEK_SUARA
	
	TOMBOL_AKTIF = 0
	
	def buram_gambar(gambar, ukuran_gambar):
		ukuran_skala = (int(ukuran_gambar[0] * 0.6), int(ukuran_gambar[1] * 0.6))
		objek = pygame.transform.smoothscale(gambar, ukuran_skala)
		return pygame.transform.smoothscale(objek, ukuran_gambar)

	Latar_belakang = pygame.transform.smoothscale(
		GAMBAR['MENU_KARAKTER']['LatarBelakang'].convert(), 
		UKURAN_LAYAR)

	sebelum = 6 if (KARAKTER - 1) < 0 else KARAKTER - 1
	tampilan_karakter_sebelum = buram_gambar(
		GAMBAR['KARAKTER'][sebelum], (200, 255))
	
	tampilan_karakter = pygame.transform.smoothscale(
		GAMBAR['KARAKTER'][KARAKTER], (250, 315))

	sesudah = 0 if (KARAKTER + 1) > 6 else KARAKTER + 1
	tampilan_karakter_sesudah = buram_gambar(
		GAMBAR['KARAKTER'][sesudah], (200, 255))

	while True:
		Layar.blit(Latar_belakang, (0, 0))

		Layar.blit(tampilan_karakter_sebelum, 
			tampilan_karakter_sebelum.get_rect(center = (230, 270)))

		Layar.blit(tampilan_karakter, 
			tampilan_karakter.get_rect(center = (480, 270)))
		
		Layar.blit(tampilan_karakter_sesudah, 
			tampilan_karakter_sesudah.get_rect(center = (730, 270)))

		for tombol in TOMBOL['karakter'].values():
			tombol.aktif(Layar)

		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				return False
			elif acara.type == pygame.locals.KEYUP:
				if acara.key in TOMBOL_BAWAH_KANAN or acara.key in TOMBOL_ATAS_KIRI:
					if EFEK_SUARA:
						EFEK_TOMBOL['geser'].play()
					if acara.key in (TOMBOL_BAWAH, TOMBOL_ATAS):
						TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 2
					elif acara.key in (TOMBOL_KANAN, TOMBOL_KIRI) and TOMBOL_AKTIF == 0:
						KARAKTER += 1 if acara.key == TOMBOL_KANAN else 6
						KARAKTER %= 7

						sebelum = 6 if (KARAKTER - 1) < 0 else KARAKTER - 1
						tampilan_karakter_sebelum = buram_gambar(
							GAMBAR['KARAKTER'][sebelum], (200, 255))
						
						tampilan_karakter = pygame.transform.smoothscale(
							GAMBAR['KARAKTER'][KARAKTER], (250, 315))

						sesudah = 0 if (KARAKTER + 1) > 6 else KARAKTER + 1
						tampilan_karakter_sesudah = buram_gambar(
							GAMBAR['KARAKTER'][sesudah], (200, 255))
				elif acara.key == pygame.locals.K_RETURN and TOMBOL_AKTIF == 1:
					if EFEK_SUARA:
						EFEK_TOMBOL['tekan'].play()
					return True
		pygame.display.flip()

def Menu_pengaturan(Layar):
	global GAMBAR, TOMBOL, TOMBOL_AKTIF, MUSIK, EFEK_SUARA

	TOMBOL_AKTIF = 0

	Latar_belakang = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['LatarBelakang'].convert(), 
		UKURAN_LAYAR)

	Suara_hidup = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['MusikHidup'], (50, 50))
	Suara_mati = pygame.transform.smoothscale(
		GAMBAR['MENU_PENGATURAN']['MusikMati'], (50, 50))

	while True:
		Layar.blit(Latar_belakang, (0, 0))

		for tombol in TOMBOL['pengaturan'].values():
			tombol.aktif(Layar)

		musik = Suara_hidup if MUSIK else Suara_mati
		Layar.blit(musik, musik.get_rect(center = (600, 210)))

		efek_suara = Suara_hidup if EFEK_SUARA else Suara_mati
		Layar.blit(efek_suara, efek_suara.get_rect(center = (600, 300)))

		for acara in pygame.event.get():
			if acara.type == pygame.QUIT:
				return False
			elif acara.type == pygame.locals.KEYUP:
				if acara.key in TOMBOL_BAWAH_KANAN or acara.key in TOMBOL_ATAS_KIRI:
					if EFEK_SUARA:
						EFEK_TOMBOL['geser'].play()
					if acara.key in TOMBOL_BAWAH_KANAN:
						TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 3
					elif acara.key in TOMBOL_ATAS_KIRI:
						TOMBOL_AKTIF = (TOMBOL_AKTIF + 2) % 3
				elif acara.key == pygame.locals.K_RETURN:
					if EFEK_SUARA:
						EFEK_TOMBOL['tekan'].play()
					for tombol in TOMBOL['pengaturan'].values():
						if TOMBOL_AKTIF == tombol.id:
							if tombol.id == 0:
								MUSIK = not MUSIK
								if MUSIK:
									MUSIK_MENU.play(-1)
								else:
									MUSIK_MENU.stop()
							elif tombol.id == 1:
								EFEK_SUARA = not EFEK_SUARA
							elif tombol.id == 2:
								return True
							break
		pygame.display.flip()

# > Menu Utama
Layar = pygame.display.set_mode(UKURAN_LAYAR)

pygame.display.set_caption('Petualangan Si Pele By Sepele.SQD')
pygame.display.set_icon(GAMBAR['MENU_UTAMA']['Icon'].convert())

Latar_belakang = pygame.transform.smoothscale(
	GAMBAR['MENU_UTAMA']['LatarBelakang'].convert(), UKURAN_LAYAR)

Latar_belakang_info = pygame.Surface(UKURAN_LAYAR)
Latar_belakang_info.fill((0, 0, 0))
Latar_belakang_info.set_alpha(150)

Gambar_Info = pygame.transform.smoothscale(
	GAMBAR['MENU_INFO']['Info'], (600, 400))

MUSIK_MENU.play(-1)

Utama = berjalan = True
while berjalan:
	Layar.blit(Latar_belakang, (0, 0))

	for tombol in TOMBOL['menu'].values():
		tombol.aktif(Layar)

	if not Utama:
		Layar.blit(Latar_belakang_info, (0, 0))
		Layar.blit(Gambar_Info, Gambar_Info.get_rect(center = (480, 270)))
	
	for acara in pygame.event.get():
		if acara.type == pygame.QUIT:
			berjalan = False
		elif acara.type == pygame.locals.KEYUP:
			if Utama and (acara.key in TOMBOL_BAWAH_KANAN or acara.key in TOMBOL_ATAS_KIRI):
				if EFEK_SUARA:
					EFEK_TOMBOL['geser'].play()
				if acara.key in TOMBOL_BAWAH_KANAN:
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 1) % 5
				elif acara.key in TOMBOL_ATAS_KIRI:
					TOMBOL_AKTIF = (TOMBOL_AKTIF + 4) % 5
			elif acara.key == pygame.locals.K_RETURN:
				if EFEK_SUARA:
					EFEK_TOMBOL['tekan'].play()
				if Utama:
					for tombol in TOMBOL['menu'].values():
						if TOMBOL_AKTIF == tombol.id:
							if tombol.id == 0:
								MUSIK_MENU.stop()
								berjalan = Mulai(Layar)
								if MUSIK:
									MUSIK_MENU.play(-1)
							elif tombol.id == 1:
								berjalan = Menu_karakter(Layar)
							elif tombol.id == 2:
								berjalan = Menu_pengaturan(Layar)
							elif tombol.id == 3:
								berjalan = False
							elif tombol.id == 4:
								Utama = False
							TOMBOL_AKTIF = tombol.id
							break
				else:
					Utama = True
	pygame.display.flip()
pygame.quit()
