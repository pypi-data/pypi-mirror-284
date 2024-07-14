import time
from datetime import datetime

import pytz

from nrt_time_utils.timezone import TIMEZONES_DICT

YMD_HMSF_DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
YMD_HMS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
YMD_T_HMS_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
YMD_DATE_FORMAT = '%Y-%m-%d'
YM_DATE_FORMAT = '%Y-%m'
Y_DATE_FORMAT = '%Y'

MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS

SECOND_MS = 1000
MINUTE_MS = 60 * SECOND_MS
HOUR_MS = 60 * MINUTE_MS
DAY_MS = 24 * HOUR_MS


class TimeUtil:

    @classmethod
    def date_ms_to_date_str(
            cls, date_ms: int, date_format: str = YMD_HMSF_DATE_FORMAT, tz=None) -> str:

        return cls.date_ms_to_date_time(date_ms, tz).strftime(date_format)

    @classmethod
    def date_ms_to_date_time(cls, date_ms: int, tz=None) -> datetime:
        tz = cls.get_timezone(tz) if isinstance(tz, str) else tz

        return \
            datetime.fromtimestamp(date_ms / 1000, tz) \
            if date_ms is not None else None

    @staticmethod
    def date_str_to_date_time(
            date_str: str, date_format: str = YMD_HMSF_DATE_FORMAT) -> datetime:

        return datetime.strptime(date_str, date_format)

    @staticmethod
    def date_time_to_date_ms(dt: datetime) -> int:
        return int(dt.timestamp()) * 1000

    @staticmethod
    def get_current_date_ms() -> int:
        return int(round(time.time() * 1000))

    @classmethod
    def get_day_end_date_ms(cls, date_ms: int, tz=None) -> int:
        date_time = cls.date_ms_to_date_time(date_ms, tz)
        date_time = date_time.replace(hour=23, minute=59, second=59)
        return cls.date_time_to_date_ms(date_time) + 999

    @classmethod
    def get_day_start_date_ms(cls, date_ms: int, tz=None) -> int:
        date_time = cls.date_ms_to_date_time(date_ms, tz)
        date_time = date_time.replace(hour=0, minute=0, second=0)
        return cls.date_time_to_date_ms(date_time)

    @staticmethod
    def get_timezone(timezone_str: str):
        try:
            return pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(f'Unknown timezone: {timezone_str}')

    @classmethod
    def get_timezone_offset_hours(cls, timezone_str: str) -> int:
        tz = TIMEZONES_DICT.get(timezone_str)

        if tz:
            return tz['utc_offset']

        for tz_v in TIMEZONES_DICT.values():
            if tz_v['name'] == timezone_str:
                return tz_v['utc_offset']

        time_zone = cls.get_timezone(timezone_str)

        return int(time_zone.utcoffset(datetime.now()).total_seconds() / HOUR_SECONDS)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @classmethod
    def is_timeout_ms(cls, start_time_ms: int, timeout_ms: int) -> bool:
        return cls.get_current_date_ms() - start_time_ms > timeout_ms

    @staticmethod
    def is_date_in_format(date_str: str, date_format: str) -> bool:
        try:
            datetime.strptime(date_str, date_format)
        except ValueError:
            return False

        return True
