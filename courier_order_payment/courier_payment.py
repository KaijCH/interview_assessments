from  datetime import datetime


TIME_FORMATION = "%Y-%m-%d %H:%M:%S"

INITIATE = "initiate"

COMPLETE = "complete"

CANCEL = "cancel"

OVER = "over"

COUNT24HRSINMIN = 24 * 60 


def converts(strin: str) -> int:
    datetime_object = datetime.strptime(strin, TIME_FORMATION)
    datetime_epoch = int(datetime_object.timestamp())
    return datetime_epoch


class Record:    

    def __init__(self, status: str, update_time: str) -> None:
        self.status = status
        self.update_epoch = converts(update_time)


class PaymentCalculation:

    def __init__(self, rate:int = 0.5):
        self.lookups = dict()
        self.rate_per_min = rate
        
    def finalizePayment(self, activities: list) -> float:
        activities.sort(lambda x: x[1], reverse=False)
        total_payment = 0

        for delivery_id, update_time, status in activities:
            update_epoch = converts(update_time)
            if delivery_id not in self.lookups and status == INITIATE:
                self.lookups[delivery_id] = Record(status, update_time)
                continue    
            if delivery_id not in self.lookups:
                continue
            last: Record = self.lookups[delivery_id]
            duration = update_epoch  if last.status == OVER else update_epoch - last.update_epoch 
            total_payment += float(duration / 60) * self.rate_per_min
            self.lookups.pop(delivery_id)
    
        settle_time = datetime.now().strftime(TIME_FORMATION)
        settle_epoch = converts(settle_time)

        for delivery_id, record in self.lookups:
            record: Record
            # if record is over single day time and stil longoing now
            if record.status == OVER:
                total_payment += COUNT24HRSINMIN * self.rate_per_min
                continue
            duration = settle_epoch - record.update_epoch
            # if recors is within last 24hrs settlement and still ongoing now, mark curr record as `over``
            total_payment += record.update_epoch * self.rate_per_min
            record.status = OVER
            self.lookups[delivery_id] = record
            
        return total_payment
        
