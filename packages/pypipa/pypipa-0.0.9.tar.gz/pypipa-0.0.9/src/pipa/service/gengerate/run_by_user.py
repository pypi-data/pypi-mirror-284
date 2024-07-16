import questionary
from rich import print
from pipa.service.gengerate.common import quest_basic, CORES_ALL, write_title, opener
from pipa.service.export_sys_config import write_export_config_script
import os


def quest():
    config = quest_basic()

    set_record = questionary.select(
        "Whether to set the duration of the perf-record run?\n",
        choices=["Yes", "No, I'll control it by myself. (Exit by Ctrl+C)"],
    ).ask()

    duration_record, duration_stat = None, None

    if set_record == "Yes":
        duration_record = questionary.text(
            "How long do you want to run perf-record? (Default: 120s)\n", "120"
        ).ask()

    set_stat = questionary.select(
        "Whether to set the duration of the perf-stat run?\n",
        choices=["Yes", "No, I'll control it by myself. (Exit by Ctrl+C)"],
    ).ask()
    if set_stat == "Yes":
        duration_stat = questionary.text(
            "How long do you want to run perf-stat? (Default: 120s)\n", "120"
        ).ask()

    config["duration_record"] = duration_record
    config["duration_stat"] = duration_stat

    return config


def generate(config: dict):
    workspace = config["workspace"]
    freq_record = config["freq_record"]
    events_record = config["events_record"]
    annotete = config["annotete"]
    duration_record = config["duration_record"]
    stat_time = config["duration_stat"]
    events_stat = config["events_stat"]
    count_delta_stat = config["count_delta_stat"]
    use_emon = config["use_emon"]
    if use_emon:
        mpp = config["MPP_HOME"]
    with open(os.path.join(workspace, "pipa-collect.sh"), "w", opener=opener) as f:
        write_title(f)

        f.write("WORKSPACE=" + workspace + "\n")
        f.write("mkdir -p $WORKSPACE\n\n")

        f.write("ps -aux -ef --forest > $WORKSPACE/ps.txt\n")

        f.write(
            f"perf record -e '{events_record}' -a -F"
            + f" {freq_record} -o $WORKSPACE/perf.data"
            + (f" -- sleep {duration_record}\n" if duration_record else "\n")
        )

        f.write("sar -o $WORKSPACE/sar.dat 1 >/dev/null 2>&1 &\n")
        f.write("sar_pid=$!\n")
        if use_emon:
            f.write(
                f"emon -i {mpp}/emon_event_all.txt -v -f $WORKSPACE/emon_result.txt -t 0.1 -l 100000000 -c -experimental "
                + (f"-w sleep {stat_time}\n" if stat_time else "\n")
            )
        else:
            f.write(
                f"perf stat -e {events_stat} -C {CORES_ALL[0]}-{CORES_ALL[-1]} -A -x , -I {count_delta_stat} -o $WORKSPACE/perf-stat.csv"
                + (f" sleep {stat_time}\n" if stat_time else "\n")
            )
        f.write("kill -9 $sar_pid\n")

        f.write("echo 'Performance data collected successfully.'\n")

    with open(os.path.join(workspace, "pipa-parse.sh"), "w", opener=opener) as f:
        write_title(f)
        f.write("WORKSPACE=" + workspace + "\n")
        f.write(
            "perf script -i $WORKSPACE/perf.data -I --header > $WORKSPACE/perf.script\n"
        )
        f.write(
            "perf report -i $WORKSPACE/perf.data -I --header > $WORKSPACE/perf.report\n\n"
        )
        f.write("LC_ALL='C' sar -A -f $WORKSPACE/sar.dat >$WORKSPACE/sar.txt\n\n")

        if use_emon:
            f.write(
                f"python {mpp}/mpp/mpp.py -i $WORKSPACE/emon_result.txt -m {mpp}/metrics/icelake_server_2s_nda.xml -o ./ --thread-view"
            )

        if annotete:
            f.write(
                "perf annotate -i $WORKSPACE/perf.data > $WORKSPACE/perf.annotate\n\n"
            )

        write_export_config_script(f, os.path.join(workspace, "config"))

        f.write("echo 'Performance data parsed successfully.'\n")

        print("Shell script generated successfully.")
        print(
            f"Please check the script in {workspace}/pipa-collect.sh and {workspace}/pipa-parse.sh"
        )
        print(
            "Note you need to make sure the workload is running when you call pipa-collect.sh",
            "and the workload is finished when you call pipa-parsed.sh.",
            "Otherwise, the performance data may be incomplete or incorrect."
            "You should ensure that the total workload is longer than ten minutes."
            "Please check the configuration file for more details.",
        )


def main():
    generate(quest())


if __name__ == "__main__":
    main()
