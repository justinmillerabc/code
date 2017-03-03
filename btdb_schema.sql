-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: btdb
-- ------------------------------------------------------
-- Server version	5.5.54-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sales_order`
--

DROP TABLE IF EXISTS `sales_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sales_order` (
  `so_number` int(11) NOT NULL,
  `so_date_created` datetime DEFAULT NULL,
  `so_created_by` varchar(50) DEFAULT NULL,
  `so_branch_office` varchar(100) DEFAULT NULL,
  `so_location` varchar(100) DEFAULT NULL,
  `so_classification` varchar(100) DEFAULT NULL,
  `so_status` varchar(20) DEFAULT NULL,
  `so_reference` varchar(256) DEFAULT NULL,
  `so_confirm_date` datetime DEFAULT NULL,
  `work_in_progress_state` varchar(100) DEFAULT NULL,
  `patient_id` int(11) NOT NULL,
  `ordering_doctor_city` varchar(50) DEFAULT NULL,
  `ordering_doctor_state` varchar(50) DEFAULT NULL,
  `insurance_pri_payor` varchar(100) DEFAULT NULL,
  `marketing_rep_fullname` varchar(50) DEFAULT NULL,
  `referral_name` varchar(50) DEFAULT NULL,
  `referral_city` varchar(50) DEFAULT NULL,
  `referral_state` varchar(50) DEFAULT NULL,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sales_order_confirmed`
--

