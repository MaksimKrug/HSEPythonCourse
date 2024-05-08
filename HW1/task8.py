from typing import Union, List, Tuple
import numpy as np

class Statistics:
    def __init__(self, data: Union[List[int|float], Tuple[int|float], np.ndarray[int|float]]):
        """
        Пара моментов:
            1. массив всегда 1D, т.е. просто вектор
            2. степенями свободы можете принебречь
        """
        self.data = data
        
    def calculate_mean(self) -> float | int:
        # считаем среднюю от self.data
        raise NotImplementedError()
        
    def calculate_median(self) -> float | int:
        # считаем медиану от self.data
        raise NotImplementedError()
        
    def calculate_mode(self) -> float | int:
        # считаем моду от self.data
        """
        в случае если два и более объекта встречаются одинаковое количество раз
        модой будет наибольший из них
        
        Пример1:
        data = [1,2,2,3]
        out: 2
        
        Пример2:
        data = [1,2,3]
        out: 3
        """
        raise NotImplementedError()
    
    def std(self) -> float | int:
        # считаем стандартное отклонение (не дисперсию)
        raise NotImplementedError()
    
    def iqr(self) -> float | int:
        # считаем интерквартильный размах: https://shorturl.at/rsuBK
        raise NotImplementedError()


    