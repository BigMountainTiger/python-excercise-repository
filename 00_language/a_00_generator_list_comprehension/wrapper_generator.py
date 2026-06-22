from datetime import datetime, timedelta


def time_slicer(start_time, end_time=None, slot_duration=12):
    end_time = end_time or datetime.now().replace(minute=0, second=0, microsecond=0)

    slot_begin = start_time
    while slot_begin < end_time:
        slot_end = slot_begin + timedelta(hours=slot_duration)
        slot_end = end_time if slot_end > end_time else slot_end

        yield (slot_begin, slot_end)

        slot_begin = slot_end


def wrapper_generator():
    start_time = datetime.fromisoformat("2025-05-23T05:00:00")
    bg = time_slicer(start_time, end_time=None, slot_duration=3)

    for item in bg:
        yield item


for item in wrapper_generator():
    print(f"{item[0].isoformat()} - {item[1].isoformat()}")
