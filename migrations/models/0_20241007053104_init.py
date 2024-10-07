from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `articles` (
    `id` VARCHAR(255) NOT NULL  PRIMARY KEY,
    `code` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `author` VARCHAR(255) NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `body` LONGTEXT NOT NULL,
    KEY `idx_articles_code_333883` (`code`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `comments` (
    `id` VARCHAR(255) NOT NULL  PRIMARY KEY,
    `code` VARCHAR(255) NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `author` VARCHAR(255) NOT NULL,
    `body` LONGTEXT NOT NULL,
    `article_id` VARCHAR(255) NOT NULL,
    KEY `idx_comments_code_53b59c` (`code`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
