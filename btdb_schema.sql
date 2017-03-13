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
-- Table structure for table `invoices_created`
--

DROP TABLE IF EXISTS `invoices_created`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices_created` (
  `invoice_number` int(11) NOT NULL,
  `invoice_status` varchar(100) DEFAULT NULL,
  `invoice_sales_order_number` int(11) NOT NULL,
  `invoice_date_created` datetime DEFAULT NULL,
  `invoice_dateof_service` datetime DEFAULT NULL,
  `invoice_holdfromprinting_x002_f_submission` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_medicare_deductible_hold` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_reprint_x002_f_re_submit_claim` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_span_date_hold` datetime DEFAULT NULL,
  `invoice_branch` varchar(100) DEFAULT NULL,
  `invoice_so_reference` varchar(100) DEFAULT NULL,
  `invoice_branch_group` varchar(100) DEFAULT NULL,
  `invoice_box19` varchar(100) DEFAULT NULL,
  `invoice_so_place_of_service` varchar(100) DEFAULT NULL,
  `invoice_so_classification` varchar(100) DEFAULT NULL,
  `invoice_so_note` text,
  `invoice_so_manual_hold_reason` varchar(100) DEFAULT NULL,
  `invoice_so_created_by` varchar(100) DEFAULT NULL,
  `invoice_so_confirmed_by` varchar(100) DEFAULT NULL,
  `invoice_submission_type` varchar(100) DEFAULT NULL,
  `invoice_key` varchar(100) DEFAULT NULL,
  `invoice_balances_charge_total` varchar(100) DEFAULT NULL,
  `invoice_balances_allow_total` varchar(100) DEFAULT NULL,
  `invoice_balances_tax_total` varchar(100) DEFAULT NULL,
  `invoice_balances_adjustments` varchar(100) DEFAULT NULL,
  `invoice_balances_payments` varchar(100) DEFAULT NULL,
  `invoice_balances_balance` varchar(100) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `policy_payor_name` varchar(100) DEFAULT NULL,
  `policy_payor_id` int(11) DEFAULT NULL,
  `policy_x0023` varchar(100) DEFAULT NULL,
  `policy_group_x0023` varchar(100) DEFAULT NULL,
  `policy_pay` varchar(100) DEFAULT NULL,
  `policy_claim_form` varchar(100) DEFAULT NULL,
  `policy_payor_level` varchar(100) DEFAULT NULL,
  `policy_plan_type` varchar(100) DEFAULT NULL,
  `policy_do_not_print_secondary_claims` varchar(100) DEFAULT NULL,
  `invoice_detail_item_id` varchar(100) DEFAULT NULL,
  `invoice_detail_item_name` varchar(100) DEFAULT NULL,
  `invoice_detail_dos_from` datetime DEFAULT NULL,
  `invoice_detail_dos_to` datetime DEFAULT NULL,
  `invoice_detail_billing_period` varchar(100) DEFAULT NULL,
  `invoice_detail_reprint_x002_f_resubmit_item` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_detail_charge` varchar(100) DEFAULT NULL,
  `invoice_detail_allow` varchar(100) DEFAULT NULL,
  `invoice_detail_tax` varchar(100) DEFAULT NULL,
  `invoice_detail_payments` varchar(100) DEFAULT NULL,
  `invoice_detail_balance` varchar(100) DEFAULT NULL,
  `invoice_detail_qty` decimal(6,2) unsigned NOT NULL DEFAULT '0.00',
  `invoice_detail_inventory_qty` decimal(6,2) unsigned DEFAULT NULL,
  `invoice_detail_proc_code` varchar(100) DEFAULT NULL,
  `invoice_detail_modifier1` varchar(100) DEFAULT NULL,
  `invoice_detail_modifier2` varchar(100) DEFAULT NULL,
  `invoice_detail_modifier3` varchar(100) DEFAULT NULL,
  `invoice_detail_modifier4` varchar(100) DEFAULT NULL,
  `invoice_detail_abn_proc_code` varchar(100) DEFAULT NULL,
  `invoice_detail_price_type` varchar(100) DEFAULT NULL,
  `invoice_detail_so_item_note` text,
  `invoice_detail_par_number` varchar(100) DEFAULT NULL,
  `marketing_rep_full_name` varchar(100) DEFAULT NULL,
  `ordering_doctor_key` varchar(50) DEFAULT NULL,
  `ordering_doctor_npi` varchar(100) DEFAULT NULL,
  `serial_numbers_serial_number` varchar(100) DEFAULT NULL,
  `sales_order_hold_cmn_not_logged` varchar(100) DEFAULT NULL,
  `sales_order_hold_cmn_expired` varchar(100) DEFAULT NULL,
  `sales_order_hold_par_not_logged` varchar(100) DEFAULT NULL,
  `sales_order_hold_par_expired` varchar(100) DEFAULT NULL,
  `sales_order_hold_manual_hold` varchar(100) DEFAULT NULL,
  `sales_order_stop_pending_pickup` varchar(100) DEFAULT NULL,
  `sales_order_stop_multiple_pricing_options` varchar(100) DEFAULT NULL,
  `sales_order_stop_policy_expired` varchar(100) DEFAULT NULL,
  `sales_order_stop_no_pricing_found` varchar(100) DEFAULT NULL,
  `sales_order_stop_policy_changed` varchar(100) DEFAULT NULL,
  `sales_order_stop_manual_stop_date` datetime DEFAULT NULL,
  `work_in_progress_wip_state` varchar(100) DEFAULT NULL,
  `work_in_progress_assigned_to` varchar(100) DEFAULT NULL,
  `work_in_progress_completed` tinyint(1) NOT NULL DEFAULT '0',
  `work_in_progress_wip_days_in_state` varchar(100) DEFAULT NULL,
  `primary_invoice_primary_invoice_number` varchar(100) DEFAULT NULL,
  `primary_invoice_primary_insurance_name` varchar(100) DEFAULT NULL,
  `secondary_invoice_secondary_invoice_number` varchar(100) DEFAULT NULL,
  `secondary_invoice_secondary_insurance_name` varchar(100) DEFAULT NULL,
  `tertiary_invoice_tertiary_invoice_number` varchar(100) DEFAULT NULL,
  `tertiary_invoice_tertiary_insurance_name` varchar(100) DEFAULT NULL,
  `patient_invoice_patient_invoice_number` int(11) DEFAULT NULL,
  `patient_invoice_patient_insurance_name` varchar(100) DEFAULT NULL,
  `responsible_party_relationship` varchar(100) DEFAULT NULL,
  `responsible_party_phone` varchar(100) DEFAULT NULL,
  `responsible_party_email_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`invoice_number`,`invoice_detail_item_id`,`invoice_detail_qty`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Invoice Created';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `invoices_status`
