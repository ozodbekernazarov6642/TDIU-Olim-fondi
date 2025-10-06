from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    # ---------------- CREATE CONNECTION POOL ---------------- #
    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    # ---------------- CLOSE CONNECTION POOL ---------------- #
    async def close(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

    # ---------------- UNIVERSAL EXECUTE METHOD ---------------- #
    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if execute:
                    result = await connection.execute(command, *args)
                elif fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                else:
                    result = None
            return result

    # ---------------- USERS TABLE ---------------- #
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            username VARCHAR(255),
            date_time TIMESTAMP,
            language VARCHAR(10)
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, id: str, full_name: str, username: str, date_time, language: str):
        sql = """
        INSERT INTO users (id, full_name, username, date_time, language)
        VALUES ($1, $2, $3, $4, $5)
        ON CONFLICT (id) DO UPDATE SET
            full_name = EXCLUDED.full_name,
            username = EXCLUDED.username,
            date_time = EXCLUDED.date_time,
            language = EXCLUDED.language
        RETURNING *;
        """
        return await self.execute(sql, id, full_name, username, date_time, language, fetchrow=True)

    async def select_user(self, user_id):
        sql = "SELECT * FROM users WHERE id = $1"
        return await self.execute(sql, user_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    # ---------------- APPEALS TABLE ---------------- #
    async def create_table_appeals(self):
        sql = """
        CREATE TABLE IF NOT EXISTS appeals (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR NOT NULL REFERENCES users(id),
            message TEXT NOT NULL,
            created_at TIMESTAMP
        );
        """
        await self.execute(sql, execute=True)

    async def add_appeal(self, user_id: str, message: str, created_at):
        sql = """
        INSERT INTO appeals (user_id, message, created_at)
        VALUES ($1, $2, $3)
        RETURNING *;
        """
        return await self.execute(sql, user_id, message, created_at, fetchrow=True)

    async def select_user_appeals(self, user_id: str):
        sql = "SELECT * FROM appeals WHERE user_id = $1 ORDER BY created_at DESC"
        return await self.execute(sql, user_id, fetch=True)

    async def select_all_appeals(self):
        sql = """
        SELECT a.id, a.message, a.created_at, 
               u.full_name, u.language
        FROM appeals a
        JOIN users u ON a.user_id = u.id
        ORDER BY a.created_at DESC;
        """
        return await self.execute(sql, fetch=True)
