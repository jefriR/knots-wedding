"""
MySQL Database Connection
=========================
"""

import mysql.connector
from mysql.connector import pooling
from contextlib import contextmanager
import logging

from config import MYSQL_CONFIG

logger = logging.getLogger(__name__)

# Connection pool for better performance
connection_pool = None

def init_connection_pool():
    """Initialize MySQL connection pool"""
    global connection_pool
    try:
        connection_pool = pooling.MySQLConnectionPool(
            pool_name="knots_pool",
            pool_size=5,
            pool_reset_session=True,
            **MYSQL_CONFIG
        )
        logger.info("MySQL connection pool created successfully")
        return True
    except mysql.connector.Error as err:
        logger.error(f"Failed to create connection pool: {err}")
        return False

@contextmanager
def get_db_connection():
    """Get a connection from the pool"""
    connection = None
    try:
        connection = connection_pool.get_connection()
        yield connection
    except mysql.connector.Error as err:
        logger.error(f"Database connection error: {err}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()

@contextmanager
def get_db_cursor(dictionary=True):
    """Get a cursor with automatic connection management"""
    with get_db_connection() as connection:
        cursor = connection.cursor(dictionary=dictionary)
        try:
            yield cursor
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()

def test_connection():
    """Test database connection"""
    try:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return result is not None
    except Exception as e:
        logger.error(f"Connection test failed: {e}")
        return False