--

DROP TABLE IF EXISTS `invoices_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoices_status` (
  `invoice_number` int(11) NOT NULL,
  `invoice_status` varchar(100) DEFAULT NULL,
  `invoice_sales_order_number` int(11) NOT NULL,
  `invoice_holdfromprinting_x002_f_submission` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_medicare_deductible_hold` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_user_manual_hold` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_holdfrom_billing_statement` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_so_manual_hold_reason` varchar(100) DEFAULT NULL,
  `invoice_biller_x002_f_collector` varchar(100) DEFAULT NULL,
  `invoice_last_printed` datetime DEFAULT NULL,
  `invoice_last_date_worked` datetime DEFAULT NULL,
  `invoice_follow_up_date` datetime DEFAULT NULL,
  `invoice_collection_type` varchar(100) DEFAULT NULL,
  `invoice_collect_action_x002_f_status` varchar(100) DEFAULT NULL,
  `invoice_pro_med_status_code` varchar(100) DEFAULT NULL,
  `invoice_pro_med_status_code_date` datetime DEFAULT NULL,
  `invoice_appeals_due_date` datetime DEFAULT NULL,
  `balances_charge_total` varchar(100) DEFAULT NULL,
  `balances_allow_total` varchar(100) DEFAULT NULL,
  `balances_tax_total` varchar(100) DEFAULT NULL,
  `balances_adjustments` varchar(100) DEFAULT NULL,
  `balances_balance` varchar(100) DEFAULT NULL,
  `balances_payments` varchar(100) DEFAULT NULL,
  `sales_order_hold_cmn_not_logged` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_hold_cmn_expired` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_hold_par_not_logged` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_hold_par_expired` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_hold_manual_hold` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_pending_pickup` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_multiple_pricing_options` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_policy_expired` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_no_pricing_found` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_policy_changed` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_manual_stop_date` datetime DEFAULT NULL,
  `sales_order_stop_automatic_eligibility_check` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_stop_ineligible_policy` tinyint(1) NOT NULL DEFAULT '0',
  `work_in_progress_wip_state` varchar(100) DEFAULT NULL,
  `work_in_progress_assigned_to` varchar(100) DEFAULT NULL,
  `work_in_progress_completed` tinyint(1) NOT NULL DEFAULT '0',
  `work_in_progress_wip_days_in_state` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`invoice_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Invoice Status';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pars_created`
--

DROP TABLE IF EXISTS `pars_created`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pars_created` (
  `par_number` varchar(100) NOT NULL DEFAULT '',
  `par_descr` varchar(100) DEFAULT NULL,
  `par_exclude_from_par_report` tinyint(1) NOT NULL DEFAULT '0',
  `par_exclude_from_claim` tinyint(1) NOT NULL DEFAULT '0',
  `par_status` varchar(100) DEFAULT NULL,
  `par_create_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `par_created_by` varchar(100) DEFAULT NULL,
  `par_logged_by` varchar(100) DEFAULT NULL,
  `par_insurance` varchar(100) DEFAULT NULL,
  `par_branch` varchar(100) DEFAULT NULL,
  `par_printed_by` varchar(100) DEFAULT NULL,
  `par_faxed_by` varchar(100) DEFAULT NULL,
  `par_purchase_quantity_limits_proc_code` varchar(100) NOT NULL DEFAULT '',
  `par_purchase_quantity_limits_approved_qty` decimal(6,2) unsigned DEFAULT NULL,
  `par_purchase_quantity_limits_returned_qty` decimal(6,2) unsigned DEFAULT NULL,
  `par_purchase_quantity_limits_used_qty` decimal(6,2) unsigned DEFAULT NULL,
  `par_purchase_quantity_limits_adjusted_qty` decimal(6,2) unsigned DEFAULT NULL,
  `sales_order_number` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `patient_key` varchar(100) DEFAULT NULL,
  `insurance_pri_payor` varchar(100) DEFAULT NULL,
  `insurance_pri_payor_id` int(11) NOT NULL,
  `insurance_pri_policy_x0023` varchar(100) DEFAULT NULL,
  `cmncmn_form` varchar(100) DEFAULT NULL,
  `cmncmn_exp` varchar(100) DEFAULT NULL,
  `cmncmn_init` varchar(100) DEFAULT NULL,
  `cmncmn_status` varchar(100) DEFAULT NULL,
  `cmncmn_log_date` datetime DEFAULT NULL,
  `cmncmn_lengthof_need` varchar(100) DEFAULT NULL,
  `cmn_excludefrom_cmn_report` tinyint(1) NOT NULL DEFAULT '0',
  `cmncmn_faxed_by` varchar(100) DEFAULT NULL,
  `cmncmn_placeholder` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`par_number`,`par_purchase_quantity_limits_proc_code`,`patient_id`,`par_create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='PARS Created';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pars_logged`
--

DROP TABLE IF EXISTS `pars_logged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pars_logged` (
  `par_number` varchar(100) NOT NULL DEFAULT '',
  `par_descr` varchar(100) DEFAULT NULL,
  `par_init` varchar(100) DEFAULT NULL,
  `par_exclude_from_par_report` tinyint(1) NOT NULL DEFAULT '0',
  `par_exclude_from_claim` tinyint(1) NOT NULL DEFAULT '0',
  `par_status` varchar(100) DEFAULT NULL,
  `par_create_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `par_created_by` varchar(100) DEFAULT NULL,
  `par_logged_date` datetime DEFAULT NULL,
  `par_logged_by` varchar(100) DEFAULT NULL,
  `par_insurance` varchar(100) DEFAULT NULL,
  `par_branch` varchar(100) DEFAULT NULL,
  `par_printed_by` varchar(100) DEFAULT NULL,
  `par_faxed_by` varchar(100) DEFAULT NULL,
  `par_purchase_quantity_limits_proc_code` varchar(100) NOT NULL DEFAULT '',
  `par_purchase_quantity_limits_approved_qty` varchar(100) DEFAULT NULL,
  `par_purchase_quantity_limits_returned_qty` varchar(100) DEFAULT NULL,
  `par_purchase_quantity_limits_used_qty` varchar(100) DEFAULT NULL,
  `par_purchase_quantity_limits_adjusted_qty` varchar(100) DEFAULT NULL,
  `sales_order_number` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL DEFAULT '0',
  `patient_key` int(11) DEFAULT NULL,
  `insurance_pri_payor` varchar(100) DEFAULT NULL,
  `insurance_pri_payor_id` int(11) DEFAULT NULL,
  `insurance_pri_policy_x0023` varchar(100) DEFAULT NULL,
  `cmncmn_form` varchar(100) DEFAULT NULL,
  `cmncmn_exp` varchar(100) DEFAULT NULL,
  `cmncmn_init` varchar(100) DEFAULT NULL,
  `cmncmn_status` varchar(100) DEFAULT NULL,
  `cmncmn_log_date` datetime DEFAULT NULL,
  `cmncmn_lengthof_need` varchar(100) DEFAULT NULL,
  `cmn_excludefrom_cmn_report` tinyint(1) NOT NULL DEFAULT '0',
  `cmncmn_faxed_by` varchar(100) DEFAULT NULL,
  `cmncmn_placeholder` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`par_number`,`par_purchase_quantity_limits_proc_code`,`patient_id`,`par_create_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='PARS Logged';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `payment_check_x002_f_reference` varchar(100) DEFAULT NULL,
  `payment_type` varchar(100) DEFAULT NULL,
  `payment_created_by` varchar(100) DEFAULT NULL,
  `payment_create_date` datetime DEFAULT NULL,
  `payment_date` datetime DEFAULT NULL,
  `payment_post_date` datetime DEFAULT NULL,
  `payment_posted_by` varchar(100) DEFAULT NULL,
  `payment_description` varchar(100) DEFAULT NULL,
  `payment_amount` varchar(100) DEFAULT NULL,
  `payment_gl_period` varchar(100) DEFAULT NULL,
  `payment_gl_year` varchar(100) DEFAULT NULL,
  `payment_gl_start_date` datetime DEFAULT NULL,
  `payment_gl_end_date` datetime DEFAULT NULL,
  `receipt_id` int(11) DEFAULT NULL,
  `receipt_type` varchar(100) DEFAULT NULL,
  `receipt_check_x002_f_reference` varchar(100) DEFAULT NULL,
  `receipt_note` text,
  `deposit_created_by` varchar(100) DEFAULT NULL,
  `deposit_posted_by` varchar(100) DEFAULT NULL,
  `deposit_reference` varchar(100) DEFAULT NULL,
  `deposit_description` varchar(100) DEFAULT NULL,
  `invoice_number` int(11) NOT NULL,
  `invoice_status` varchar(100) DEFAULT NULL,
  `invoice_sales_order_number` int(11) NOT NULL,
  `invoice_date_created` datetime DEFAULT NULL,
  `invoice_date_opened` datetime DEFAULT NULL,
  `invoice_last_submitted` datetime DEFAULT NULL,
  `invoice_last_printed` datetime DEFAULT NULL,
  `invoice_dateof_service` datetime DEFAULT NULL,
  `invoice_holdfromprinting_x002_f_submission` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_reprint_x002_f_re_submit_claim` tinyint(1) NOT NULL DEFAULT '0',
  `invoice_branch` varchar(100) DEFAULT NULL,
  `invoice_note` text,
  `invoice_so_created_by` varchar(100) DEFAULT NULL,
  `invoice_so_confirmed_by` varchar(100) DEFAULT NULL,
  `invoice_balances_charge_total` varchar(100) DEFAULT NULL,
  `invoice_balances_allow_total` varchar(100) DEFAULT NULL,
  `invoice_balances_tax_total` varchar(100) DEFAULT NULL,
  `invoice_balances_adjustments` varchar(100) DEFAULT NULL,
  `invoice_balances_payments` varchar(100) DEFAULT NULL,
  `invoice_balances_balance` varchar(100) DEFAULT NULL,
  `invoice_biller_x002_f_collector` varchar(100) DEFAULT NULL,
  `invoice_last_date_worked` datetime DEFAULT NULL,
  `invoice_follow_up_date` datetime DEFAULT NULL,
  `invoice_collection_type` varchar(100) DEFAULT NULL,
  `invoice_collect_action_x002_f_status` varchar(100) DEFAULT NULL,
  `invoice_pro_med_status_code` varchar(100) DEFAULT NULL,
  `invoice_pro_med_status_code_date` datetime DEFAULT NULL,
  `invoice_appeals_due_date` datetime DEFAULT NULL,
  `sales_order_so_number` int(11) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `policy_payor_name` varchar(100) DEFAULT NULL,
  `policy_payor_id` int(11) DEFAULT NULL,
  `policy_x0023` varchar(100) DEFAULT NULL,
  `policy_pay` varchar(100) DEFAULT NULL,
  `invoice_detail_id` int(11) DEFAULT NULL,
  `invoice_detail_item_id` varchar(100) DEFAULT NULL,
  `marketing_rep_last_name` varchar(100) DEFAULT NULL,
  `marketing_rep_first_name` varchar(100) DEFAULT NULL,
  `related_invoice_primary_invoice_nbr` int(11) DEFAULT NULL,
  `related_invoice_secondary_invoice_nbr` int(11) DEFAULT NULL,
  `related_invoice_tertiary_invoice_nbr` int(11) DEFAULT NULL,
  `related_invoice_patient_invoice_nbr` int(11) DEFAULT NULL,
  PRIMARY KEY (`payment_id`,`invoice_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Payments';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rcm_closed`
--

DROP TABLE IF EXISTS `rcm_closed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rcm_closed` (
  `activity_task_id` int(11) NOT NULL,
  `activity_type` varchar(100) DEFAULT NULL,
  `activity` varchar(100) DEFAULT NULL,
  `priority` varchar(100) DEFAULT NULL,
  `assigned_to` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `task_status` varchar(100) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `closed_date` datetime DEFAULT NULL,
  `patient_name` varchar(100) DEFAULT NULL,
  `patient_id` int(11) DEFAULT NULL,
  `patient_branch` varchar(100) DEFAULT NULL,
  `insurance_id` int(11) DEFAULT NULL,
  `insurance_name` varchar(100) DEFAULT NULL,
  `note` text,
  `work_item_name` varchar(100) DEFAULT NULL,
  `work_item_id` int(11) NOT NULL,
  `work_item_branch` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`activity_task_id`,`work_item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='RCM Closed';
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `sleep_therapy_external_patient_id` varchar(100) DEFAULT NULL,
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
-- Table structure for table `so_void`
--

DROP TABLE IF EXISTS `so_void`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `so_void` (
  `sales_order_void_voided_sales_order_number` int(11) NOT NULL,
  `sales_order_void_void_reason` varchar(100) DEFAULT NULL,
  `sales_order_void_voided_by` varchar(100) DEFAULT NULL,
  `sales_order_void_voided_date` datetime DEFAULT NULL,
  PRIMARY KEY (`sales_order_void_voided_sales_order_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='SO VOID';
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
-- Table structure for table `soc_items`
--

DROP TABLE IF EXISTS `soc_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soc_items` (
  `sales_order_number` int(11) NOT NULL,
  `sales_order_detail_item_id` varchar(100) DEFAULT NULL,
  `sales_order_detail_item_name` varchar(100) NOT NULL DEFAULT '',
  `sales_order_detail_item_description` varchar(100) DEFAULT NULL,
  `sales_order_detail_stocking_uom` varchar(100) DEFAULT NULL,
  `sales_order_detail_original_dos` datetime DEFAULT NULL,
  `sales_order_detail_next_date_of_service` datetime DEFAULT NULL,
  `sales_order_detail_next_billing_date` datetime DEFAULT NULL,
  `sales_order_detail_special_pricing` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_price_override` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_qty` decimal(6,2) unsigned NOT NULL DEFAULT '0.00',
  `sales_order_detail_bqty` decimal(6,2) unsigned DEFAULT NULL,
  `sales_order_detail_proc_code` varchar(100) DEFAULT NULL,
  `sales_order_detail_price_option` int(11) DEFAULT '0',
  `sales_order_detail_modifier1` varchar(100) DEFAULT NULL,
  `sales_order_detail_modifier2` varchar(100) DEFAULT NULL,
  `sales_order_detail_modifier3` varchar(100) DEFAULT NULL,
  `sales_order_detail_modifier4` varchar(100) DEFAULT NULL,
  `sales_order_detail_charge` varchar(100) DEFAULT NULL,
  `sales_order_detail_allow` varchar(100) DEFAULT NULL,
  `sales_order_detail_taxable` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_non_tax_reason` varchar(100) DEFAULT NULL,
  `sales_order_detail_sale_type` varchar(100) DEFAULT NULL,
  `sales_order_detail_item_group` varchar(100) DEFAULT NULL,
  `sales_order_detail_item_user1` varchar(100) DEFAULT NULL,
  `sales_order_detail_manual_convert_to_purchase_mctp` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_mctp_charge` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_allow` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_modifier1` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_modifier2` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_modifier3` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_modifier4` varchar(100) DEFAULT NULL,
  `sales_order_detail_mctp_period` varchar(100) DEFAULT NULL,
  `sales_order_detail_addtl_modifier1` varchar(100) DEFAULT NULL,
  `sales_order_detail_addtl_modifier2` varchar(100) DEFAULT NULL,
  `sales_order_detail_addtl_modifier3` varchar(100) DEFAULT NULL,
  `sales_order_detail_addtl_modifier4` varchar(100) DEFAULT NULL,
  `sales_order_detail_price_table` varchar(100) DEFAULT NULL,
  `sales_order_detail_price_option_name` varchar(100) DEFAULT NULL,
  `sales_order_detail_extended_charge_amount` varchar(100) DEFAULT NULL,
  `sales_order_detail_extended_allowance_amount` varchar(100) DEFAULT NULL,
  `sales_order_detail_cb_pricing` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_cb_price_table_override` tinyint(1) NOT NULL DEFAULT '0',
  `sales_order_detail_cb_override` varchar(100) DEFAULT NULL,
  `sales_order_detail_messages` varchar(100) DEFAULT NULL,
  `sales_order_detail_default_vendor` varchar(100) DEFAULT NULL,
  `sales_order_detail_calories_per_day` int(11) DEFAULT '0',
  `sales_order_detail_location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sales_order_number`,`sales_order_detail_item_id`,`sales_order_detail_qty`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='SOC Items';
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

-- Dump completed on 2017-03-08 15:47:27
