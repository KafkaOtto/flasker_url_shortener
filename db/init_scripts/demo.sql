SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
USE `shortener`;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `users`  (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'users name',
  `password` varchar(128)  CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'password',
  PRIMARY KEY (`userid`) USING BTREE,
  UNIQUE KEY `username` (`username`)
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

CREATE TABLE `url_mapping`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `long_url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'original url',
  `expire_date` datetime NULL DEFAULT NULL COMMENT 'date of expiry',
  `username` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'users name',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_long_url` (`long_url`, `username`)
);


INSERT INTO `users` VALUES (1, 'wxt', '16cb2816035b90698c93be3c9331a28d');
INSERT INTO `users` VALUES (2, 'avl', 'e0bebd4964fd90f01f31875eef3bf68c');

INSERT INTO `url_mapping` VALUES (1, 'http://google.com', '2024-12-31 00:00:01', 'wxt');
INSERT INTO `url_mapping` VALUES (2, 'http://bat.com', '2024-12-31 00:00:02', 'wxt');
INSERT INTO `url_mapping` VALUES (3, 'http://bing.com', '2024-12-31 00:00:03', 'avl');
INSERT INTO `url_mapping` VALUES (4, 'http://apple.com', '2024-12-31 00:00:04', 'avl');

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



