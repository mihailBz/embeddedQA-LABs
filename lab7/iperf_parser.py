def iperf_parser(output):
    parsed_res = []
    output_lines = output.split("\n")
    for line in output_lines[6:-1]:
        splitted_line = line.split("  ")
        parsed_res.append(
            {
                "transfer": float(splitted_line[-2].strip().split(" ")[0]),
                "bitrate": float(splitted_line[-1].strip().split(" ")[0]),
            }
        )
    return parsed_res