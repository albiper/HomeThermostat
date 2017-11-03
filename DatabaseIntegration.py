"""Module for sqlite3 database integration"""
import sqlite3
import logging
import os
import psutil


class DatabaseIntegration:
    """Class for sqlite3 database integration"""

    def __init__(self, database_name, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.conn = None
        self.cursor = None
        self.database_name = database_name
        self.is_open = False

    def connect(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.is_open = True

    def execute_query(self, query, autocommit=True):
        self.cursor.execute(query)
        if autocommit:
            self.cursor.commit()

    def execute_select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
