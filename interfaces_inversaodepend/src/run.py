from scr.use_case import MyUsecase
from src.database import Database1

use_case = MyUsecase(Database1())

use_case.search_something()
use_case.insert_something()