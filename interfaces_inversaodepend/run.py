from src.database import Database1
from src.use_case import MyUsecase


use_case = MyUsecase(Database1())

use_case.search_something()
use_case.insert_something()