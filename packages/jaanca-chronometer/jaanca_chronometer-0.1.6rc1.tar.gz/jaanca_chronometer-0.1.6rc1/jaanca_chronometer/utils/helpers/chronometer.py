import time
from datetime import timedelta

class Interval:
    '''Format: HH:mm:ss
    '''
    def __init__(self,hours:int=0, minutes:int=0, seconds:int=0) -> None:
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def __repr__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    @classmethod
    def get_format_time(cls)->str:
        return "HH:mm:ss"

class Chronometer:
    def __init__(self) -> None:
        self.reset()
    def start(self)->None:
        '''Start the stopwatch
        '''
        self.reset()
        self.__start_time = time.time()
    def stop(self)->None:
        '''End stopwatch
        '''
        self.__end_time = time.time()
    def reset(self)->None:
        '''Set the stopwatch to zero
        '''
        self.__start_time=0
        self.__end_time=0
    def get_elapsed_time(self,interval_format:bool=True)->Interval|timedelta:
        '''Description
        :return Interval(str): HH:mm:ss format supported for inserting records into databases and adding elapsed times

        ## Example
        ```Python
        from datetime import timedelta
        from jaanca_chronometer import Chronometer
        import time

        if __name__=="__main__":
            chronometer=Chronometer()

            print(f"date_time format or interval format: {chronometer.get_format_time()}")

            chronometer.start()
            time.sleep(1)
            chronometer.stop()
            elapsed_time=str(chronometer.get_elapsed_time())
            print(f"type[str]:{elapsed_time}")

            chronometer.start()
            time.sleep(2)
            chronometer.stop()
            elapsed_time=str(chronometer.get_elapsed_time())
            print(f"type[str]:{elapsed_time}")

            chronometer.start()
            time.sleep(3)
            chronometer.stop()
            elapsed_time:timedelta=chronometer.get_elapsed_time(interval_format=False)
            print(f"type[timedelta] to insert into databases like PostgreSQL:{elapsed_time}")
            print(f"timedelta[seconds]:{elapsed_time.seconds}")
            
            parse_elapsed_time = Chronometer.parse_elapsed_time("20:3:35")
            print(f"parse_elapsed_time[20:3:35]:{parse_elapsed_time}")

            parse_elapsed_time = Chronometer.parse_elapsed_time("1:1")
            print(f"parse_elapsed_time[1:1]:{parse_elapsed_time}")        
        ´´´
        '''
        elapsed_time:Interval=Chronometer.parse_elapsed_time(self.__end_time - self.__start_time)
        hours, minutes, seconds = map(int, str(elapsed_time).split(':'))
        if interval_format:
            return Interval(hours, minutes, seconds)
        else:
            hours, minutes, seconds = map(int, str(elapsed_time).split(':'))
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def get_format_time(self)->str:
        return Interval.get_format_time()

    @classmethod
    def parse_seconds(cls,elapsed_time:str="00:00:00")->int:
        '''Description
        :param elapsed_time:str: Elapsed time un format "HH:mm:ss"
        :return int: Converts a time into HH:mm format to seconds.
        '''
        hours, minutes, seconds = map(int, str(elapsed_time).split(':'))
        return hours * 3600 + minutes * 60 + seconds

    @classmethod
    def parse_elapsed_time(cls,elapsed_seconds:int|float|str="00:00:00",interval_format:bool=True)->Interval|timedelta:
        '''Description
        :param elapsed_time:str: Elapsed time un format "HH:mm:ss"
        :return int: Converts a time into HH:mm format to seconds.
        '''
        if any([isinstance(elapsed_seconds,int),isinstance(elapsed_seconds,float)]):
            hours = int(elapsed_seconds / 3600)
            minutes = int((elapsed_seconds % 3600) / 60)
            seconds = int(elapsed_seconds % 60)
        else:
            try:
                hours, minutes, seconds = map(int, str(elapsed_seconds).split(':'))
            except:
                hours, minutes, seconds = map(int, "00:00:00".split(':'))
        if interval_format:
            return Interval(hours, minutes, seconds)
        else:            
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)

    @classmethod
    def sum_elapsed_times(cls,elapsed_time1:str="00:00:00",elapsed_time2:str="00:00:00",interval_format:bool=True)->Interval|timedelta:
        '''Description
        Takes two times in HH:mm format, converts them to seconds, adds them and converts the result back to HH:mm.
        '''
        total_seconds = Chronometer.parse_seconds(elapsed_time1) + Chronometer.parse_seconds(elapsed_time2)
        return Chronometer.parse_elapsed_time(total_seconds)