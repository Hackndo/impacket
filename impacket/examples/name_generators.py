"""
Name generators for creating plausible Windows service, file, and directory names
"""

import random
import string
from datetime import datetime


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
