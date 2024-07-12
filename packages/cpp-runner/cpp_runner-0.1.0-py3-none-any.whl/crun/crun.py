import os
import argparse

home = os.path.expanduser("~")

with open(os.path.join(home, ".crun", "usacoheaders")) as f:
    usaco_headers = "".join(f.readlines())

with open(os.path.join(home, ".crun", "template")) as f:
    template = "".join(f.readlines())

with open(os.path.join(home, ".crun", "biomain")) as f:
    bio_main = "".join(f.readlines())

with open(os.path.join(home, ".crun", "usacomain")) as f:
    usaco_main = "".join(f.readlines())

with open(os.path.join(home, ".crun", "main")) as f:
    normal_main = "".join(f.readlines())


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file to run")
    parser.add_argument("-u", "--usaco", help="use usaco template", action="store_true")
    parser.add_argument("-b", "--bio", help="use bio r2 template", action="store_true")
    args = parser.parse_args()
    if not os.path.exists(f"{args.filename}.cpp"):
        with open(f"{args.filename}.cpp", "w+") as f:
            if args.bio:
                f.write(template + bio_main)
            elif args.usaco:
                if os.path.exists(os.path.join(home, ".usaco")):
                    with open(os.path.join(home, ".crun", "usacocreds")) as f2:
                        username = f2.readline().strip()
                else:
                    username = input("Please enter your usaco username: ")
                    with open(os.path.join(home, ".crun", "usacocreds"), "w+") as f2:
                        f2.write(username)

                f.write(
                    usaco_headers % (username, args.filename) + template + usaco_main % (args.filename, args.filename))
            else:
                f.write(template + normal_main)
    else:
        with open(f"{args.filename}.cpp") as f:
            data = f.readlines()

        with open("awrhjhjrtbaktbj.cpp", "w+") as f:
            i = 0
            while i < len(data):
                if "ifstream cin" in data[i] or "ofstream cout" in data[i] or "ios_base::sync_with_stdio" in data[
                    i] or "cin.tie(NULL)" in data[i]:
                    data.pop(i)
                else:
                    i += 1
            f.writelines(data)

        os.system(f"g++ awrhjhjrtbaktbj.cpp")
        os.system(f"./a.out")
        os.system(f"rm -rf ./a.out")
        os.system(f"rm -rf ./awrhjhjrtbaktbj.cpp")


if __name__ == "__main__":
    cli()
