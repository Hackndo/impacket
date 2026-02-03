"""
Name generators for creating plausible Windows service, file, and directory names
"""

import random
import string
from datetime import datetime, timedelta


class ServiceNameGenerator:
    """Generates plausible Windows service names"""

    # Real Windows service name patterns
    VENDORS = ['Microsoft', 'Windows', 'Intel', 'AMD', 'NVIDIA', 'Adobe', 'Realtek']
    COMPONENTS = ['Audio', 'Display', 'Network', 'Security', 'Update', 'Telemetry',
                  'Diagnostic', 'Performance', 'Device', 'Management']
    SUFFIXES = ['Service', 'Helper', 'Manager', 'Monitor', 'Agent']

    @staticmethod
    def generate():
        """Generate a plausible service name (no extension)"""
        pattern = random.choice([
            '{vendor}{component}{suffix}',
            '{vendor}{suffix}',
            '{component}{suffix}',
            'svc{component}',
        ])

        return pattern.format(
            vendor=random.choice(ServiceNameGenerator.VENDORS),
            component=random.choice(ServiceNameGenerator.COMPONENTS),
            suffix=random.choice(ServiceNameGenerator.SUFFIXES)
        )


class FileNameGenerator:
    """Generates plausible file names"""

    # Common file prefixes in Windows
    LOG_PREFIXES = ['log', 'trace', 'debug', 'error', 'event', 'setup', 'install']
    TEMP_PREFIXES = ['tmp', 'temp', 'cache', 'backup', 'old', 'bak']
    DATA_PREFIXES = ['data', 'update', 'config', 'settings', 'info']

    @staticmethod
    def generate_log():
        """Generate a plausible log filename with .log extension"""
        prefix = random.choice(FileNameGenerator.LOG_PREFIXES)

        # Different patterns for log files
        pattern = random.choice([
            '{prefix}_{date}',           # log_20260203
            '{prefix}{number:04d}',      # trace0123
            '{prefix}_{timestamp}',      # error_153042
            '{prefix}',                  # debug (just prefix)
        ])

        return pattern.format(
            prefix=prefix,
            date=datetime.now().strftime('%Y%m%d'),
            number=random.randint(0, 9999),
            timestamp=datetime.now().strftime('%H%M%S')
        ) + '.log'

    @staticmethod
    def generate_temp(extension='.tmp'):
        """Generate a plausible temporary filename"""
        prefix = random.choice(FileNameGenerator.TEMP_PREFIXES)

        pattern = random.choice([
            '{prefix}{hex}',             # tmp4A3F2E
            '{prefix}_{number}',         # temp_12345
            '~{prefix}{number}',         # ~tmp123
            '{prefix}',                  # cache (just prefix)
        ])

        name = pattern.format(
            prefix=prefix,
            hex=''.join(random.choices('0123456789ABCDEF', k=6)),
            number=random.randint(1000, 99999)
        )

        # Only add extension if provided
        return name + extension if extension else name

    @staticmethod
    def generate_batch():
        """Generate a plausible batch filename with .bat extension"""
        prefix = random.choice(['setup', 'install', 'update', 'cleanup', 'init', 'start'])

        pattern = random.choice([
            '{prefix}',                  # setup.bat
            '{prefix}_{number}',         # install_01.bat
            '{prefix}_tmp',              # update_tmp.bat
        ])

        return pattern.format(
            prefix=prefix,
            number=random.randint(1, 99)
        ) + '.bat'

    @staticmethod
    def generate_executable():
        """Generate a plausible executable filename with .exe extension"""
        prefixes = ['svc', 'setup', 'update', 'install', 'helper', 'agent', 'manager', 'host']
        suffixes = ['host', 'svc', 'mngr', 'agent', 'helper', 'exe']

        pattern = random.choice([
            '{prefix}{suffix}',          # svchost.exe, setupmngr.exe
            '{prefix}',                  # agent.exe, helper.exe
        ])

        return pattern.format(
            prefix=random.choice(prefixes),
            suffix=random.choice(suffixes)
        ) + '.exe'


class TaskNameGenerator:
    """Generates plausible Windows scheduled task names"""

    # Common task name patterns in Windows
    ACTIONS = ['Update', 'Sync', 'Check', 'Scan', 'Verify', 'Backup', 'Clean', 'Monitor']
    TARGETS = ['System', 'Security', 'Network', 'Cache', 'Registry', 'Config', 'Logs', 'Data']

    @staticmethod
    def generate():
        """Generate a plausible task name (no extension)"""
        pattern = random.choice([
            '{action}{target}',          # UpdateSystem
            '{target}{action}',          # SystemUpdate
            'Scheduled{action}',         # ScheduledBackup
            '{action}Task',              # ScanTask
        ])

        return pattern.format(
            action=random.choice(TaskNameGenerator.ACTIONS),
            target=random.choice(TaskNameGenerator.TARGETS)
        )


