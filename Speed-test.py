# biblioteca speedtest-cli
import speedtest as sp

test=sp.Speedtest()

down=test.download()
rsDown=round(down)
fDown=int (rsDown/1e+6)

upload=test.upload()
rsUp=round(upload)
fup=int (rsUp/1e+6)


print(f"Sua velocidade de download é de:{fDown} mb/s")
print(f"Sua velocidade de upload é de: {fup} mb/s")