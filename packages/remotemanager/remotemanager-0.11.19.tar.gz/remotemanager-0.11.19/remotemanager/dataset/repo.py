import json
import os
import re
from datetime import datetime

date_format = "%d/%m/%Y %H:%M:%S"
manifest_filename = "{manifest_filename}"


class Manifest:

    def __init__(
        self, instance_uuid, path_override: str = None, name_override: str = None
    ):
        self.instance_uuid = instance_uuid

        self.filename = name_override or manifest_filename

        path = path_override or __file__
        if "." in path:
            path = os.path.split(path)[0]
        self.basepath = path

        self.runner_mode = False  # set True by runners, disables printing

    def now(self) -> str:
        return datetime.strftime(datetime.now(), date_format)

    def to_timestamp(self, timestring: str) -> int:
        return int(datetime.strptime(timestring, date_format).timestamp())

    @property
    def path(self):
        return os.path.join(self.basepath, self.filename)

    def get_data(self, path: str = None) -> list:
        if path is None:
            path = self.path
        if not os.path.exists(path):
            return []
        with open(path) as o:
            data = o.readlines()
        return data

    def write(self, string: str):
        string = f"{self.now()} {self.instance_uuid} {string.strip()}\n"
        with open(self.path, "a+") as o:
            o.write(string)

    def get(self, uuid: str) -> list:

        full_log = self.parse_log()
        uuid_select = full_log.get(uuid, [])
        if not uuid_select:
            return []

        log = [
            f"{datetime.fromtimestamp(line[0]).strftime(date_format)} {uuid} {line[1]}"
            for line in uuid_select
        ]
        return log

    def parse_log(self, path: str = None, string: str = None) -> dict:
        """Convert the log into a dict of {uuid: [time, log]}"""
        if string is not None:
            data = string.split("\n")
        else:
            data = self.get_data(path)

        date_regex = re.compile(r"\d{2}/\d{2}/\d{4}")

        cache = []
        output = {}

        uuid = None
        ts = 0
        for line in data:
            if re.match(date_regex, line):
                if len(cache) != 0:
                    data = [ts, "\n".join(cache)]
                    cache = []
                    try:
                        output[uuid].append(data)
                    except KeyError:
                        output[uuid] = [data]

                datestring, timestring, uuid, *content = line.split(" ")
                ts = self.to_timestamp(f"{datestring} {timestring}")

                cache.append("".join(content))
            else:
                cache.append(line)

        if len(cache) != 0:
            data = [ts, "".join(cache)]
            try:
                output[uuid].append(data)
            except KeyError:
                output[uuid] = [data]

        return output

    def last_time(self, state: str) -> dict:
        """Takes parsed log, returning the last time state appeared for each uuid"""
        data = self.parse_log()
        output = {}
        for uuid, log in data.items():
            if uuid not in output:
                output[uuid] = None
            for line in log:
                if line[1].strip().lower() == state.lower():
                    output[uuid] = line[0]

        if not self.runner_mode:
            print(json.dumps(output))
        return output


# DATASET_CONTENT #
