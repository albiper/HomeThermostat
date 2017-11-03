"""Module for database interaction"""
import datetime

from DatabaseIntegration import DatabaseIntegration


class DatabaseInteraction:
    """Class for database interaction"""
    db_integration = None

    def __init__(self, database_name):
        self.database_name = database_name
        self.initialized = False

        self.initialize()

    def initialize(self):
        if self.db_integration is None:
            self.db_integration = DatabaseIntegration(self.database_name)

        if not self.db_integration.is_open:
            self.db_integration.connect()

    def get_schedules(self):
        """Get schedules from DB"""

        if not self.initialized:
            self.initialize()

        return self.db_integration.execute_select_query("SELECT * FROM schedules")

    def get_current_schedule(self):
        if not self.initialized:
            self.initialize()

        now = datetime.time.now()
        query = "SELECT * FROM schedules where start <= time('%s') and day_of_week = " % (now.strftime('%H:%M%S'), now.weekday)
        self.db_integration.execute_select_query(query)
