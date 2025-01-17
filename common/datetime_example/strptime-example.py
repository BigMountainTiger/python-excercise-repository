# https://www.geeksforgeeks.org/python-datetime-strptime-function/

from datetime import datetime, timedelta

def date_batches(start_date, end_date, batch_size=1):
    format = '%Y-%m-%d'

    start_date = datetime.strptime(start_date, format).date()
    end_date = datetime.strptime(end_date, format).date()

    if start_date > end_date:
        print(f'start_date {start_date} is later than end_date {end_date}, skip.')
        return

    no_of_days = (end_date - start_date).days + 1
    no_of_batches, remainder = divmod(no_of_days, batch_size)

    next_batch_start_date = start_date
    for b in range(no_of_batches):
        batch_start_date = next_batch_start_date
        batch_end_date = batch_start_date + timedelta(days=(batch_size - 1))
        next_batch_start_date = batch_end_date + timedelta(days=1)

        yield batch_start_date.strftime(format), batch_end_date.strftime(format)

    if remainder > 0:
        batch_start_date = next_batch_start_date
        batch_end_date = batch_start_date + timedelta(days=(remainder - 1))

        yield batch_start_date.strftime(format), batch_end_date.strftime(format)


if __name__ == '__main__':

    for batch_start_date, batch_end_date in date_batches('2025-12-01', '2025-12-05'):
        print(f'Processing batch {batch_start_date} - {batch_end_date}')
