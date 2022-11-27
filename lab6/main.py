import subprocess
import shlex
import re

server_ip = "127.0.0.1"


def client(server_ip):
    command = f"iperf -c {server_ip} -i 1"
    args = shlex.split(command)
    res = subprocess.check_output(args).decode(encoding="UTF-8")
    if re.match(r"^-*\nClient\sconnecting\sto", res):
        return res, None
    else:
        return None, res


def iperf_parser(output):
    parsed_res = []
    output_lines = output.split("\n")
    for line in output_lines[6:-1]:
        splitted_line = line.split("  ")
        parsed_res.append(
            {
                "transfer": float(splitted_line[-2].split(" ")[0]),
                "bitrate": float(splitted_line[-1].split(" ")[0]),
            }
        )
    return parsed_res


def main():
    result, error = client(server_ip)
    if error is not None:
        print(error)
    else:
        for value in iperf_parser(result):
            if value["transfer"] > 2 and value["bitrate"] > 20:
                print(value)


if __name__ == "__main__":
    main()
