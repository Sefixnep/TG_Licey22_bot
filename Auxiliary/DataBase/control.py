# Edit path to database
from Auxiliary.config import Paths

Paths.DataBase = "DataBase.db"

# Import utils for database
from Auxiliary.DataBase import operations

operations.record_news("ты лох", "я лох")