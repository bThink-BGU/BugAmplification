import subprocess
import random

print("Running x264")

# Run the command 1000 times with random arguments and redirect the output
with open("output.log", "w") as log_file, open("stat_result.txt", "w") as stat_file:
    for i in range(1, 1000):
        # Generate random values for each argument
        qp = random.randint(0, 20)
        ref = random.randint(1, 10)
        subme = random.randint(0, 9)
        threads = random.randint(2, 10)
        # input_file = random.randint(0, 19)
        input_file = random.randint(2, 2)

        # Create the full command with the given arguments
        # cmd = f"RaceBenchData/x264.1/install/x264 --quiet --qp {qp} --partitions b8x8,i4x4 --ref {ref} --direct auto --b-pyramid --weightb --mixed-refs --no-fast-pskip --me umh --subme {subme} --analyse b8x8,i4x4 --threads {threads} -o /dev/null RaceBenchData/x264.1/input/input-{input_file}"
        cmd = f"RaceBenchData/x264.1/install/x264 --quiet --qp {qp} --partitions b8x8,i4x4 --ref {ref} --direct auto --b-pyramid --weightb --mixed-refs --no-fast-pskip --me umh --subme {subme} --analyse b8x8,i4x4 --threads {threads} -o /dev/null videos/video_{input_file}.y4m"

        log_file.write(f"\n\n******* Test #{i} ********\n")

        log_file.write(f"{cmd=}\n")
        print(f"{cmd=}")

        log_file.write(f"{qp=} {ref=} {subme=} {threads=} {input_file=}\n")
        print(f"{qp=} {ref=} {subme=} {threads=} {input_file=}")

        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Check if the output contains "RaceBench crashes deliberately"
        status = "fail" if "RaceBench crashes deliberately" in result.stdout else "pass"

        # Write the arguments and status to the stat_result.txt file
        print(f"{i}: {qp=} {ref=} {subme=} {threads=} {input_file=} {status=}")
        stat_file.write(f"{i}: {qp=} {ref=} {subme=} {threads=} {input_file=} {status=}\n")

        # Write the command output to the log file
        log_file.write(result.stdout)
        log_file.write(f"Status: {status}\n")
