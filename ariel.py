import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Nya")

print ("\033[1;32matau silahkan Hubungi Author 69 / Ariel WA :085755494225 ")

username = 'Ariel'      

password = '69'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSelamat Datang Sayank Jangan lupa Subscribe Youtube :Mr.D4N Dan Jangan Direcode yha sayank Buatnya Lama lo :v",

                        os.system('xdg-open https://www.youtube.com/channel/UCsEE2vIlitUSGJAxp_uNJDg')

			sys.exit()



		else:

			print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

