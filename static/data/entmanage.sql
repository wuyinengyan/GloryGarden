/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost
 Source Database       : entmanage

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : utf-8

 Date: 08/15/2019 21:32:47 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can view log entry', '1', 'view_logentry'), ('5', 'Can add permission', '2', 'add_permission'), ('6', 'Can change permission', '2', 'change_permission'), ('7', 'Can delete permission', '2', 'delete_permission'), ('8', 'Can view permission', '2', 'view_permission'), ('9', 'Can add group', '3', 'add_group'), ('10', 'Can change group', '3', 'change_group'), ('11', 'Can delete group', '3', 'delete_group'), ('12', 'Can view group', '3', 'view_group'), ('13', 'Can add user', '4', 'add_user'), ('14', 'Can change user', '4', 'change_user'), ('15', 'Can delete user', '4', 'delete_user'), ('16', 'Can view user', '4', 'view_user'), ('17', 'Can add content type', '5', 'add_contenttype'), ('18', 'Can change content type', '5', 'change_contenttype'), ('19', 'Can delete content type', '5', 'delete_contenttype'), ('20', 'Can view content type', '5', 'view_contenttype'), ('21', 'Can add session', '6', 'add_session'), ('22', 'Can change session', '6', 'change_session'), ('23', 'Can delete session', '6', 'delete_session'), ('24', 'Can view session', '6', 'view_session'), ('25', 'Can add browse_record', '7', 'add_browse_record'), ('26', 'Can change browse_record', '7', 'change_browse_record'), ('27', 'Can delete browse_record', '7', 'delete_browse_record'), ('28', 'Can view browse_record', '7', 'view_browse_record'), ('29', 'Can add dictionary', '8', 'add_dictionary'), ('30', 'Can change dictionary', '8', 'change_dictionary'), ('31', 'Can delete dictionary', '8', 'delete_dictionary'), ('32', 'Can view dictionary', '8', 'view_dictionary'), ('33', 'Can add generate', '9', 'add_generate'), ('34', 'Can change generate', '9', 'change_generate'), ('35', 'Can delete generate', '9', 'delete_generate'), ('36', 'Can view generate', '9', 'view_generate'), ('37', 'Can add online', '10', 'add_online'), ('38', 'Can change online', '10', 'change_online'), ('39', 'Can delete online', '10', 'delete_online'), ('40', 'Can view online', '10', 'view_online'), ('41', 'Can add role', '11', 'add_role'), ('42', 'Can change role', '11', 'change_role'), ('43', 'Can delete role', '11', 'delete_role'), ('44', 'Can view role', '11', 'view_role'), ('45', 'Can add test', '12', 'add_test'), ('46', 'Can change test', '12', 'change_test'), ('47', 'Can delete test', '12', 'delete_test'), ('48', 'Can view test', '12', 'view_test'), ('49', 'Can add user', '13', 'add_user'), ('50', 'Can change user', '13', 'change_user'), ('51', 'Can delete user', '13', 'delete_user'), ('52', 'Can view user', '13', 'view_user'), ('53', 'Can add 菜单管理', '14', 'add_menu'), ('54', 'Can change 菜单管理', '14', 'change_menu'), ('55', 'Can delete 菜单管理', '14', 'delete_menu'), ('56', 'Can view 菜单管理', '14', 'view_menu');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('3', 'auth', 'group'), ('2', 'auth', 'permission'), ('4', 'auth', 'user'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session'), ('7', 'sysmanage', 'browse_record'), ('8', 'sysmanage', 'dictionary'), ('9', 'sysmanage', 'generate'), ('14', 'sysmanage', 'menu'), ('10', 'sysmanage', 'online'), ('11', 'sysmanage', 'role'), ('12', 'sysmanage', 'test'), ('13', 'sysmanage', 'user');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-08-15 16:17:17.627862'), ('2', 'auth', '0001_initial', '2019-08-15 16:17:17.767115'), ('3', 'admin', '0001_initial', '2019-08-15 16:17:18.058956'), ('4', 'admin', '0002_logentry_remove_auto_add', '2019-08-15 16:17:18.142645'), ('5', 'admin', '0003_logentry_add_action_flag_choices', '2019-08-15 16:17:18.198501'), ('6', 'contenttypes', '0002_remove_content_type_name', '2019-08-15 16:17:18.365717'), ('7', 'auth', '0002_alter_permission_name_max_length', '2019-08-15 16:17:18.420202'), ('8', 'auth', '0003_alter_user_email_max_length', '2019-08-15 16:17:18.461492'), ('9', 'auth', '0004_alter_user_username_opts', '2019-08-15 16:17:18.475723'), ('10', 'auth', '0005_alter_user_last_login_null', '2019-08-15 16:17:18.536272'), ('11', 'auth', '0006_require_contenttypes_0002', '2019-08-15 16:17:18.540379'), ('12', 'auth', '0007_alter_validators_add_error_messages', '2019-08-15 16:17:18.552924'), ('13', 'auth', '0008_alter_user_username_max_length', '2019-08-15 16:17:18.630971'), ('14', 'auth', '0009_alter_user_last_name_max_length', '2019-08-15 16:17:18.697344'), ('15', 'auth', '0010_alter_group_name_max_length', '2019-08-15 16:17:18.730647'), ('16', 'auth', '0011_update_proxy_permissions', '2019-08-15 16:17:18.747432'), ('17', 'sessions', '0001_initial', '2019-08-15 16:17:18.778079'), ('18', 'sysmanage', '0001_initial', '2019-08-15 16:17:19.001332');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `sys_browse_record`
