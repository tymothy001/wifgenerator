from bit import Key
from bit.format import bytes_to_wif
from tqdm import tqdm

i = 1
target = 20777
print("                                                                                           ")
print("\033[0;32m██╗    ██╗██╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ \033[00m")
print("\033[0;32m██║    ██║██║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗\033[00m")
print("\033[0;32m██║ █╗ ██║██║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝\033[00m")
print("\033[0;32m██║███╗██║██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗\033[00m")
print("\033[0;32m╚███╔███╔╝██║██║         ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║\033[00m")
print("\033[0;32m ╚══╝╚══╝ ╚═╝╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\033[00m")
print("                                                                                           ")
print("                                                                                           ")

print("donate :  1xxxxieunR11dGzNz4ChUdQrhqQAdwUTq                                                                       ")
print("                                                                                           ")
print("                                                                                           ")
print("                                                                                           ")
with open("wif.txt", "w") as f, open("add.txt", "w") as addr_file, open("target.txt", "r") as b_file:
    b_addresses = set(b_file.read().splitlines())

    pbar = tqdm(total=(target - i + 1))

    while i <= target:
        key1 = Key.from_int(i)

        wif = bytes_to_wif(key1.to_bytes(), compressed=False)
        wif2 = bytes_to_wif(key1.to_bytes(), compressed=True)
        key2 = Key(wif)
        key1 == key2

        f.write(wif + "\n")
        f.write(wif2 + "\n")

        address = key1.address
        addr_file.write(address + "\n")

        if address in b_addresses:
            print("Found matching address:", address)

        i += 1
        pbar.update(1)

    pbar.close()
