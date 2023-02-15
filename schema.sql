DROP TABLE IF EXISTS users;

CREATE TABLE [users] (
  [id] int PRIMARY KEY,
  [mail] nvarchar(255),
  [password] nvarchar(255)
)
GO

CREATE TABLE [package] (
  [id] int PRIMARY KEY,
  [user_id] int
)
GO

ALTER TABLE [package] ADD FOREIGN KEY ([user_id]) REFERENCES [users] ([id])
GO