-- ----------------------------
DROP TABLE IF EXISTS `sys_browse_record`;
CREATE TABLE `sys_browse_record` (
  `browse_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` char(32) DEFAULT NULL,
  `menu_id` int(11) DEFAULT NULL,
  `createby` datetime(6) NOT NULL,
  PRIMARY KEY (`browse_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_browse_record`
-- ----------------------------
BEGIN;
INSERT INTO `sys_browse_record` VALUES ('1', '0e42282188bd4068bd4a57af3b9a7630', '15', '2019-08-15 17:31:31.877904'), ('2', '0e42282188bd4068bd4a57af3b9a7630', '10', '2019-08-15 17:31:33.253371'), ('3', '0e42282188bd4068bd4a57af3b9a7630', '9', '2019-08-15 17:31:34.299378'), ('4', '0e42282188bd4068bd4a57af3b9a7630', '14', '2019-08-15 17:31:43.929067'), ('5', '0e42282188bd4068bd4a57af3b9a7630', '77', '2019-08-15 17:33:05.230493');
COMMIT;

-- ----------------------------
--  Table structure for `sys_dictionary`
-- ----------------------------
DROP TABLE IF EXISTS `sys_dictionary`;
CREATE TABLE `sys_dictionary` (
  `dict_id` char(32) NOT NULL,
  `dict_name` varchar(255) NOT NULL,
  `dict_cont` varchar(255) NOT NULL,
  `dict_class` varchar(255) NOT NULL,
  `dict_order` int(11) DEFAULT NULL,
  `parent_id` varchar(255) NOT NULL,
  `createtime` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `is_active` int(11) NOT NULL,
  `dict_type` int(11) NOT NULL,
  PRIMARY KEY (`dict_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_dictionary`
-- ----------------------------
BEGIN;
INSERT INTO `sys_dictionary` VALUES ('008fc85b51d041fabc032d2f4ee62118', '下三角', 'layui-icon-triangle-d', 'icon-list', '108', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.317395', '2019-08-15 16:18:47.000000', '1', '1'), ('014b7d81336f4120a2b13e033323dddc', '删除', 'layui-icon-delete', 'icon-list', '88', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.244258', '2019-08-15 16:18:47.000000', '1', '1'), ('03d8c13ba051402583b4942afbd08344', '上一页', 'layui-icon-prev', 'icon-list', '53', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.114285', '2019-08-15 16:18:47.000000', '1', '1'), ('05ea3aa7426d433d9c3780e16ad1ec1a', '上传-圆圈', 'layui-icon-upload-circle', 'icon-list', '102', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.297876', '2019-08-15 16:18:47.000000', '1', '1'), ('08d2f67995414062bf8b7f58af38f94e', '聊天 对话 沟通', 'layui-icon-dialogue', 'icon-list', '91', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.255921', '2019-08-15 16:18:47.000000', '1', '1'), ('0b090edf2d3242ed9de6fdfc2ac3c18b', '网站', 'layui-icon-website', 'icon-list', '25', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.007946', '2019-08-15 16:18:47.000000', '1', '1'), ('0eca2918bfcb417b89615c279c593c5e', '主题', 'layui-icon-theme', 'icon-list', '23', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.001630', '2019-08-15 16:18:47.000000', '1', '1'), ('101607d88a4e4798b1d92cd0ec99154e', '添加-圆圈', 'layui-icon-add-circle', 'icon-list', '112', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.332855', '2019-08-15 16:18:47.000000', '1', '1'), ('120c9da45bbf4e389a36f1cfdd2c938b', '窗口', 'layui-icon-layer', 'icon-list', '93', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.262887', '2019-08-15 16:18:47.000000', '1', '1'), ('13ebabc0c6aa4b299d862268e3c92444', '客服', 'layui-icon-chat', 'icon-list', '133', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.408481', '2019-08-15 16:18:47.000000', '1', '1'), ('17f48e68e97f46c98763ec3eea789bb7', '删除链接', 'layui-icon-unlink', 'icon-list', '74', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.191510', '2019-08-15 16:18:47.000000', '1', '1'), ('19f1bd9889f140b88988f5061ae98ddc', '发现-实心', 'layui-icon-find-fill', 'icon-list', '60', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.140226', '2019-08-15 16:18:47.000000', '1', '1'), ('1e0ecb70e9094e2dac0c5fea2abcfff3', 'Tabs 选项卡', 'layui-icon-tabs', 'icon-list', '83', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.227574', '2019-08-15 16:18:47.000000', '1', '1'), ('1eb1c59a34a5473f88539f694dba04d2', '正确', 'layui-icon-ok-circle', 'icon-list', '139', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.430431', '2019-08-15 16:18:47.000000', '1', '1'), ('1f81c6038ea64a65bfc21bf011edeb6b', '图标 报表 屏幕', 'layui-icon-chart-screen', 'icon-list', '106', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.310564', '2019-08-15 16:18:47.000000', '1', '1'), ('2169977abcf143a883723133255e53fe', '好友', 'layui-icon-friends', 'icon-list', '123', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.372864', '2019-08-15 16:18:47.000000', '1', '1'), ('21a46a13463f4248ade373e343f83a2b', '用户名', 'layui-icon-username', 'icon-list', '10', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.955708', '2019-08-15 16:18:47.000000', '1', '1'), ('27e56814a4a343e5a5dafce76a55e0e0', '控制台', 'layui-icon-console', 'icon-list', '26', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.011071', '2019-08-15 16:18:47.000000', '1', '1'), ('29a65e0f95b945288c9acff29e0584d7', '星星-空心', 'layui-icon-rate', 'icon-list', '2', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.929518', '2019-08-15 16:18:47.000000', '1', '1'), ('29e9c4baa546477f80849e0973e23e84', '箭头 向右', 'layui-icon-right', 'icon-list', '118', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.354895', '2019-08-15 16:18:47.000000', '1', '1'), ('2b8438046c2f4a3ab56510094cf59162', '赞', 'layui-icon-praise', 'icon-list', '32', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.035289', '2019-08-15 16:18:47.000000', '1', '1'), ('2e4c67f5f8954c8ea24d5868045b709f', '相机-空心', 'layui-icon-camera', 'icon-list', '36', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.050135', '2019-08-15 16:18:47.000000', '1', '1'), ('2ef9c833b30f4e1ea487760455140d1c', '字体-斜体', 'layui-icon-fonts-i', 'icon-list', '82', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.221726', '2019-08-15 16:18:47.000000', '1', '1'), ('307f2a3332174642846faba29a9daad1', '收藏-空心', 'layui-icon-star', 'icon-list', '135', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.414758', '2019-08-15 16:18:47.000000', '1', '1'), ('31f1ace9703a400281c0a28c2d5c78d9', '链接', 'layui-icon-link', 'icon-list', '76', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.198648', '2019-08-15 16:18:47.000000', '1', '1'), ('34248c7f03af4295b130af390507148e', '购物车', 'layui-icon-cart-simple', 'icon-list', '50', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.100790', '2019-08-15 16:18:47.000000', '1', '1'), ('370bc5c0002041cfa1063376b546a0bd', '分享', 'layui-icon-share', 'icon-list', '87', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.240803', '2019-08-15 16:18:47.000000', '1', '1'), ('3971f51c2ce945908e6a640a91e26b65', '代码-圆圈', 'layui-icon-code-circle', 'icon-list', '96', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.274743', '2019-08-15 16:18:47.000000', '1', '1'), ('3bee6acc5b5b48b2af38ea73c78f6806', '视频', 'layui-icon-video', 'icon-list', '67', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.166885', '2019-08-15 16:18:47.000000', '1', '1'), ('3dc215ee3eea461582327e91166c8339', '用户', 'layui-icon-user', 'icon-list', '59', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.137278', '2019-08-15 16:18:47.000000', '1', '1'), ('3f6a5c5388b948169af4da636ce31393', '404', 'layui-icon-404', 'icon-list', '113', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.336234', '2019-08-15 16:18:47.000000', '1', '1'), ('4085a881f368465f87eec9be6fef8841', '轮播组图', 'layui-icon-carousel', 'icon-list', '97', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.278962', '2019-08-15 16:18:47.000000', '1', '1'), ('437d8fbbd65f4253bd6c9612e94af199', '播放', 'layui-icon-play', 'icon-list', '64', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.157265', '2019-08-15 16:18:47.000000', '1', '1'), ('45aeae2864044754b60e4c9094415d49', '表单', 'layui-icon-form', 'icon-list', '89', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.250126', '2019-08-15 16:18:47.000000', '1', '1'), ('46a14c774bd543f2adc1240cbe2c7dad', '消息-通知-喇叭', 'layui-icon-speaker', 'icon-list', '69', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.173562', '2019-08-15 16:18:47.000000', '1', '1'), ('4a94a6824af64df880d4308d5500b1c5', '帮助', 'layui-icon-help', 'icon-list', '132', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.405694', '2019-08-15 16:18:47.000000', '1', '1'), ('4ac14210595f44098c56472413d7ca0a', '办公-阅读', 'layui-icon-read', 'icon-list', '46', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.087454', '2019-08-15 16:18:47.000000', '1', '1'), ('4ace1e59844c4d3889c6ab734355bd53', 'QQ', 'layui-icon-login-qq', 'icon-list', '7', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.946874', '2019-08-15 16:18:47.000000', '1', '1'), ('4b3a21a6019d446ebf83fffb6a0fe112', '调查', 'layui-icon-survey', 'icon-list', '47', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.090092', '2019-08-15 16:18:47.000000', '1', '1'), ('4d26ae1cf33e49ae9f9577a2e5b305f3', '表情-微笑', 'layui-icon-face-smile', 'icon-list', '48', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.093086', '2019-08-15 16:18:47.000000', '1', '1'), ('4f9e8aea112347e8a86b1baf6729697f', '删除线', 'layui-icon-fonts-del', 'icon-list', '70', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.177128', '2019-08-15 16:18:47.000000', '1', '1'), ('52d91ffe1a104e9a94e149f5544c3c62', '日期', 'layui-icon-date', 'icon-list', '94', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.265707', '2019-08-15 16:18:47.000000', '1', '1'), ('5401abe5f7e44cd586043de6ff846835', '代码', 'layui-icon-fonts-code', 'icon-list', '71', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.182443', '2019-08-15 16:18:47.000000', '1', '1'), ('56f79eab7a1c434191632a3135ec3dba', '添加-圆圈-细体', 'layui-icon-add-circle-fine', 'icon-list', '140', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.433684', '2019-08-15 16:18:47.000000', '1', '1'), ('586465f807fc4da38d745d44fa6a18d5', '表情-惊讶', 'layui-icon-face-surprised', 'icon-list', '27', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.017263', '2019-08-15 16:18:47.000000', '1', '1'), ('58a12800078647ee90d09f7e3aa29b93', '下载-圆圈', 'layui-icon-download-circle', 'icon-list', '56', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.124304', '2019-08-15 16:18:47.000000', '1', '1'), ('597c1133fa9f40709f889597a0ab114f', '图片', 'layui-icon-picture', 'icon-list', '75', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.195602', '2019-08-15 16:18:47.000000', '1', '1'), ('5c2545dc5a654bbf8b93e46b9e6b0a82', '提示说明', 'layui-icon-tips', 'icon-list', '16', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.976751', '2019-08-15 16:18:47.000000', '1', '1'), ('5d84e33730b74952b1a4ff2ee14750ed', '单选框-候选', 'layui-icon-circle', 'icon-list', '85', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.235102', '2019-08-15 16:18:47.000000', '1', '1'), ('5e99fe0e06a541f5ba42668a9fc5c9c8', '刷新', 'layui-icon-refresh-1', 'icon-list', '21', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.994661', '2019-08-15 16:18:47.000000', '1', '1'), ('5f9258bee16c4829a07f621fbe6563c8', '对 OK', 'layui-icon-ok', 'icon-list', '131', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.403095', '2019-08-15 16:18:47.000000', '1', '1'), ('5fb5b71601d04f628c2ea7c52d9e6ff1', '刷新', 'layui-icon-refresh', 'icon-list', '20', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.990213', '2019-08-15 16:18:47.000000', '1', '1'), ('6306cc5bdc1d41e2b93c87f2a7629c6b', '语音-声音', 'layui-icon-voice', 'icon-list', '68', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.169831', '2019-08-15 16:18:47.000000', '1', '1'), ('64c34f8d6aa249f5baab563bb7906e28', 'icon-列表', 'icon-list', 'icon-list', '1', '0', '2019-08-15 16:18:45.000000', '2019-08-15 16:18:47.000000', '1', '0'), ('695a3106e2fe45cbb24083010360475d', '相机-实心', 'layui-icon-camera-fill', 'icon-list', '37', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.052903', '2019-08-15 16:18:47.000000', '1', '1'), ('6bf59245472d49ab90db2048cb300876', '下一页', 'layui-icon-next', 'icon-list', '52', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.109927', '2019-08-15 16:18:47.000000', '1', '1'), ('6ca70243032a46d49c1620fa39c65480', '字体-下划线', 'layui-icon-fonts-u', 'icon-list', '81', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.217046', '2019-08-15 16:18:47.000000', '1', '1'), ('6dbaf910667b4341b7c4ee6e8d692f77', '箭头 向下', 'layui-icon-down', 'icon-list', '116', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.349200', '2019-08-15 16:18:47.000000', '1', '1'), ('6dc24d1dfc884b798919aa8d48e722a2', '暂停', 'layui-icon-pause', 'icon-list', '65', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.160139', '2019-08-15 16:18:47.000000', '1', '1'), ('6eaf069731574481b2492493c81559d8', '翻页', 'layui-icon-prev-circle', 'icon-list', '98', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.282403', '2019-08-15 16:18:47.000000', '1', '1'), ('6fa208c35b5d4d5b8b3659fac25a8896', '表情-笑-细体', 'layui-icon-face-smile-fine', 'icon-list', '128', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.389254', '2019-08-15 16:18:47.000000', '1', '1'), ('6fefff5dbec443d491d24f2ca83491cb', '发布 纸飞机', 'layui-icon-release', 'icon-list', '130', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.400307', '2019-08-15 16:18:47.000000', '1', '1'), ('7166c02073e94df6a60e2f62de486af9', '高级', 'layui-icon-senior', 'icon-list', '19', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.985621', '2019-08-15 16:18:47.000000', '1', '1'), ('7a6ae104ae3f498ab679f1ba41b74e25', '密码', 'layui-icon-password', 'icon-list', '9', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.952532', '2019-08-15 16:18:47.000000', '1', '1'), ('7b5259e63b994c7898cd9bcaadbbb306', '便签', 'layui-icon-note', 'icon-list', '17', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.980064', '2019-08-15 16:18:47.000000', '1', '1'), ('7b8e4ecb84e24f72a700c474349133ac', '旗帜', 'layui-icon-flag', 'icon-list', '22', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.997917', '2019-08-15 16:18:47.000000', '1', '1'), ('7f9c5aba9b1e4672bd34764d639dbb51', '箭头 向左', 'layui-icon-left', 'icon-list', '117', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.352409', '2019-08-15 16:18:47.000000', '1', '1'), ('7ff77f249e0a4dbfad3ba4ff05f6a132', '购物车', 'layui-icon-cart', 'icon-list', '51', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.103711', '2019-08-15 16:18:47.000000', '1', '1'), ('805d7ff6be7f4efb91ff3df63c035c93', 'loading', 'layui-icon-loading', 'icon-list', '61', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.142939', '2019-08-15 16:18:47.000000', '1', '1'), ('871559666bec49629395d6271039b9d5', '设置-空心', 'layui-icon-set', 'icon-list', '28', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.021333', '2019-08-15 16:18:47.000000', '1', '1'), ('88623109abae4a9691adf316a4db1a8e', '菜单-水平', 'layui-icon-more', 'icon-list', '38', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.055564', '2019-08-15 16:18:47.000000', '1', '1'), ('8960f3d73e5c454291a039ca55a75a12', '搜索', 'layui-icon-search', 'icon-list', '120', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.360389', '2019-08-15 16:18:47.000000', '1', '1'), ('89b279c69e884d7a8d5a48271954085c', '位置-地图', 'layui-icon-location', 'icon-list', '45', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.084683', '2019-08-15 16:18:47.000000', '1', '1'), ('89d9a1adf5134b909147e0027da26edd', '应用', 'layui-icon-app', 'icon-list', '30', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.028336', '2019-08-15 16:18:47.000000', '1', '1'), ('8e29b619903644489dd735e9a783e36d', '半星', 'layui-icon-rate-half', 'icon-list', '1', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.825938', '2019-08-15 16:18:47.000000', '1', '1'), ('8f7fc7480d6d427e8cd9ee6d54feb9eb', '菜单-垂直', 'layui-icon-more-vertical', 'icon-list', '39', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.060229', '2019-08-15 16:18:47.000000', '1', '1'), ('901eb8b5766a4bd79eba098675c559eb', '列表', 'layui-icon-list', 'icon-list', '129', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.396091', '2019-08-15 16:18:47.000000', '1', '1'), ('934fc446083c491fa07e234bc365dbf0', '验证码', 'layui-icon-vercode', 'icon-list', '5', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.941472', '2019-08-15 16:18:47.000000', '1', '1'), ('946ec4dd14814d349ea739a40c790e72', '圆点', 'layui-icon-circle-dot', 'icon-list', '119', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.357529', '2019-08-15 16:18:47.000000', '1', '1'), ('95485725cb3843fdb9391f81bbd7d7a0', '组件', 'layui-icon-component', 'icon-list', '57', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.127714', '2019-08-15 16:18:47.000000', '1', '1'), ('97ade73cc2ab489184599f27d56851cb', '树', 'layui-icon-tree', 'icon-list', '103', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.302106', '2019-08-15 16:18:47.000000', '1', '1'), ('9820d109da8b419d9172838802b5c250', '群组', 'layui-icon-group', 'icon-list', '122', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.367127', '2019-08-15 16:18:47.000000', '1', '1'), ('9ba5da5e25554f0dafc404632a86a97a', '文件', 'layui-icon-file', 'icon-list', '110', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.325931', '2019-08-15 16:18:47.000000', '1', '1'), ('a0f2006a294e48a8ba1af35a5b176619', '手机-细体', 'layui-icon-cellphone-fine', 'icon-list', '90', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.253154', '2019-08-15 16:18:47.000000', '1', '1'), ('a1621a830ad9490084a19bcc1666e7c9', '右对齐', 'layui-icon-align-right', 'icon-list', '79', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.210318', '2019-08-15 16:18:47.000000', '1', '1'), ('a21329c8a2834bffa8737de56db4750d', '手机', 'layui-icon-cellphone', 'icon-list', '4', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.937924', '2019-08-15 16:18:47.000000', '1', '1'), ('a2e0b8509d97403796579ef83dedc268', '设置-小型', 'layui-icon-set-sm', 'icon-list', '111', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.329824', '2019-08-15 16:18:47.000000', '1', '1'), ('a571835a3b9d4725965ba599cd71d721', '右三角', 'layui-icon-triangle-r', 'icon-list', '109', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.323127', '2019-08-15 16:18:47.000000', '1', '1'), ('a68e49b84b0b4f0bb1f1f0cf34f232ba', '男', 'layui-icon-male', 'icon-list', '34', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.042846', '2019-08-15 16:18:47.000000', '1', '1'), ('a9ae9c3173f845fbb0b6a1306fec1754', '文字格式化', 'layui-icon-fonts-clear', 'icon-list', '92', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.258894', '2019-08-15 16:18:47.000000', '1', '1'), ('abd2148fa9c747ee85c730b1c52957fd', '添加', 'layui-icon-add-1', 'icon-list', '63', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.151253', '2019-08-15 16:18:47.000000', '1', '1'), ('acbdbb73c2ff424db73211bfce91c639', '表格', 'layui-icon-table', 'icon-list', '104', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.304793', '2019-08-15 16:18:47.000000', '1', '1'), ('b0fd307ec80643e7a8ebe1305ae6d447', '文件-粗', 'layui-icon-file-b', 'icon-list', '58', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.133610', '2019-08-15 16:18:47.000000', '1', '1'), ('b200e1e946a54c4a8a73584dd95399f7', 'top 置顶', 'layui-icon-top', 'icon-list', '134', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.411877', '2019-08-15 16:18:47.000000', '1', '1'), ('b2b8e1a1c1cf4e89a1e5012f998f9cbf', '关闭-实心', 'layui-icon-close-fill', 'icon-list', '137', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.423763', '2019-08-15 16:18:47.000000', '1', '1'), ('b2f25cbcc001430a99027639ec5f0953', '模板', 'layui-icon-template', 'icon-list', '31', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.031391', '2019-08-15 16:18:47.000000', '1', '1'), ('b2f7428a22574978bbfff6f338e93649', '火', 'layui-icon-fire', 'icon-list', '43', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.075835', '2019-08-15 16:18:47.000000', '1', '1'), ('b363d3517ab4440a81e49d76c8bcd03f', '雪花', 'layui-icon-snowflake', 'icon-list', '15', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.973607', '2019-08-15 16:18:47.000000', '1', '1'), ('b3f1f88c13824877bdc5183a0a485b28', '星星-实心', 'layui-icon-rate-solid', 'icon-list', '3', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.934742', '2019-08-15 16:18:47.000000', '1', '1'), ('b7a5e2efa86e49bf928342e523c58384', '编辑', 'layui-icon-edit', 'icon-list', '86', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.237873', '2019-08-15 16:18:47.000000', '1', '1'), ('b8bc1a8135be45c8bc173cb9bd995fd1', '模板', 'layui-icon-template-1', 'icon-list', '29', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.024884', '2019-08-15 16:18:47.000000', '1', '1'), ('bbf9bd34f8874a66a18447c73874d56b', 'HTML', 'layui-icon-fonts-html', 'icon-list', '72', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.186227', '2019-08-15 16:18:47.000000', '1', '1'), ('bfc316cf70ce4da18a7c680a20592625', '表情-笑-粗', 'layui-icon-face-smile-b', 'icon-list', '77', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.204652', '2019-08-15 16:18:47.000000', '1', '1'), ('bfc88893ffe640c3b3b39354c8f0b36b', '金额-美元', 'layui-icon-dollar', 'icon-list', '41', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.068834', '2019-08-15 16:18:47.000000', '1', '1'), ('bfddbb6899824da2bf6ee7b2d2dee9bc', '居中对齐', 'layui-icon-align-center', 'icon-list', '80', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.213983', '2019-08-15 16:18:47.000000', '1', '1'), ('bfe73be614b44e11b889d36da6bb64e8', '字体加粗', 'layui-icon-fonts-strong', 'icon-list', '73', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.188891', '2019-08-15 16:18:47.000000', '1', '1'), ('c03c61e3dde44e17846fcd76371da984', '返回', 'layui-icon-return', 'icon-list', '44', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.079030', '2019-08-15 16:18:47.000000', '1', '1'), ('c10dfdff80b14880978f4f5af5f0b58d', '水 下雨', 'layui-icon-water', 'icon-list', '95', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.269273', '2019-08-15 16:18:47.000000', '1', '1'), ('c12e4be66e6c4d618272557037137bbd', '关于', 'layui-icon-about', 'icon-list', '114', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.339724', '2019-08-15 16:18:47.000000', '1', '1'), ('c2ebebc411374e60a2b9a6a95bade818', '左向右伸缩菜单', 'layui-icon-spread-left', 'icon-list', '13', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.966000', '2019-08-15 16:18:47.000000', '1', '1'), ('c2fd101e4e7844a59121f98eec164f9a', '设置-实心', 'layui-icon-set-fill', 'icon-list', '121', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.364496', '2019-08-15 16:18:47.000000', '1', '1'), ('c4062788135f4b85b34ce43580bfb679', '主页', 'layui-icon-home', 'icon-list', '18', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.982914', '2019-08-15 16:18:47.000000', '1', '1'), ('c757dceb76d145f1b798520dad36f75c', '布局', 'layui-icon-layouts', 'icon-list', '99', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.285350', '2019-08-15 16:18:47.000000', '1', '1'), ('cc3ed06cb5fa4d0790eeb39f09c50149', '回复 评论 实心', 'layui-icon-reply-fill', 'icon-list', '124', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.376355', '2019-08-15 16:18:47.000000', '1', '1'), ('d0e67a1221174a99a2ad96a7b4ea9aa8', '上传-空心-拖拽', 'layui-icon-upload-drag', 'icon-list', '54', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.117572', '2019-08-15 16:18:47.000000', '1', '1'), ('d6977e0ba726489f85e5d5ba00025fc9', '选择模板', 'layui-icon-templeate-1', 'icon-list', '101', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.291558', '2019-08-15 16:18:47.000000', '1', '1'), ('dafb010cb1984e29ae6d53a05f88b8b3', '关闭-空心', 'layui-icon-close', 'icon-list', '138', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.426610', '2019-08-15 16:18:47.000000', '1', '1'), ('db40342551404e5d8782a0c6d1035668', '菜单 隐身 实心', 'layui-icon-menu-fill', 'icon-list', '125', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.379994', '2019-08-15 16:18:47.000000', '1', '1'), ('dd0f827ba37c49a1b7824019bb23c71a', '钻石-等级', 'layui-icon-diamond', 'icon-list', '42', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.071733', '2019-08-15 16:18:47.000000', '1', '1'), ('dd14580f80364e72b03de6313222f75a', '女', 'layui-icon-female', 'icon-list', '35', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.045836', '2019-08-15 16:18:47.000000', '1', '1'), ('dff3c8790a784925afe0878c1c015c8e', '刷新-粗', 'layui-icon-refresh-3', 'icon-list', '11', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.959235', '2019-08-15 16:18:47.000000', '1', '1'), ('e1413b8fe5fa4619b44786faf571edba', '工具', 'layui-icon-util', 'icon-list', '100', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.288104', '2019-08-15 16:18:47.000000', '1', '1'), ('e249393065dc4ab4bb9f5377fa94e6a5', '金额-人民币', 'layui-icon-rmb', 'icon-list', '40', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.064841', '2019-08-15 16:18:47.000000', '1', '1'), ('e472de6fd73244e394dccb553d00dd3a', '音频-耳机', 'layui-icon-headset', 'icon-list', '66', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.164021', '2019-08-15 16:18:47.000000', '1', '1'), ('e4c280b1679c4252933b1401938000fe', '上传-实心', 'layui-icon-upload', 'icon-list', '55', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.120582', '2019-08-15 16:18:47.000000', '1', '1'), ('e944dd3ac1404eff810261fee3d7c4f0', '消息-通知', 'layui-icon-notice', 'icon-list', '24', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.005142', '2019-08-15 16:18:47.000000', '1', '1'), ('ea42c065f4be4e8cbbba9b8da4a1f1a4', '图表', 'layui-icon-chart', 'icon-list', '105', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.307854', '2019-08-15 16:18:47.000000', '1', '1'), ('ea8c7594ba124c50ba7b95b4cc1ab494', '踩', 'layui-icon-tread', 'icon-list', '33', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.039994', '2019-08-15 16:18:47.000000', '1', '1'), ('ef4ed8726ba440bd844d46c6578a8409', '图片-细体', 'layui-icon-picture-fine', 'icon-list', '127', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.385801', '2019-08-15 16:18:47.000000', '1', '1'), ('ef57dd3ce642497288c4a915e5c5892b', '记录', 'layui-icon-log', 'icon-list', '126', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.382897', '2019-08-15 16:18:47.000000', '1', '1'), ('f1b75a8982ea4d38a0cfd2d268e1f445', '授权', 'layui-icon-auz', 'icon-list', '12', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.962055', '2019-08-15 16:18:47.000000', '1', '1'), ('f416397081e04739bad150f4cf6f246c', '收藏-实心', 'layui-icon-star-fill', 'icon-list', '136', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.420162', '2019-08-15 16:18:47.000000', '1', '1'), ('f5260a2860b2467aaf61b010088052ce', '左对齐', 'layui-icon-align-left', 'icon-list', '78', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.207451', '2019-08-15 16:18:47.000000', '1', '1'), ('f65a849ce17d4a12a6cb146610795c35', '微信', 'layui-icon-login-wechat', 'icon-list', '6', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.944242', '2019-08-15 16:18:47.000000', '1', '1'), ('f7df21edc58545759af371b97e27cce8', '表情-哭泣', 'layui-icon-face-cry', 'icon-list', '49', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.097067', '2019-08-15 16:18:47.000000', '1', '1'), ('f9079aea9592419f919fac7a16a99328', '微博', 'layui-icon-login-weibo', 'icon-list', '8', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.949371', '2019-08-15 16:18:47.000000', '1', '1'), ('f9514099f4654d0aaa5c098c6fd5a222', '单选框-选中', 'layui-icon-radio', 'icon-list', '84', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.231743', '2019-08-15 16:18:47.000000', '1', '1'), ('f98ae22a577948f1920be6dd6c5e99c5', '箭头 向上', 'layui-icon-up', 'icon-list', '115', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.344976', '2019-08-15 16:18:47.000000', '1', '1'), ('fa288d7fb399424db859b77fd7bf4399', 'loading', 'layui-icon-loading-1', 'icon-list', '62', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.147712', '2019-08-15 16:18:47.000000', '1', '1'), ('fa8203e94d2c4ac7868693d09e73a538', '右向左伸缩菜单', 'layui-icon-shrink-right', 'icon-list', '14', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:43.970578', '2019-08-15 16:18:47.000000', '1', '1'), ('fd64954d1b4543489204cf2d40c43c45', '引擎', 'layui-icon-engine', 'icon-list', '107', '64c34f8d6aa249f5baab563bb7906e28', '2019-08-15 17:21:44.313967', '2019-08-15 16:18:47.000000', '1', '1');
COMMIT;

-- ----------------------------
--  Table structure for `sys_generate`
-- ----------------------------
DROP TABLE IF EXISTS `sys_generate`;
CREATE TABLE `sys_generate` (
  `generate_id` char(32) NOT NULL,
  `name` varchar(255) NOT NULL,
  `is_active` int(11) NOT NULL,
  PRIMARY KEY (`generate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `sys_menu`
-- ----------------------------
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE `sys_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `menu_url` varchar(255) DEFAULT NULL,
  `menu_order` varchar(100) DEFAULT NULL,
  `menu_icon` varchar(60) DEFAULT NULL,
  `menu_type` varchar(10) DEFAULT NULL,
  `menu_state` int(11) DEFAULT NULL,
  `attributes_color_type` varchar(30) DEFAULT NULL,
  `attributes_other` varchar(100) DEFAULT NULL,
  `shiro_key` varchar(100) DEFAULT NULL,
  `menu_states` int(11) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `sys_menu_parent_id_84e9a06a_fk_sys_menu_id` (`parent_id`),
  KEY `sys_menu_tree_id_2fdc42d8` (`tree_id`),
  CONSTRAINT `sys_menu_parent_id_84e9a06a_fk_sys_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `sys_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_menu`
-- ----------------------------
BEGIN;
INSERT INTO `sys_menu` VALUES ('1', '首页', null, '1', null, 'tree', null, null, null, null, null, '1', '1', '52', '12', '0', null), ('2', '物资模块报表', '', '2', 'layui-icon-dollar', 'tree', null, null, null, null, null, '1', '1', '4', '11', '0', null), ('3', '营运模块报表', '', '3', 'layui-icon-survey', 'tree', null, null, null, null, null, '1', '1', '2', '10', '0', null), ('4', '系统管理', null, '1', 'layui-icon-set', 'tree', null, null, null, null, '0', '1', '2', '25', '12', '1', '1'), ('5', '用户管理', '', '2', 'layui-icon-user', 'tree', null, null, null, null, null, '1', '48', '51', '12', '1', '1'), ('7', '系统工具', null, '4', null, 'tree', null, null, null, null, null, '1', '34', '45', '12', '1', '1'), ('8', '数据库管理', null, '5', null, 'tree', null, null, null, null, null, '1', '46', '47', '12', '1', '1'), ('9', '数据字典', 'http://192.168.110.25:8080/WebReport/ReportServer?reportlet=finereport7%2FMM%2Fcheck_detail.cpt&op=view', '4', 'layui-icon-read', 'leaf', null, null, null, null, null, '1', '19', '20', '12', '2', '4'), ('10', '日志管理', '', '5', 'layui-icon-file-b', 'leaf', null, null, null, null, null, '1', '21', '22', '12', '2', '4'), ('11', '登录管理', 'online_page', '6', 'layui-icon-log', 'leaf', null, null, null, null, null, '1', '15', '16', '12', '2', '4'), ('12', '权限管理', null, '1', 'layui-icon-auz', 'tree', null, null, null, null, null, '1', '5', '14', '12', '2', '4'), ('13', '系统用户', 'user_page', '1', 'layui-icon-user', 'leaf', null, null, null, null, null, '1', '49', '50', '12', '2', '5'), ('14', '菜单管理', 'menu_page', '3', 'layui-icon-more', 'leaf', null, null, null, null, null, '1', '17', '18', '12', '2', '4'), ('15', '角色（基础权限）', 'role_page', '1', 'layui-icon-face-smile-fine', 'leaf', null, null, null, null, null, '1', '6', '7', '12', '3', '12'), ('16', '按钮权限', null, '2', 'layui-icon-template', 'leaf', null, null, null, null, null, '1', '8', '9', '12', '3', '12'), ('44', '测试菜单树', '', '5', '', 'tree', null, null, null, null, null, '1', '1', '54', '13', '0', null), ('66', '测试菜单叶1', '', '1', '', 'tree', null, null, null, null, null, '1', '42', '43', '13', '1', '44'), ('67', '测试菜单叶2', '', '2', '', 'tree', null, null, null, null, null, '1', '44', '45', '13', '1', '44'), ('68', '测试菜单叶5', '', '5', '', 'tree', null, null, null, null, null, '1', '46', '47', '13', '1', '44'), ('69', '测试菜单叶3', '', '3', '', 'tree', null, null, null, null, null, '1', '48', '49', '13', '1', '44'), ('70', '测试菜单叶4', '', '4', '', 'tree', null, null, null, null, null, '1', '50', '51', '13', '1', '44'), ('71', '测试菜单叶6', '', '6', '', 'tree', null, null, null, null, null, '1', '52', '53', '13', '1', '44'), ('72', '代码生成器', '', '1', '', 'tree', null, null, null, null, null, '1', '35', '42', '12', '2', '7'), ('73', '普通列表', 'test', '1', 'layui-icon-note', 'leaf', null, null, null, null, null, '1', '38', '39', '12', '3', '72'), ('74', '树型列表', '', '2', 'layui-icon-tree', 'leaf', null, null, null, null, null, '0', '36', '37', '12', '3', '72'), ('75', '普通列表 实例', 'generate_page', '3', 'layui-icon-tabs', 'leaf', null, null, null, null, null, '1', '40', '41', '12', '3', '72'), ('76', '界面设置', 'interface_home', '6', 'layui-icon-layer', 'leaf', null, null, null, null, null, '1', '23', '24', '12', '2', '4'), ('77', 'icon_列表', 'icon_list', '2', 'layui-icon-rate-half', 'leaf', null, null, null, null, null, '1', '43', '44', '12', '2', '7');
COMMIT;

-- ----------------------------
--  Table structure for `sys_online`
-- ----------------------------
DROP TABLE IF EXISTS `sys_online`;
CREATE TABLE `sys_online` (
  `online_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `online_date` datetime(6) NOT NULL,
  PRIMARY KEY (`online_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_online`
-- ----------------------------
BEGIN;
INSERT INTO `sys_online` VALUES ('1', '0e42282188bd4068bd4a57af3b9a7630', '2019-08-15 17:31:21.256519'), ('2', '0e42282188bd4068bd4a57af3b9a7630', '2019-08-15 18:26:24.703272'), ('3', '0e42282188bd4068bd4a57af3b9a7630', '2019-08-15 18:59:38.830370'), ('4', '0e42282188bd4068bd4a57af3b9a7630', '2019-08-15 21:04:38.054974');
COMMIT;

-- ----------------------------
--  Table structure for `sys_role`
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role` (
  `role_id` varchar(50) NOT NULL,
  `role_name` varchar(30) NOT NULL,
  `role_menu_rights` varchar(255) DEFAULT NULL,
  `role_create_rights` varchar(255) DEFAULT NULL,
  `role_delete_rights` varchar(255) DEFAULT NULL,
  `role_update_rights` varchar(255) DEFAULT NULL,
  `role_select_rights` varchar(255) DEFAULT NULL,
  `role_order` varchar(30) NOT NULL,
  `is_active` int(11) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_role`
-- ----------------------------
BEGIN;
INSERT INTO `sys_role` VALUES ('1', '系统管理员', '1', '1,4,9,10,11,12,15,16,14,5,13,7,72,73,74,75,8,3', '1,4,9,10,11,12,15,16,14,5,13,7,72,73,74,75,8', '1,4,9,10,11,12,15,16,14,5,13,7,72,73,74,75,8,3', '1,4,9,10,11,12,15,16,14,5,13,7,72,73,74,75,8,2,3', '1', '1'), ('2', '开发者', '2,3', '2,3', '2,3', '2,3', '2,3', '2', '1'), ('3', '访客', '1', '1', '1', '1', '1', '3', '1');
COMMIT;

-- ----------------------------
--  Table structure for `sys_Test`
-- ----------------------------
DROP TABLE IF EXISTS `sys_Test`;
CREATE TABLE `sys_Test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_name` varchar(255) DEFAULT NULL,
  `img_url` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Table structure for `sys_user`
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user` (
  `user_id` char(32) NOT NULL,
  `user_full_name` varchar(30) DEFAULT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_password` varchar(30) NOT NULL,
  `user_email` varchar(45) DEFAULT NULL,
  `user_sex` int(11) NOT NULL,
  `user_phone_number` varchar(20) DEFAULT NULL,
  `user_card` varchar(30) NOT NULL,
  `createby` varchar(32) NOT NULL,
  `createtime` datetime(6) NOT NULL,
  `updateby` varchar(32) DEFAULT NULL,
  `updatetime` datetime(6) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `img_url` varchar(100) DEFAULT NULL,
  `role_id` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `sys_user_role_id_8a2e10d7_fk_sys_role_role_id` (`role_id`),
  CONSTRAINT `sys_user_role_id_8a2e10d7_fk_sys_role_role_id` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
--  Records of `sys_user`
-- ----------------------------
BEGIN;
INSERT INTO `sys_user` VALUES ('0e42282188bd4068bd4a57af3b9a7610', '系统测试', '1231345', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7630', '系统管理员', 'admin', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7631', '系统测试', '14124124', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7632', '系统测试', '1412412123', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7633', '系统测试', 'admi', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7634', '系统测试', '141241233242', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7635', '系统测试', '141241241', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7636', '系统测试', '1412412411', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7637', '系统测试', '1412412414', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7638', '系统测试', '1412412416', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1'), ('0e42282188bd4068bd4a57af3b9a7639', '系统测试', '14124124164564', '123123', '936669361@qq.com', '1', '17690752702', '650108199807020012', '0e42282188bd4068bd4a57af3b9a7630', '2019-06-28 13:30:58.102893', '0e42282188bd4068bd4a57af3b9a7630', null, '1', 'img/7c2bb08c3c707d11978b4578e468d3b1.jpg', '1');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
