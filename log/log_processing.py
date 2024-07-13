import sys

# test script, which is still being finalized
    
def parse_log_line(line: str) -> dict:
    """ Parsing log line """
    line_item = line.strip().split(' ', 3)
    
    return {
        'date': line_item[0],
        'time': line_item[1],
        'level': line_item[2],
        'message': line_item[3].strip(),
    }


def load_logs(file_path: str) -> list:
    """ Load a log file """
    logs = []
    try:
        with open(file_path) as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """ Filter logs by log level """
    
    filtered_list = [log for log in logs if log['level'] == level]
    return filtered_list


def count_logs_by_level(logs: list) -> dict:
    """ Count logs by log level """
    log_counts = {
        'INFO': 0,
        'DEBUG': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    for log in logs:
        if log['level'] in log_counts:
            log_counts[log['level']] += 1
    return log_counts


def display_log_counts(counts: dict):
    """ Display formatted log counts """
    print('Рівень логування | Кількість')
    for level, count in counts.items():
        print(f"{level}: {count}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script.py /path/logfile.log [log_level]')
        sys.exit(1)
    
    logfile = sys.argv[1]
    log_level_filter = None
    
    if len(sys.argv) > 2:
        log_level_filter = sys.argv[2].upper()
        if log_level_filter not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
            print('Invalid log level filter. Choose from: INFO, DEBUG, ERROR, WARNING')
            sys.exit(1)
    
    logs = load_logs(logfile)
    
    if log_level_filter:
        filtered_logs = filter_logs_by_level(logs, log_level_filter)
        display_log_counts(count_logs_by_level(filtered_logs))
    else:
        display_log_counts(count_logs_by_level(logs))