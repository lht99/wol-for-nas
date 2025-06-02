# wol-for-nas
wake on lan/wan server run on NAS Synology

1. Download or clone this one
   **git clone https://github.com/lht99/wol-for-nas && cd wol-for-nas**
2. Run: **docker build -t wol-api .**
   (Note that you need . )
3. Save .tar file to import to NAS
   docker save wol-api -o wol-api.tar
4. You can check it work or not by using this command: curl "http://localhost:8000/wol?mac=AA-BB-CC-AA-BB-CC&ip=192.168.1.255&port=9"
   IP you can replace 192.168.1.255 by your ddns