class ShareNameGenerator:
    """Generates plausible SMB share and directory names"""

    SHARE_NAMES = ['SHARE', 'DATA', 'FILES', 'DOCS', 'PUBLIC', 'TRANSFER', 'COMMON']
    DIR_PREFIXES = ['tmp', 'temp', 'cache', 'data', 'backup', 'old']

    @staticmethod
    def generate_share():
        """Generate a plausible share name"""
        base = random.choice(ShareNameGenerator.SHARE_NAMES)

        # Sometimes add a number
        if random.choice([True, False]):
            base += str(random.randint(1, 9))

        return base

    @staticmethod
    def generate_directory():
        """Generate a plausible directory name (with __ prefix for temp dirs)"""
        prefix = random.choice(ShareNameGenerator.DIR_PREFIXES)
        suffix = random.randint(100, 999)

        return f'__{prefix}{suffix}'


class TaskSchedulerGenerator:
    """Generates plausible Windows Task Scheduler configuration values"""

    @staticmethod
    def generate_start_boundary():
        """Generate a plausible StartBoundary timestamp close to current time

        Returns a timestamp in the format: 2024-07-02T21:35:13.1337324
        Uses current date/time with random variation to avoid signatures
        """
        # Generate time within the last 24 hours with random offset
        now = datetime.now()
        hours_offset = random.randint(-24, 0)
        minutes_offset = random.randint(0, 59)
        seconds_offset = random.randint(0, 59)

        target_time = now + timedelta(hours=hours_offset, minutes=minutes_offset, seconds=seconds_offset)

        # Generate random microseconds (7 digits for Windows Task Scheduler format)
        microseconds = random.randint(1000000, 9999999)

        # Format: YYYY-MM-DDTHH:MM:SS.MMMMMMM
        return f"{target_time.strftime('%Y-%m-%dT%H:%M:%S')}.{microseconds}"

    @staticmethod
    def generate_days_interval():
        """Generate a plausible DaysInterval (1-7 days)

        Most Windows tasks use 1 (daily), 7 (weekly), or occasionally 2-6
        """
        # Weighted towards common values
        weights = [50, 10, 5, 5, 5, 10, 15]  # More likely to be 1 or 7
        return random.choices(range(1, 8), weights=weights)[0]

    @staticmethod
    def generate_execution_time_limit():
        """Generate a plausible ExecutionTimeLimit

        Returns duration string in ISO 8601 format (PT1H, PT2H, P1D, P3D, etc.)
        Common values: PT1H (1 hour), PT2H, PT4H, P1D (1 day), P3D (3 days)
        """
        formats = [
            'PT1H',   # 1 hour
            'PT2H',   # 2 hours
            'PT4H',   # 4 hours
            'PT12H',  # 12 hours
            'P1D',    # 1 day
            'P2D',    # 2 days
            'P3D',    # 3 days (original value)
            'P5D',    # 5 days
            'P7D',    # 7 days
        ]
        return random.choice(formats)

    @staticmethod
    def generate_priority():
        """Generate a plausible Priority value (0-10)

        Windows Task Scheduler priorities:
        - 0: Realtime (rarely used)
        - 1-3: High
        - 4-6: Normal (most common)
        - 7-9: Below Normal
        - 10: Idle

        Returns mostly normal priorities (4-7) with occasional variations
        """
        # Weighted towards normal priorities
        priorities = [4, 5, 6, 7, 8]
        weights = [25, 30, 25, 15, 5]  # Most likely 5 or 6
        return random.choices(priorities, weights=weights)[0]

    @staticmethod
    def generate_hidden():
        """Generate a plausible Hidden value (true/false)

        Many legitimate tasks are hidden, but not all
        Returns True 70% of the time, False 30%
        """
        return random.choices([True, False], weights=[70, 30])[0]

    @staticmethod
    def generate_idle_settings():
        """Generate plausible IdleSettings values

        Returns a dict with StopOnIdleEnd and RestartOnIdle boolean values
        Most tasks don't care about idle state, so False is more common
        """
        return {
            'StopOnIdleEnd': random.choices([True, False], weights=[20, 80])[0],
            'RestartOnIdle': random.choices([True, False], weights=[15, 85])[0]
        }

    @staticmethod
    def generate_all():
        """Generate all task scheduler values at once

        Returns a dict with randomized values for easy integration
        Hidden and idle settings are kept at default values to avoid suspicious patterns
        """
        return {
            'StartBoundary': TaskSchedulerGenerator.generate_start_boundary(),
            'DaysInterval': TaskSchedulerGenerator.generate_days_interval(),
            'ExecutionTimeLimit': TaskSchedulerGenerator.generate_execution_time_limit(),
            'Priority': TaskSchedulerGenerator.generate_priority()
        }
