def analyze_log(filename):
    info_count = 0
    warning_count = 0
    error_count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.startswith("INFO"):
                info_count += 1
            elif line.startswith("WARNING"):
                warning_count += 1
            elif line.startswith("ERROR"):
                error_count += 1

    print("===== LOG ANALYSIS REPORT =====")
    print(f"INFO messages   : {info_count}")
    print(f"WARNING messages: {warning_count}")
    print(f"ERROR messages  : {error_count}")


# program start here
if __name__ == "__main__":
    analyze_log("app.log")
