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

        self.initialized = True

    def get_schedules(self):
        """Get schedules from DB"""

        if not self.initialized:
            self.initialize()

        return self.db_integration.execute_select_query("SELECT * FROM schedules")

    def get_current_schedule(self):
        if not self.initialized:
            self.initialize()

        now = datetime.datetime.now()
        query = "SELECT temperatures_levels.temperature FROM schedules inner join temperatures_levels " \
                "on schedules.temperature_level_id = temperatures_levels.id where start <= time('%s') " \
                "and day_of_week = %d ORDER BY start DESC LIMIT 1" % \
                (now.strftime('%H:%M:%S'), now.weekday())

        result = self.db_integration.execute_select_query(query)

        if len(result) == 0:
            return None
        else:
            return result[0]
