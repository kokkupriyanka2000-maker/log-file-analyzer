def analyze_log(log_file, level=None):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    output_lines = []

    try:
        with open(log_file, "r") as file:
            for line in file:
                line = line.strip()

                for key in counts:
                    if line.startswith(key):
                        counts[key] += 1

                        if level and key == level:
                            output_lines.append(line)

        output_lines.append("\nLog Summary:")
        for key, value in counts.items():
            output_lines.append(f"{key}: {value}")

        # write to output file
        with open("log_summary.txt", "w") as out:
            for line in output_lines:
                out.write(line + "\n")

        print("Analysis completed. Results saved to log_summary.txt")

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found")
        