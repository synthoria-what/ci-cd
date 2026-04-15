class DB:
    def __init__(self):
        self.db_name = "database"
        self.users = ["user1", "user2", "user3", "user4"]

    def get_users(self):
        return {"total": len(self.users),
                "users": self.users
                }

    def get_total_users(self):
        return len(self.users)

    