DROP TABLE IF EXISTS `sales_order_confirmed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sales_order_confirmed` (
  `so_number` int(11) NOT NULL,
  `so_date_created` datetime DEFAULT NULL,
  `so_created_by` varchar(100) DEFAULT NULL,
  `so_branch_office` varchar(100) DEFAULT NULL,
  `so_status` varchar(100) DEFAULT NULL,
  `so_manual_hold` varchar(100) DEFAULT NULL,
  `so_location` varchar(100) DEFAULT NULL,
  `so_po_number` varchar(100) DEFAULT NULL,
  `so_purchase_order_number` varchar(100) DEFAULT NULL,
  `so_reference` varchar(100) DEFAULT NULL,
  `so_user1` varchar(100) DEFAULT NULL,
  `so_user2` varchar(100) DEFAULT NULL,
  `so_user3` varchar(100) DEFAULT NULL,
  `so_user4` varchar(100) DEFAULT NULL,
  `so_confirm_date` datetime DEFAULT NULL,
  `so_confirmed_by` varchar(100) DEFAULT NULL,
  `so_last_printed` datetime DEFAULT NULL,
  `so_note` text,
  `so_classification` varchar(100) DEFAULT NULL,
  `so_type` varchar(100) DEFAULT NULL,
  `so_manual_hold_reason` varchar(100) DEFAULT NULL,
  `so_custom_fields_field1` varchar(100) DEFAULT NULL,
  `so_custom_fields_field2` varchar(100) DEFAULT NULL,
  `so_custom_fields_field3` varchar(100) DEFAULT NULL,
  `so_custom_fields_field4` varchar(100) DEFAULT NULL,
  `so_custom_fields_field5` varchar(100) DEFAULT NULL,
  `so_custom_fields_field6` varchar(100) DEFAULT NULL,
  `so_custom_fields_field7` varchar(100) DEFAULT NULL,
  `so_custom_fields_field8` varchar(100) DEFAULT NULL,
  `so_custom_fields_field9` varchar(100) DEFAULT NULL,
  `so_custom_fields_field10` varchar(100) DEFAULT NULL,
  `so_custom_fields_field11` varchar(100) DEFAULT NULL,
  `so_custom_fields_field12` varchar(100) DEFAULT NULL,
  `so_custom_fields_field13` varchar(100) DEFAULT NULL,
  `so_custom_fields_field14` varchar(100) DEFAULT NULL,
  `so_custom_fields_field15` varchar(100) DEFAULT NULL,
  `so_custom_fields_field16` varchar(100) DEFAULT NULL,
  `so_custom_fields_field17` varchar(100) DEFAULT NULL,
  `so_custom_fields_field18` varchar(100) DEFAULT NULL,
  `so_custom_fields_field19` varchar(100) DEFAULT NULL,
  `so_hold_cmn_not_logged` tinyint(1) NOT NULL DEFAULT '0',
  `so_hold_cmn_expired` tinyint(1) NOT NULL DEFAULT '0',
  `so_hold_par_not_logged` tinyint(1) NOT NULL DEFAULT '0',
  `so_hold_par_expired` tinyint(1) NOT NULL DEFAULT '0',
  `so_hold_manual_hold` tinyint(1) NOT NULL DEFAULT '0',
  `so_stop_pending_pickup` tinyint(1) NOT NULL DEFAULT '0',
  `so_stop_multiple_pricing_options` varchar(100) DEFAULT NULL,
  `so_stop_policy_expired` tinyint(1) NOT NULL DEFAULT '0',
  `so_stop_no_pricing_found` tinyint(1) NOT NULL DEFAULT '0',
  `so_stop_policy_changed` tinyint(1) NOT NULL DEFAULT '0',
  `so_stop_manual_stop_date` datetime DEFAULT NULL,
  `so_stop_automatic_eligibility_check` varchar(100) DEFAULT NULL,
  `so_stop_ineligible_policy` varchar(100) DEFAULT NULL,
  `so_delivery_note` text,
  `work_in_progress_wip_state` varchar(100) DEFAULT NULL,
  `work_in_progress_assigned_to` varchar(100) DEFAULT NULL,
  `work_in_progress_completed` tinyint(1) NOT NULL DEFAULT '0',
  `work_in_progress_wip_days_in_state` varchar(100) DEFAULT NULL,
  `sleep_therapy_solution` varchar(100) DEFAULT NULL,
  `sleep_therapy_external_patient_id` int(11) NOT NULL,
  `marketing_rep_last_name` varchar(100) DEFAULT NULL,
  `marketing_rep_first_name` varchar(100) DEFAULT NULL,
  `marketing_rep_full_name` varchar(100) DEFAULT NULL,
  `practitioner_last_name` varchar(100) DEFAULT NULL,
  `practitioner_first_name` varchar(100) DEFAULT NULL,
  `practitioner_middle_name` varchar(100) DEFAULT NULL,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_delivery`
--

DROP TABLE IF EXISTS `soc_delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_delivery` (
  `so_number` int(11) NOT NULL,
  `delivery_scheduled_date` datetime DEFAULT NULL,
  `delivery_actual_date` datetime DEFAULT NULL,
  `delivery_address1` varchar(100) DEFAULT NULL,
  `delivery_address2` varchar(100) DEFAULT NULL,
  `delivery_city` varchar(100) DEFAULT NULL,
  `delivery_state` varchar(100) DEFAULT NULL,
  `delivery_county` varchar(100) DEFAULT NULL,
  `delivery_country` varchar(100) DEFAULT NULL,
  `delivery_postal_code` varchar(100) DEFAULT NULL,
  `delivery_phone` varchar(100) DEFAULT NULL,
  `delivery_fax` varchar(100) DEFAULT NULL,
  `delivery_tax_zone` varchar(100) DEFAULT NULL,
  `delivery_tax_rate` varchar(100) DEFAULT NULL,
  `delivery_technician` varchar(100) DEFAULT NULL,
  `delivery_bright_ship_status` varchar(100) DEFAULT NULL,
  `delivery_bright_ship_carrier` varchar(100) DEFAULT NULL,
  `delivery_bright_ship_method` varchar(100) DEFAULT NULL,
  `delivery_bright_ship_tracking_numbers` varchar(100) DEFAULT NULL,
  `delivery_fulfillment_vendor` varchar(100) DEFAULT NULL,
  `delivery_account_number` varchar(100) DEFAULT NULL,
  `delivery_ship_by` varchar(100) DEFAULT NULL,
  `delivery_status` varchar(100) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_delivery_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Delivery';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_diagnosis`
--

DROP TABLE IF EXISTS `soc_diagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_diagnosis` (
  `so_number` int(11) NOT NULL,
  `so_diagnosis_codes_dxicd-10_code_x0023_01` varchar(200) DEFAULT NULL,
  `so_diagnosis_codes_dxicd-10_description_x0023_01` varchar(200) DEFAULT NULL,
  `so_diagnosis_codes_dxicd-10_code_x0023_02` varchar(200) DEFAULT NULL,
  `so_diagnosis_codes_dxicd-10_description_x0023_02` varchar(200) DEFAULT NULL,
  `so_diagnosis_codes_dxicd-10_code_x0023_03` varchar(200) DEFAULT NULL,
  `so_diagnosis_codes_dxicd-10_description_x0023_03` varchar(200) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_diagnosis_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Diagnosis';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_insurance`
--

DROP TABLE IF EXISTS `soc_insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_insurance` (
  `so_number` int(11) NOT NULL,
  `insurance_pri_payor` varchar(100) DEFAULT NULL,
  `insurance_pri_policy_x0023_` varchar(100) DEFAULT NULL,
  `insurance_pri_policy_verified` varchar(100) DEFAULT NULL,
  `insurance_pri_pay_pct` varchar(100) DEFAULT NULL,
  `insurance_sec_payor` varchar(100) DEFAULT NULL,
  `insurance_sec_policy_x0023_` varchar(100) DEFAULT NULL,
  `insurance_sec_policy_verified` varchar(100) DEFAULT NULL,
  `insurance_sec_payPct` varchar(100) DEFAULT NULL,
  `insurance_ter_payor` varchar(100) DEFAULT NULL,
  `insurance_ter_policy_x0023_` varchar(100) DEFAULT NULL,
  `insurance_insurance_verified` varchar(50) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_insurance_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Insurance';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_ordering_doctor`
--

DROP TABLE IF EXISTS `soc_ordering_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_ordering_doctor` (
  `so_number` int(11) NOT NULL,
  `ordering_doctor_last_name` varchar(100) DEFAULT NULL,
  `ordering_doctor_first_name` varchar(100) DEFAULT NULL,
  `ordering_doctor_address1` varchar(100) DEFAULT NULL,
  `ordering_doctor_address2` varchar(100) DEFAULT NULL,
  `ordering_doctor_city` varchar(100) DEFAULT NULL,
  `ordering_doctor_state` varchar(100) DEFAULT NULL,
  `ordering_doctor_postal_code` varchar(100) DEFAULT NULL,
  `ordering_doctor_phone` varchar(100) DEFAULT NULL,
  `ordering_doctor_fax` varchar(100) DEFAULT NULL,
  `ordering_doctor_fax_to` varchar(100) DEFAULT NULL,
  `ordering_doctor_pecos_certify_status` varchar(100) DEFAULT NULL,
  `ordering_doctor_full_name` varchar(100) DEFAULT NULL,
  `ordering_doctor_group` varchar(100) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_ordering_doctor_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Ordering Doctor';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_patient`
--

DROP TABLE IF EXISTS `soc_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_patient` (
  `so_number` int(11) NOT NULL,
  `patient_email_address` varchar(100) DEFAULT NULL,
  `patient_id` int(11) NOT NULL,
  `patient_date_created` datetime DEFAULT NULL,
  `patient_delivery_note` text,
  `patient_branch` varchar(100) DEFAULT NULL,
  `patient_bpc_auto_pay_status` varchar(100) DEFAULT NULL,
  `patient_bpc_edelivery_status` varchar(100) DEFAULT NULL,
  `patient_bpc_payment_plan` varchar(100) DEFAULT NULL,
  `patient_bpc_information` varchar(100) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_patient_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Patient';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `soc_referral`
--

DROP TABLE IF EXISTS `soc_referral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_referral` (
  `so_number` int(11) NOT NULL,
  `referral_type` varchar(100) DEFAULT NULL,
  `referral_name` varchar(100) DEFAULT NULL,
  `referral_address1` varchar(100) DEFAULT NULL,
  `referral_city` varchar(100) DEFAULT NULL,
  `referral_state` varchar(100) DEFAULT NULL,
  `referral_zip` varchar(100) DEFAULT NULL,
  `referral_phone` varchar(100) DEFAULT NULL,
  `referral_fax` varchar(100) DEFAULT NULL,
  `referral_doctor_group` varchar(100) DEFAULT NULL,
  `referral_facility_group` varchar(100) DEFAULT NULL,
  KEY `so_number` (`so_number`),
  CONSTRAINT `soc_referral_ibfk_1` FOREIGN KEY (`so_number`) REFERENCES `sales_order_confirmed` (`so_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Sales Order Confirmed - Referral';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-25 14:07:50
