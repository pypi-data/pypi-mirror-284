import main, os, tqdm
os.mkdir("./testData")

def mainfunc(n_file: int):
    with open(f"./testData/test_{n_file}.txt", "w") as f:
        f.write(''.join(main.scrng(50, 200)))

for i in tqdm.trange(100):
    mainfunc(i + 1)
