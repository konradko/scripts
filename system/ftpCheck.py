import ftplib

def ftpCheck(ftpAddress, login, passw, output_file, download_file=None):
    ftp = ftplib.FTP(ftpAddress)
    ftp.login(login, passw) 

    listing = []
    ftp.retrlines("NLST", listing.append)

    for line in listing:
        output_file.write(line + "\n")

    if download_file:
        ftp.retrbinary('RETR %s' % download_file, open(download_file, 'wb').write)

    ftp.quit