from dataclasses import dataclass
from datetime import datetime


DISCORD_EPOCH = 1420070400000


@dataclass
class Snowflake:
    """Class for holding the data contained in a snowflake."""

    timestamp: datetime
    worker_id: int
    process_id: int
    increment: int

    @staticmethod
    def parse(snowflake: str) -> "Snowflake":
        """Parse a snowflake into an object."""
        sn = int(snowflake)
        ts = (sn >> 22) + DISCORD_EPOCH
        w_id = (sn & 0x3E0000) >> 17
        p_id = (sn & 0x1F000) >> 12
        inc = sn & 0xFFF
        dt = datetime.fromtimestamp(ts // 1000).replace(microsecond=ts % 1000 * 1000)
        return Snowflake(
            timestamp=dt,
            worker_id=w_id,
            process_id=p_id,
            increment=inc,
        )

    def format(self) -> str:
        """Format this object into a snowflake string."""
        ts = int(self.timestamp.timestamp() * 1000) - DISCORD_EPOCH
        ret = (
            str(int(bin(ts)[2:])).lstrip("0")
            + bin(self.worker_id)[2:].zfill(5)
            + bin(self.process_id)[2:].zfill(5)
            + bin(self.increment)[2:].zfill(12)
        )
        return str(int(ret, 2))
