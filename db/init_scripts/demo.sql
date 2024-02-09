SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
USE `shortener`;

-- DROP TABLE IF EXISTS `users`;
-- CREATE TABLE `users`  (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `first_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'first name',
--   `last_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'last name',
--   `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'encoded password',
--   `email` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'email',
--   `role` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'user role',
--   PRIMARY KEY (`id`) USING BTREE,
--   UNIQUE KEY `unique_email` (`email`)
-- ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- -- ----------------------------
-- -- Records of user
-- -- ----------------------------
-- INSERT INTO `users` VALUES (1, 'san', 'zhang', '$2a$10$.6mcEOKBNjsOBhHFhHxPDuv2QKscC9KZSqouKa0ZhBtwz6h54dJWq', '1@qq.com', 'USER');
-- INSERT INTO `users` VALUES (2, 'a', 'b', '$2a$10$.6mcEOKBNjsOBhHFhHxPDuv2QKscC9KZSqouKa0ZhBtwz6h54dJWq', '2@qq.com', 'USER');
-- INSERT INTO `users` VALUES (3, 'c', 'd', '$2a$10$.6mcEOKBNjsOBhHFhHxPDuv2QKscC9KZSqouKa0ZhBtwz6h54dJWq', '3@qq.com', 'USER');
-- INSERT INTO `users` VALUES (4, 'e', 'f', '$2a$10$.6mcEOKBNjsOBhHFhHxPDuv2QKscC9KZSqouKa0ZhBtwz6h54dJWq', '4@qq.com', 'USER');

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `url_mapping`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `long_url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'original url',
  `short_url` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'encoded url',
  `expire_date` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'date of expiry',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `short_url` (`short_url`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

INSERT INTO `url_mapping` VALUES (1, 'google.com', 'Z29vZ2xlLmNvbQ==', '2024-12-31 00:00:01');
INSERT INTO `url_mapping` VALUES (2, 'baidu.com', 'YmFpZHUuY29t', '2024-12-31 00:00:02');
INSERT INTO `url_mapping` VALUES (3, 'bing.com', 'YmluZy5jb20=', '2024-12-31 00:00:03');

